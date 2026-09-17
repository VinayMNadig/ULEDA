import random


class KnowledgeEngine:

    @staticmethod
    def answer(question: str):

        q = question.lower().strip()

        # -------------------------------
        # SQL
        # -------------------------------

        if "what is sql" in q:

            return (
                "SQL (Structured Query Language) is the standard language "
                "used to communicate with relational databases.\n\n"
                "It allows you to:\n"
                "• Retrieve data\n"
                "• Insert data\n"
                "• Update records\n"
                "• Delete records\n"
                "• Create databases and tables"
            )

        # -------------------------------

        if "what is dbms" in q:

            return (
                "A DBMS (Database Management System) is software that "
                "stores, organizes, retrieves and manages data.\n\n"
                "Examples:\n"
                "• MySQL\n"
                "• PostgreSQL\n"
                "• SQLite\n"
                "• Oracle\n"
                "• SQL Server"
            )

        # -------------------------------

        if "primary key" in q:

            return (
                "A Primary Key uniquely identifies each record in a table.\n\n"
                "Features:\n"
                "• Unique\n"
                "• Cannot be NULL\n"
                "• One Primary Key per table"
            )

        # -------------------------------

        if "foreign key" in q:

            return (
                "A Foreign Key connects two tables.\n\n"
                "It references the Primary Key of another table and "
                "maintains referential integrity."
            )

        # -------------------------------

        if "normalization" in q:

            return (
                "Normalization is the process of organizing data to "
                "reduce redundancy and improve consistency.\n\n"
                "Common Normal Forms:\n"
                "• 1NF\n"
                "• 2NF\n"
                "• 3NF\n"
                "• BCNF"
            )

        # -------------------------------

        if "join" in q:

            return (
                "SQL JOIN combines rows from multiple tables.\n\n"
                "Types:\n"
                "• INNER JOIN\n"
                "• LEFT JOIN\n"
                "• RIGHT JOIN\n"
                "• FULL JOIN"
            )

        # -------------------------------

        if "acid" in q:

            return (
                "ACID Properties ensure reliable database transactions.\n\n"
                "A - Atomicity\n"
                "C - Consistency\n"
                "I - Isolation\n"
                "D - Durability"
            )

        # -------------------------------

        if "rag" in q:

            return (
                "RAG (Retrieval-Augmented Generation) combines "
                "retrieved information with an LLM to produce "
                "accurate and context-aware responses."
            )

        # -------------------------------

        if "llm" in q:

            return (
                "LLM stands for Large Language Model.\n\n"
                "Examples:\n"
                "• Llama\n"
                "• GPT\n"
                "• Gemini\n"
                "• Claude"
            )

        # -------------------------------

        if "ai" in q:

            return (
                "Artificial Intelligence (AI) enables machines to "
                "perform tasks that normally require human intelligence, "
                "such as learning, reasoning and decision-making."
            )

        # -------------------------------

        if "difference between mysql and postgresql" in q:

            return (
                "MySQL:\n"
                "• Faster for simple applications\n"
                "• Easy to use\n\n"
                "PostgreSQL:\n"
                "• More advanced features\n"
                "• Better for analytics and complex queries\n"
                "• Highly standards compliant"
            )

        # -------------------------------

        responses = [

            "I can explain SQL, DBMS, AI, RAG, normalization, joins and many other database concepts.",

            "Try asking me things like:\n"
            "• What is SQL?\n"
            "• Explain DBMS\n"
            "• What is Normalization?\n"
            "• Difference between MySQL and PostgreSQL"

        ]

        return random.choice(responses)