from app.sql.executor import execute_sql

query = "SELECT * FROM employees"

result = execute_sql(query)

print(result)