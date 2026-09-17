
from fastapi import APIRouter, HTTPException
from sqlalchemy import text
import re
from difflib import get_close_matches
 
from app.database.connection_manager import connection_manager
from app.database.active_database import active_database
from app.database.connection import SessionLocal
from app.api.database_manager import UPLOAD_FOLDER
 
from app.rag.schema_reader import schema_to_text, read_schema
from app.llm.sql_generator import generate_sql
from app.llm.table_explainer import explain_table_llm
 
from app.services.approval_service import approval_service
from app.services.sql_validator import sql_validator
from app.services.result_formatter import result_formatter
from app.services.sql_executor import execute_multi
 
router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)
 
 
# ==========================================================
# Conversation Context (per user)
# ==========================================================
# In-memory only — resets when the server restarts. Good enough
# to let the AI resolve "this"/"that" within an active session.
 
LAST_CONTEXT = {}
 
 
def get_last_context(user_id):
    return LAST_CONTEXT.get(user_id)
 
 
def set_last_context(user_id, question, sql, data):
 
    LAST_CONTEXT[user_id] = {
        "question": question,
        "sql": sql,
        "data": (data or [])[:5],
    }
 
 
# ==========================================================
# Intent Detection
# ==========================================================
 
def contains_database_word(q: str) -> bool:
 
    words = re.findall(r"[a-zA-Z]+", q)
 
    for w in words:
 
        if len(w) < 3:
            continue
 
        if get_close_matches(w, ["database", "databases", "db"], n=1, cutoff=0.72):
            return True
 
    return False
 
 
def extract_requested_db_name(q: str):
 
    match = re.search(
        r"(?:named|called)\s+([a-zA-Z0-9_\-\.]+)",
        q
    )
 
    if match:
        return match.group(1)
 
    return None
 
 
def is_list_databases_query(q: str):
 
    if not contains_database_word(q):
        return False
 
    verbs = ["show", "list", "which", "what", "available", "all", "named", "called"]
 
    if not any(v in q for v in verbs):
        return False
 
    # Avoid misfiring on real data questions like
    # "show me all customers in the database"
    data_hints = [
        "table", "record", "row", "column",
        "customer", "order", "employee", "product",
        "where", "from ", "count of"
    ]
 
    if any(h in q for h in data_hints):
        return False
 
    return True
 
 
def is_explain_table_query(q: str):
 
    if "table" not in q:
        return False
 
    if "database" in q:
        return False
 
    starters = [
        "what is",
        "what's",
        "whats",
        "tell me about",
        "explain",
        "describe",
    ]
 
    return any(s in q for s in starters)
 
 
def find_mentioned_table(q: str, table_names):
 
    q_lower = q.lower()
 
    # exact substring match first (handles plural/singular typed correctly)
    for t in table_names:
        if t.lower() in q_lower:
            return t
 
    # fuzzy match each word in the question against real table names
    words = re.findall(r"[a-zA-Z]+", q_lower)
 
    lower_map = {t.lower(): t for t in table_names}
 
    for w in words:
 
        if len(w) < 3:
            continue
 
        matches = get_close_matches(
            w, list(lower_map.keys()), n=1, cutoff=0.75
        )
 
        if matches:
            return lower_map[matches[0]]
 
    return None
 
 
def extract_table_from_sql(sql: str):
 
    if not sql:
        return None
 
    match = re.search(
        r"FROM\s+[\"\[]?([a-zA-Z_][a-zA-Z0-9_]*)[\"\]]?",
        sql,
        re.IGNORECASE
    )
 
    if match:
        return match.group(1)
 
    return None
 
 
def is_describe_database_query(q: str):
 
    keywords = [
        "what tables",
        "what is this database",
        "what's in this database",
        "whats in this database",
        "describe the database",
        "describe this database",
        "database schema",
        "database structure",
        "structure of the database",
        "what does this database contain",
        "what data is in",
        "tell me about this database",
        "database overview",
        "explain this database",
        "what kind of database",
        "identify this database",
        "identify the database",
    ]
 
    return any(k in q for k in keywords)
 
 
