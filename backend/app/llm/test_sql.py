from app.rag.schema_reader import schema_to_text
from app.llm.sql_generator import generate_sql

schema = schema_to_text()

question = "Show all employees"

sql = generate_sql(schema, question)

print("\nGenerated SQL:\n")
print(sql)