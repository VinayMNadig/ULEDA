from enum import Enum


class Intent(Enum):

    GREETING = "GREETING"

    SMALL_TALK = "SMALL_TALK"

    HELP = "HELP"

    ABOUT = "ABOUT"

    KNOWLEDGE = "KNOWLEDGE"

    DATABASE_QUERY = "DATABASE_QUERY"

    DATABASE_MODIFICATION = "DATABASE_MODIFICATION"

    CHART = "CHART"

    REPORT = "REPORT"

    SQL_EXPLANATION = "SQL_EXPLANATION"

    GOODBYE = "GOODBYE"

    UNKNOWN = "UNKNOWN"


class IntentDetector:

    @staticmethod
    def detect(question: str):

        q = question.lower().strip()


        greetings = {

            "hi",

            "hello",

            "hey",

            "hii",

            "good morning",

            "good afternoon",

            "good evening"

        }

        if q in greetings:

            return Intent.GREETING


        if q in {

            "how are you",

            "how are you?"

        }:

            return Intent.SMALL_TALK


        if q in {

            "who are you",

            "introduce yourself",

            "what are you"

        }:

            return Intent.ABOUT


        if q in {

            "help",

            "features",

            "what can you do"

        }:

            return Intent.HELP


        if q in {

            "bye",

            "goodbye",

            "see you"

        }:

            return Intent.GOODBYE


        chart_words = [

            "chart",

            "graph",

            "plot",

            "pie",

            "bar",

            "line chart"

        ]

        if any(word in q for word in chart_words):

            return Intent.CHART


        report_words = [

            "report",

            "pdf",

            "excel"

        ]

        if any(word in q for word in report_words):

            return Intent.REPORT


        modify_words = [

            "insert",

            "update",

            "delete",

            "drop",

            "alter",

            "create"

        ]

        if any(word in q for word in modify_words):

            return Intent.DATABASE_MODIFICATION


        database_words = [

            "show",

            "list",

            "find",

            "display",

            "customers",

            "employees",

            "orders",

            "albums",

            "tracks",

            "invoice"

        ]

        if any(word in q for word in database_words):

            return Intent.DATABASE_QUERY


        knowledge_words = [

            "what is",

            "difference",

            "explain",

            "define"

        ]

        if any(word in q for word in knowledge_words):

            return Intent.KNOWLEDGE


        return Intent.UNKNOWN