def detect_intent(question: str):
 
    q = question.lower().strip()
 
    greetings = [
        "hi",
        "hii",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]
 
    if q in greetings:
        return "GREETING"
 
    if q in [
        "how are you",
        "how are you?"
    ]:
        return "STATUS"
 
    if q in [
        "who are you",
        "what are you",
        "introduce yourself"
    ]:
        return "ABOUT"
 
    if q in [
        "help",
        "features",
        "what can you do",
        "commands"
    ]:
        return "HELP"
 
    if q in [
        "thanks",
        "thank you",
        "ok",
        "okay"
    ]:
        return "THANKS"
 
    if q in [
        "bye",
        "goodbye",
        "see you"
    ]:
        return "BYE"
 
    if is_list_databases_query(q):
        return "LIST_DATABASES"
 
    if is_describe_database_query(q):
        return "DESCRIBE_DATABASE"
 
    if is_explain_table_query(q):
        return "EXPLAIN_TABLE"
 
    return "DATABASE"
 
 
# ==========================================================
# Conversation Responses
# ==========================================================
 
def greeting_response():
 
    return {
        "success": True,
        "answer":
            "👋 Hello! Welcome to ULEDA.\n\n"
            "I'm your Universal LLM Database Assistant.\n\n"
            "I can help you with:\n\n"
            "• 📊 Database Queries\n"
            "• 🤖 AI SQL Generation\n"
            "• 📈 Charts & Analytics\n"
            "• 📄 Reports\n"
            "• 🔍 Search Records\n"
            "• 🔐 Secure Database Operations (OTP)\n\n"
            "How can I help you today?",
        "sql": "",
        "data": [],
        "requires_permission": False
    }
 
 
def about_response():
 
    return {
        "success": True,
        "answer":
            "I'm ULEDA (Universal LLM Database Assistant).\n\n"
            "I help you interact with databases using natural language.\n\n"
            "You don't need to write SQL manually.\n\n"
            "I can generate SQL, analyze data, create charts, produce reports, and securely execute database operations using OTP verification.",
        "sql": "",
        "data": [],
        "requires_permission": False
    }
 
 
def status_response():
 
    return {
        "success": True,
        "answer":
            "I'm doing great! 😊\n\n"
            "Ready to help you work with your databases.",
        "sql": "",
        "data": [],
        "requires_permission": False
    }
 
 
def thanks_response():
 
    return {
        "success": True,
        "answer":
            "You're welcome! 😊\n\n"
            "Feel free to ask me anything about your database.",
        "sql": "",
        "data": [],
        "requires_permission": False
    }
 
 
def bye_response():
 
    return {
        "success": True,
        "answer":
            "👋 Goodbye!\n\n"
            "Have a wonderful day.\n\n"
            "Come back anytime you need help with your database.",
        "sql": "",
        "data": [],
        "requires_permission": False
    }
 
 
def help_response():
 
    return {
        "success": True,
        "answer":
            "I can help you with:\n\n"
            "• Natural Language SQL\n"
            "• Database Search\n"
            "• AI SQL Generation\n"
            "• Charts & Analytics\n"
            "• PDF / Excel Reports\n"
            "• OTP Protected Queries\n"
            "• Database Analysis\n"
            "• SQL Explanations\n"
            "• General Database Questions",
        "sql": "",
        "data": [],
        "requires_permission": False
    }
 
 
