from app.llm.answer_generator import generate_answer

question = "Show all employees"

sql = "SELECT * FROM employees"

results = [
    {
        "employee_id": 1,
        "name": "Rahul",
        "department": "HR",
        "salary": 60000
    },
    {
        "employee_id": 2,
        "name": "Priya",
        "department": "Sales",
        "salary": 55000
    }
]

answer = generate_answer(question, sql, results)

print(answer)