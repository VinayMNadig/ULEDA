from app.llm.llm import llm
from app.llm.prompt import SYSTEM_PROMPT


# ==========================================
# Generate SQL
# ==========================================

def generate_sql(
    schema: str,
    question: str,
    context: dict = None,
):

    context_block = ""

    if context:

        context_block = f"""
Previous Question: {context.get('question')}
Previous SQL: {context.get('sql')}
Previous Result (sample rows): {context.get('data')}

If the current question uses words like "this", "that", "these", "it", or
otherwise refers back to something without naming it explicitly, resolve
that reference using the specific values (e.g. IDs) shown in the previous
result above. Do not guess a new, unrelated condition.
"""

    prompt = f"""
{SYSTEM_PROMPT}

You are an expert SQL Engineer.

Generate ONLY SQL.

Rules:

1. Return ONLY SQL.
2. Do NOT explain.
3. No markdown.
4. No ```sql blocks.
5. Use only the given schema.
6. Never create imaginary tables.
7. Use proper joins.
8. For DELETE/UPDATE use WHERE.
9. Prefer SELECT unless user explicitly requests modification.
10. If a request needs different values for different conditions
    (e.g. "set X to 1000 where A, and 2000 where B"), prefer a
    single UPDATE using CASE WHEN instead of multiple statements.
{context_block}
Database Schema:

{schema}

Question:

{question}

SQL:
"""

    response = llm.invoke(prompt)

    sql = response.content.strip()

    # Remove markdown if model returns it

    sql = sql.replace("```sql", "")

    sql = sql.replace("```", "")

    sql = sql.strip()

    return sql