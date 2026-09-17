import re


class ConversationEngine:

    # ==========================================================
    # MAIN ENTRY
    # ==========================================================

    @staticmethod
    def detect(question: str):

        q = question.lower().strip()

        # ------------------------------------
        # Greeting
        # ------------------------------------

        if ConversationEngine.is_greeting(q):
            return ConversationEngine.greeting()

        # ------------------------------------
        # Introduction
        # ------------------------------------

        if ConversationEngine.is_about(q):
            return ConversationEngine.about()

        # ------------------------------------
        # How are you
        # ------------------------------------

        if ConversationEngine.is_how_are_you(q):
            return ConversationEngine.how_are_you()

        # ------------------------------------
        # Thank You
        # ------------------------------------

        if ConversationEngine.is_thanks(q):
            return ConversationEngine.thanks()

        # ------------------------------------
        # Help
        # ------------------------------------

        if ConversationEngine.is_help(q):
            return ConversationEngine.help()

        # ------------------------------------
        # Joke
        # ------------------------------------

        if ConversationEngine.is_joke(q):
            return ConversationEngine.joke()

        # ------------------------------------
        # SQL Knowledge
        # ------------------------------------

        if ConversationEngine.is_sql_theory(q):
            return ConversationEngine.sql_theory()

        # ------------------------------------
        # Normalization
        # ------------------------------------

        if ConversationEngine.is_normalization(q):
            return ConversationEngine.normalization()

        # ------------------------------------
        # Chart Intent
        # ------------------------------------

        if ConversationEngine.is_chart_request(q):
            return {
                "type": "CHART"
            }

        # ------------------------------------
        # Report Intent
        # ------------------------------------

        if ConversationEngine.is_report_request(q):
            return {
                "type": "REPORT"
            }

        # ------------------------------------
        # Database Query
        # ------------------------------------

        if ConversationEngine.is_database_question(q):
            return {
                "type": "DATABASE"
            }

        # ------------------------------------
        # Default
        # ------------------------------------

        return ConversationEngine.unknown()

    # ==========================================================
    # GREETING
    # ==========================================================

    @staticmethod
    def is_greeting(q):

        words = [

            "hi",
            "hii",
            "hello",
            "hey",
            "hola",
            "good morning",
            "good afternoon",
            "good evening"

        ]

        return q in words

    @staticmethod
    def greeting():

        return {

            "type": "CHAT",

            "success": True,

            "answer":
                "👋 Hello! Welcome to **ULEDA**.\n\n"
                "I'm your **Universal LLM Database Assistant**.\n\n"
                "I can help you with:\n\n"
                "📊 Database Analysis\n"
                "🔍 Search Records\n"
                "📈 Charts & Analytics\n"
                "📝 SQL Generation\n"
                "📄 Reports\n"
                "🔐 Secure Database Operations\n\n"
                "How can I help you today?"

        }

    # ==========================================================
    # ABOUT
    # ==========================================================

    @staticmethod
    def is_about(q):

        phrases = [

            "who are you",

            "what are you",

            "introduce yourself",

            "about you"

        ]

        return q in phrases

    @staticmethod
    def about():

        return {

            "type": "CHAT",

            "success": True,

            "answer":
                "I'm **ULEDA (Universal LLM Database Assistant)**.\n\n"
                "I help users interact with databases using natural language.\n\n"
                "Instead of writing SQL manually, you can simply ask questions like:\n\n"
                "• Show all employees\n"
                "• Create sales chart\n"
                "• Delete customer 10\n"
                "• Explain SQL\n\n"
                "I'll generate SQL, analyze data, create charts and securely execute operations."

        }

    # ==========================================================
    # HOW ARE YOU
    # ==========================================================

    @staticmethod
    def is_how_are_you(q):

        return q in [

            "how are you",

            "how are you?"

        ]

    @staticmethod
    def how_are_you():

        return {

            "type": "CHAT",

            "success": True,

            "answer":
                "😊 I'm doing great!\n\n"
                "Ready to help you with your databases."

        }

    # ==========================================================
    # THANK YOU
    # ==========================================================

    @staticmethod
    def is_thanks(q):

        return q in [

            "thanks",

            "thank you",

            "ok",

            "okay"

        ]

    @staticmethod
    def thanks():

        return {

            "type": "CHAT",

            "success": True,

            "answer":
                "You're welcome! 😊\n\n"
                "Feel free to ask me anything about your database."

        }

    # ==========================================================
    # HELP
    # ==========================================================

    @staticmethod
    def is_help(q):

        return q in [

            "help",

            "features",

            "what can you do"

        ]

    @staticmethod
    def help():

        return {

            "type": "CHAT",

            "success": True,

            "answer":
                "I can help you with:\n\n"
                "📊 Query databases\n"
                "🤖 Generate SQL\n"
                "📈 Charts\n"
                "📄 Reports\n"
                "🔍 Search Records\n"
                "📚 Explain SQL\n"
                "🔐 OTP Protected Operations"

        }

    # ==========================================================
    # JOKE
    # ==========================================================

    @staticmethod
    def is_joke(q):

        return "joke" in q

    @staticmethod
    def joke():

        return {

            "type": "CHAT",

            "success": True,

            "answer":
                "😂 Why did the database administrator break up with the SQL table?\n\n"
                "Because there was no primary key to the relationship!"

        }

    # ==========================================================
    # SQL THEORY
    # ==========================================================

    @staticmethod
    def is_sql_theory(q):

        return (

            "what is sql" in q or

            "explain sql" in q

        )

    @staticmethod
    def sql_theory():

        return {

            "type": "CHAT",

            "success": True,

            "answer":
                "SQL (Structured Query Language) is the standard language used to communicate with relational databases.\n\n"
                "It allows you to CREATE, READ, UPDATE and DELETE data."

        }

    # ==========================================================
    # NORMALIZATION
    # ==========================================================

    @staticmethod
    def is_normalization(q):

        return "normalization" in q

    @staticmethod
    def normalization():

        return {

            "type": "CHAT",

            "success": True,

            "answer":
                "Normalization is the process of organizing database tables to reduce redundancy and improve data integrity.\n\n"
                "Common normal forms:\n"
                "• 1NF\n"
                "• 2NF\n"
                "• 3NF\n"
                "• BCNF"

        }

    # ==========================================================
    # CHART
    # ==========================================================

    @staticmethod
    def is_chart_request(q):

        words = [

            "chart",

            "graph",

            "plot",

            "visualize"

        ]

        return any(word in q for word in words)

    # ==========================================================
    # REPORT
    # ==========================================================

    @staticmethod
    def is_report_request(q):

        words = [

            "report",

            "summary",

            "analysis"

        ]

        return any(word in q for word in words)

    # ==========================================================
    # DATABASE
    # ==========================================================

    @staticmethod
    def is_database_question(q):

        keywords = [

            "show",

            "list",

            "find",

            "select",

            "insert",

            "update",

            "delete",

            "create",

            "drop",

            "alter",

            "employee",

            "customer",

            "invoice",

            "artist",

            "album",

            "track",

            "sales"

        ]

        return any(word in q for word in keywords)

    # ==========================================================
    # UNKNOWN
    # ==========================================================

    @staticmethod
    def unknown():

        return {

            "type": "CHAT",

            "success": True,

            "answer":
                "I'm not completely sure what you mean.\n\n"
                "You can ask me about:\n\n"
                "• Databases\n"
                "• SQL\n"
                "• Charts\n"
                "• Reports\n"
                "• Database Analysis\n"
                "• General database concepts"

        }