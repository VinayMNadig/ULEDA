
from app.rag.schema_reader import schema_to_text
from app.llm.sql_generator import generate_sql
from app.llm.sql_validator import validate_sql
from app.services.execute_sql import execute_sql

schema = schema_to_text()

question = "Show all employees"

sql = generate_sql(schema, question)

print("\nGenerated SQL:")
print(sql)

if validate_sql(sql):
    result = execute_sql(sql)

    print("\nDatabase Result:")
    print(result)

else:
    print("\nUnsafe SQL Blocked!")