def list_databases_response(question: str = ""):
 
    files = sorted(UPLOAD_FOLDER.glob("*.db"))
 
    active_name = (
        active_database.database_name
        if active_database.is_connected()
        else None
    )
 
    requested_name = extract_requested_db_name(question.lower())
 
    if requested_name:
 
        match = next(
            (f for f in files if requested_name in f.stem.lower()),
            None
        )
 
        if match:
 
            rows = [{
                "name": match.name,
                "size_kb": round(match.stat().st_size / 1024, 2),
                "active": "Yes" if match.name == active_name else "No"
            }]
 
            answer = f"📂 Found a database matching '{requested_name}'."
 
        else:
 
            rows = []
 
            available = ", ".join(f.name for f in files) or "none"
 
            answer = (
                f"❌ No uploaded database matches '{requested_name}'.\n\n"
                f"Currently uploaded: {available}.\n\n"
                f"If you meant a table inside one of these (e.g. 'tracks'), "
                f"just ask a data question directly, like \"show me all tracks\"."
            )
 
        return {
            "success": True,
            "answer": answer,
            "sql": "-- Uploaded database files\nSELECT name, size_kb, active FROM uploaded_databases;",
            "data": rows,
            "rows": len(rows),
            "requires_permission": False
        }
 
    rows = []
 
    for f in files:
        rows.append({
            "name": f.name,
            "size_kb": round(f.stat().st_size / 1024, 2),
            "active": "Yes" if f.name == active_name else "No"
        })
 
    if not rows:
        answer = (
            "📂 No databases have been uploaded yet.\n\n"
            "Upload a .db file from the sidebar to get started."
        )
    else:
        answer = f"📂 Found {len(rows)} database(s)."
 
    return {
        "success": True,
        "answer": answer,
        "sql": "-- Uploaded database files\nSELECT name, size_kb, active FROM uploaded_databases;",
        "data": rows,
        "rows": len(rows),
        "requires_permission": False
    }
 
 
def describe_database_response():
 
    if not active_database.is_connected():
 
        return {
            "success": True,
            "answer":
                "📭 No database is connected right now.\n\n"
                "Upload or select a database first, then ask me again.",
            "sql": "",
            "data": [],
            "requires_permission": False
        }
 
    schema = read_schema()
 
    session = connection_manager.get_session()
 
    rows = []
 
    try:
 
        for table in schema["tables"]:
 
            table_name = table["table_name"]
 
            try:
                row_count = session.execute(
                    text(f'SELECT COUNT(*) FROM "{table_name}"')
                ).scalar()
 
            except Exception:
                row_count = "?"
 
            rows.append({
                "table": table_name,
                "columns": len(table["columns"]),
                "primary_key": ", ".join(table["primary_keys"]) or "-",
                "rows": row_count
            })
 
    finally:
        session.close()
 
    answer = (
        f"🗄️ Connected database: {active_database.database_name} "
        f"({schema['database_type']}).\n\n"
        f"It has {len(rows)} table(s). Ask me anything about the data inside them, "
        f"e.g. \"show me the top 10 rows from {rows[0]['table']}\"."
        if rows else
        f"🗄️ Connected database: {active_database.database_name} "
        f"({schema['database_type']}).\n\nIt has no tables yet."
    )
 
    return {
        "success": True,
        "answer": answer,
        "sql": "-- Database schema overview\nSELECT table_name, columns, primary_key, row_count FROM information_schema;",
        "data": rows,
        "rows": len(rows),
        "requires_permission": False
    }
 
 
