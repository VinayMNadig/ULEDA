from sqlalchemy import text


def split_sql_statements(sql: str):
    """
    Splits a possibly multi-statement SQL string on ';' into
    individual statements, dropping empty fragments.
    """

    statements = [s.strip() for s in sql.split(";")]

    return [s for s in statements if s]


def execute_multi(session, sql: str):
    """
    Executes one or more semicolon-separated SQL statements
    against the given session, one at a time (SQLite/most
    DBAPI drivers reject multiple statements in a single
    execute() call).

    Returns:
        last_result   -> the Result object of the final statement
                          (used for SELECT)
        total_rowcount -> sum of affected rows across all statements
                          (used for INSERT/UPDATE/DELETE)
    """

    statements = split_sql_statements(sql)

    if not statements:
        raise ValueError("No SQL statement to execute.")

    last_result = None
    total_rowcount = 0

    for statement in statements:

        last_result = session.execute(text(statement))

        if last_result.rowcount and last_result.rowcount > 0:
            total_rowcount += last_result.rowcount

    return last_result, total_rowcount
