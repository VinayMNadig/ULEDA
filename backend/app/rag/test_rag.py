from app.rag.retriever import retrieve

question = "Which table contains customer information?"

result = retrieve(question)

print(result)