def explain_table_response(question: str, user_id: str):
 
    if not active_database.is_connected():
 
        return {
            "success": True,
            "answer":
                "📭 No database is connected right now.\n\n"
                "Upload or select a database first, then ask me again.",
            "sql": "",
            "data": [],
            "requires_permission": False
        }
 
    schema = read_schema()
 
    table_names = [t["table_name"] for t in schema["tables"]]
 
    mentioned = find_mentioned_table(question.lower(), table_names)
 
    if not mentioned:
 
        prior = get_last_context(user_id)
 
        prior_sql = prior.get("sql") if prior else None
 
        mentioned = extract_table_from_sql(prior_sql)
 
        if mentioned:
            # match back to real casing from schema
            match = next(
                (t for t in table_names if t.lower() == mentioned.lower()),
                None
            )
            mentioned = match
 
    if not mentioned:
 
        return {
            "success": True,
            "answer":
                "I'm not sure which table you mean. 🤔\n\n"
                "Try naming it directly, like \"tell me about the artists table\", "
                "or ask a question about a table first (e.g. \"show me artists\") "
                "and then say \"tell me about this table\".",
            "sql": "",
            "data": [],
            "requires_permission": False
        }
 
    table_info = next(
        (t for t in schema["tables"] if t["table_name"] == mentioned),
        None
    )
 
    session = connection_manager.get_session()
 
    sample_rows = []
 
    try:
 
        try:
            result = session.execute(
                text(f'SELECT * FROM "{mentioned}" LIMIT 3')
            )
 
            cols = result.keys()
 
            sample_rows = [
                dict(zip(cols, row))
                for row in result.fetchall()
            ]
 
        except Exception:
            sample_rows = []
 
    finally:
        session.close()
 
    description = explain_table_llm(
        table_name=mentioned,
        columns=table_info["columns"],
        sample_rows=sample_rows,
        foreign_keys=table_info["foreign_keys"],
    )
 
    columns_data = [
        {
            "column": c["name"],
            "type": c["type"],
            "nullable": "Yes" if c["nullable"] else "No"
        }
        for c in table_info["columns"]
    ]
 
    set_last_context(user_id, question, f'SELECT * FROM "{mentioned}"', sample_rows)
 
    return {
        "success": True,
        "answer": description,
        "sql": f'-- Structure of {mentioned}\nPRAGMA table_info("{mentioned}");',
        "data": columns_data,
        "rows": len(columns_data),
        "requires_permission": False
    }
 
 
# ==========================================================
# SQL Query Type
# ==========================================================
 
def get_query_type(sql: str):
 
    sql = sql.strip().upper()
 
    if sql.startswith("SELECT"):
        return "SELECT"
 
    if sql.startswith("INSERT"):
        return "INSERT"
 
    if sql.startswith("UPDATE"):
        return "UPDATE"
 
    if sql.startswith("DELETE"):
        return "DELETE"
 
    if sql.startswith("CREATE"):
        return "CREATE"
 
    if sql.startswith("ALTER"):
        return "ALTER"
 
    if sql.startswith("DROP"):
        return "DROP"
 
    return "UNKNOWN"
 
 
# ==========================================================
# CHAT ENDPOINT
# ==========================================================
 
