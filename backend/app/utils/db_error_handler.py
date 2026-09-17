def format_database_error(error: Exception):

    message = str(error).lower()

    # -----------------------------
    # Table already exists
    # -----------------------------
    if "already exists" in message:

        return {
            "success": False,
            "answer": "❌ This object already exists in the database.",
            "reason": str(error)
        }

    # -----------------------------
    # Duplicate column
    # -----------------------------
    if "duplicate column name" in message:

        return {
            "success": False,
            "answer": "❌ That column already exists.",
            "reason": str(error)
        }

    # -----------------------------
    # No such table
    # -----------------------------
    if "no such table" in message:

        return {
            "success": False,
            "answer": "❌ Table not found.",
            "reason": str(error)
        }

    # -----------------------------
    # No such column
    # -----------------------------
    if "no such column" in message:

        return {
            "success": False,
            "answer": "❌ Column not found.",
            "reason": str(error)
        }

    # -----------------------------
    # UNIQUE constraint
    # -----------------------------
    if "unique constraint failed" in message:

        return {
            "success": False,
            "answer": "❌ Duplicate value detected.",
            "reason": str(error)
        }

    # -----------------------------
    # FOREIGN KEY
    # -----------------------------
    if "foreign key constraint failed" in message:

        return {
            "success": False,
            "answer": "❌ This record is linked to other data.",
            "reason": str(error)
        }

    # -----------------------------
    # NOT NULL
    # -----------------------------
    if "not null constraint failed" in message:

        return {
            "success": False,
            "answer": "❌ Required data is missing.",
            "reason": str(error)
        }

    # -----------------------------
    # SQL Syntax
    # -----------------------------
    if "syntax error" in message:

        return {
            "success": False,
            "answer": "❌ Invalid SQL generated.",
            "reason": str(error)
        }

    # -----------------------------
    # Default
    # -----------------------------
    return {
        "success": False,
        "answer": "❌ Database operation failed.",
        "reason": str(error)
    }