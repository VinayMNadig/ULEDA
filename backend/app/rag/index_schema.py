from app.rag.schema_reader import schema_to_text
from app.rag.vector_store import collection

print("Reading Database Schema...")

text = schema_to_text()

print(text)

# Delete previous document if it exists
try:
    collection.delete(ids=["schema"])
except Exception:
    pass

collection.add(
    ids=["schema"],
    documents=[text]
)

print("Schema Indexed Successfully!")