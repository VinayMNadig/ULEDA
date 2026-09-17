"""
=========================================================
ULEDA Conversation Engine
Universal LLM Database Assistant
=========================================================
Handles normal conversations.

If the message is NOT database related,
it returns a conversational response.

If the message IS database related,
it returns None so the SQL engine can continue.
=========================================================
"""

import random


class ConversationEngine:

    def __init__(self):

        self.greetings = [
            "hi",
            "hii",
            "hello",
            "hey",
            "hola",
            "good morning",
            "good afternoon",
            "good evening",
            "good night",
        ]

        self.help_words = [
            "help",
            "features",
            "what can you do",
            "commands",
            "options",
        ]

        self.database_keywords = [

            "table",
            "database",
            "employee",
            "employees",
            "customer",
            "customers",
            "artist",
            "album",
            "track",
            "invoice",
            "genre",
            "playlist",

            "show",
            "display",
            "list",
            "find",
            "search",
            "count",
            "select",

            "insert",
            "update",
            "delete",
            "drop",
            "alter",
            "create",

            "chart",
            "graph",
            "analytics",
            "report",

            "sql",

        ]

    # ====================================================
    # Main
    # ====================================================

    def process(self, question: str):

        q = question.lower().strip()

        # -------------------------------
        # Greeting
        # -------------------------------

        if q in self.greetings:

            return {
                "success": True,
                "answer":
                    "👋 Hello! Welcome to **ULEDA**.\n\n"
                    "I'm your **Universal LLM Database Assistant**.\n\n"
                    "I can help you with:\n\n"
                    "📊 Database Queries\n"
                    "🤖 AI SQL Generation\n"
                    "📈 Charts & Analytics\n"
                    "📄 Reports\n"
                    "🔍 Search Records\n"
                    "🔐 Secure Database Operations (OTP)\n\n"
                    "How can I help you today?",
                "sql": "",
                "data": [],
                "requires_permission": False,
            }

        # -------------------------------
        # How are you
        # -------------------------------

        if q in [
            "how are you",
            "how are you?",
            "how are u",
        ]:

            responses = [

                "😊 I'm doing great! Ready to help you work with your databases.",

                "I'm doing well! What database task would you like to perform today?",

                "Everything is running smoothly 🚀 How can I assist you today?",

            ]

            return {
                "success": True,
                "answer": random.choice(responses),
                "sql": "",
                "data": [],
                "requires_permission": False,
            }

        # -------------------------------
        # Who are you
        # -------------------------------

        if q in [

            "who are you",

            "what are you",

            "introduce yourself",

            "about you",

        ]:

            return {

                "success": True,

                "answer":
                    "🤖 I'm **ULEDA (Universal LLM Database Assistant)**.\n\n"
                    "I allow you to interact with databases using natural language.\n\n"
                    "Instead of writing SQL manually, you can simply ask questions.\n\n"
                    "I can:\n"
                    "• Retrieve data\n"
                    "• Generate SQL\n"
                    "• Explain SQL\n"
                    "• Create reports\n"
                    "• Generate charts\n"
                    "• Securely execute INSERT/UPDATE/DELETE using OTP.",

                "sql": "",

                "data": [],

                "requires_permission": False,

            }

        # -------------------------------
        # Thank you
        # -------------------------------

        if q in [

            "thanks",

            "thank you",

            "ok",

            "okay",

            "thanks buddy",

            "thanks uleda",

        ]:

            return {

                "success": True,

                "answer":
                    "😊 You're welcome!\n\n"
                    "I'm always here whenever you need help with your database.",

                "sql": "",

                "data": [],

                "requires_permission": False,

            }

        # -------------------------------
        # Help
        # -------------------------------

        if q in self.help_words:

            return {

                "success": True,

                "answer":
                    "Here are some things you can ask me:\n\n"

                    "📊 Show all employees\n"

                    "📈 Create sales chart\n"

                    "📝 Generate SQL\n"

                    "📄 Generate reports\n"

                    "🔍 Search records\n"

                    "📚 Explain SQL queries\n"

                    "🔐 Insert / Update / Delete with OTP approval\n"

                    "😂 Tell a joke\n"

                    "❓ Ask SQL concepts",

                "sql": "",

                "data": [],

                "requires_permission": False,

            }

        # -------------------------------
        # Joke
        # -------------------------------

        if "joke" in q:

            jokes = [

                "😂 Why did the database administrator break up with the SQL table?\nBecause there was no PRIMARY KEY to the relationship!",

                "😂 I told my database a joke...\nIt couldn't relate.",

                "😂 SQL walks into a bar, walks up to two tables and asks...\nCan I JOIN you?",

            ]

            return {

                "success": True,

                "answer": random.choice(jokes),

                "sql": "",

                "data": [],

                "requires_permission": False,

            }

        # -------------------------------
        # SQL Meaning
        # -------------------------------

        if q in [

            "what is sql",

            "define sql",

            "sql",

        ]:

            return {

                "success": True,

                "answer":
                    "SQL (Structured Query Language) is the standard language used to communicate with relational databases.\n\n"
                    "It is used to:\n"
                    "• Retrieve data\n"
                    "• Insert records\n"
                    "• Update records\n"
                    "• Delete records\n"
                    "• Create tables\n"
                    "• Manage databases",

                "sql": "",

                "data": [],

                "requires_permission": False,

            }

        # -------------------------------
        # Normalization
        # -------------------------------

        if "normalization" in q:

            return {

                "success": True,

                "answer":
                    "Database Normalization is the process of organizing data to reduce redundancy and improve consistency.\n\n"
                    "Common Normal Forms:\n"
                    "• 1NF\n"
                    "• 2NF\n"
                    "• 3NF\n"
                    "• BCNF",

                "sql": "",

                "data": [],

                "requires_permission": False,

            }

        # -------------------------------
        # Bye
        # -------------------------------

        if q in [

            "bye",

            "goodbye",

            "see you",

            "bye uleda",

        ]:

            return {

                "success": True,

                "answer":
                    "👋 Goodbye!\n\n"
                    "Have a wonderful day.\n"
                    "I'll be here whenever you need database assistance.",

                "sql": "",

                "data": [],

                "requires_permission": False,

            }

        # -------------------------------
        # Detect Database Question
        # -------------------------------

        for keyword in self.database_keywords:

            if keyword in q:
                return None

        # -------------------------------
        # Unknown Conversation
        # -------------------------------

        return {

            "success": True,

            "answer":
                "🙂 That's interesting.\n\n"
                "I'm designed mainly to help with databases, SQL, analytics, reports, and data visualization.\n\n"
                "Feel free to ask me anything related to databases!",

            "sql": "",

            "data": [],

            "requires_permission": False,

        }


conversation_engine = ConversationEngine()