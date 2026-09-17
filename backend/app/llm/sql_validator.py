import re

def validate_sql(sql: str):
    """
    Allow only safe SELECT queries.
    """

    sql = sql.strip()

    # Must start with SELECT
    if not sql.upper().startswith("SELECT"):
        return False

    # Block dangerous keywords
    blocked = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE",
        "CREATE",
        "REPLACE",
        "ATTACH",
        "DETACH",
        "PRAGMA"
    ]

    for word in blocked:
        if re.search(rf"\b{word}\b", sql, re.IGNORECASE):
            return False

    return True