@router.post("")
async def chat(request: dict):
 
    question = request.get("question", "").strip()
    approve = request.get("approve", False)
    sql = request.get("sql", "")
    user_id = request.get("user_id") or "default"
 
    if question == "" and sql == "":
        raise HTTPException(
            status_code=400,
            detail="Question is required."
        )
 
    # ------------------------------------------------------
    # Conversation Intent
    # ------------------------------------------------------
 
    intent = detect_intent(question)
 
    if intent == "GREETING":
        return greeting_response()
 
    if intent == "STATUS":
        return status_response()
 
    if intent == "ABOUT":
        return about_response()
 
    if intent == "HELP":
        return help_response()
 
    if intent == "THANKS":
        return thanks_response()
 
    if intent == "BYE":
        return bye_response()
 
    if intent == "LIST_DATABASES":
        return list_databases_response(question)
 
    if intent == "DESCRIBE_DATABASE":
        return describe_database_response()
 
    if intent == "EXPLAIN_TABLE":
        return explain_table_response(question, user_id)
 
    # ------------------------------------------------------
    # Database Connection Check
    # ------------------------------------------------------
 
    if not active_database.is_connected():
        raise HTTPException(
            status_code=400,
            detail="No database connected."
        )
 
    # ------------------------------------------------------
    # Read Database Schema
    # ------------------------------------------------------
 
    schema = schema_to_text()
 
    # ------------------------------------------------------
    # Generate SQL
    # ------------------------------------------------------
 
    if sql == "":
 
        prior_context = get_last_context(user_id)
 
        sql = generate_sql(
            schema=schema,
            question=question,
            context=prior_context
        )
 
    print("Generated SQL =", repr(sql))
 
    # ------------------------------------------------------
    # Validate SQL
    # ------------------------------------------------------
 
    validation = sql_validator.validate(sql)
 
    if not validation["success"]:
 
        return {
            "success": False,
            "answer": validation["answer"],
            "sql": sql,
            "data": [],
            "requires_permission": False
        }
 
    # ------------------------------------------------------
    # Detect Query Type
    # ------------------------------------------------------
 
    query_type = get_query_type(sql)
 
    # ------------------------------------------------------
    # OTP Required
    # ------------------------------------------------------
 
    dangerous_queries = [
        "INSERT",
        "UPDATE",
        "DELETE",
        "CREATE",
        "ALTER",
        "DROP"
    ]
 
    if query_type in dangerous_queries and not approve:
 
        approval_db = SessionLocal()
 
        try:
 
            approval = approval_service.create_request(
                db=approval_db,
                question=question,
                sql=sql,
                email="vinaynadig27@gmail.com"
            )
 
        finally:
            approval_db.close()
 
        set_last_context(user_id, question, sql, [])
 
        return {
            "success": False,
            "requires_permission": True,
            "request_id": approval.id,
            "answer": "OTP verification required.",
            "sql": sql,
            "query_type": query_type,
            "data": []
        }
 
    # ------------------------------------------------------
    # Execute SQL
    # ------------------------------------------------------
 
    db = connection_manager.get_session()
 
    try:
 
        result, total_rowcount = execute_multi(db, sql)
 
        # ======================================================
        # SELECT
        # ======================================================
 
        if query_type == "SELECT":
 
            rows = result.fetchall()
            columns = result.keys()
 
            data = [
                dict(zip(columns, row))
                for row in rows
            ]
 
            message = result_formatter.format_select(data)
 
            set_last_context(user_id, question, sql, data)
 
            return {
                "success": True,
                "answer": message["answer"],
                "sql": sql,
                "data": data,
                "rows": len(data),
                "requires_permission": False,
                "query_type": query_type,
            }
 
        # ======================================================
        # INSERT / UPDATE / DELETE / CREATE / ALTER / DROP
        # ======================================================
 
        db.commit()
 
        if query_type in ["UPDATE", "DELETE"] and total_rowcount == 0:
 
            answer = (
                f"⚠️ {query_type} ran successfully but matched 0 rows — "
                f"nothing was actually changed. The condition may not "
                f"match any existing record."
            )
 
        else:
 
            answer = f"{query_type} executed successfully ({total_rowcount} row(s) affected)."
 
        return {
            "success": True,
            "answer": answer,
            "sql": sql,
            "data": [],
            "affected_rows": total_rowcount,
            "requires_permission": False,
            "query_type": query_type,
        }
 
    except Exception as e:
 
        db.rollback()
 
        error = str(e).lower()
 
        if "duplicate" in error:
            answer = "❌ Duplicate value already exists."
 
        elif "no such table" in error:
            answer = "❌ Table not found."
 
        elif "no such column" in error:
            answer = "❌ Column not found."
 
        elif "syntax" in error:
            answer = "❌ Invalid SQL generated."
 
        elif "already exists" in error:
            answer = "❌ Object already exists."
 
        elif "foreign key" in error:
            answer = "❌ Foreign key constraint failed."
 
        else:
            answer = str(e)
 
        return {
            "success": False,
            "answer": answer,
            "sql": sql,
            "data": [],
            "requires_permission": False,
            "query_type": query_type,
        }
 
    finally:
 
        db.close()
 
