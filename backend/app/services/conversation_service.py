class ConversationService:

    @staticmethod
    def get_response(question: str):
        q = question.lower().strip()

        greetings = [
            "hi",
            "hello",
            "hey",
            "hii",
            "good morning",
            "good afternoon",
            "good evening",
        ]

        if q in greetings:
            return {
                "handled": True,
                "answer": (
                    "👋 Hello! Welcome to ULEDA.\n\n"
                    "I'm your Universal LLM Database Assistant.\n\n"
                    "I can help you with:\n"
                    "• 📊 Database Queries\n"
                    "• 🤖 AI SQL Generation\n"
                    "• 📈 Charts & Analytics\n"
                    "• 📄 Reports\n"
                    "• 🔐 Secure Database Operations (OTP)\n\n"
                    "How can I help you today?"
                )
            }

        if q in ["how are you", "how are you?"]:
            return {
                "handled": True,
                "answer": (
                    "😊 I'm doing great!\n\n"
                    "I'm ready to help you work with your databases."
                )
            }

        if q in [
            "who are you",
            "what are you",
            "introduce yourself",
        ]:
            return {
                "handled": True,
                "answer": (
                    "I'm ULEDA (Universal LLM Database Assistant).\n\n"
                    "I help you interact with databases using natural language.\n"
                    "You don't need to write SQL manually."
                )
            }

        if q in [
            "thanks",
            "thank you",
            "ok",
            "okay",
        ]:
            return {
                "handled": True,
                "answer": (
                    "😊 You're welcome!\n\n"
                    "Feel free to ask anything about your database."
                )
            }

        if q in [
            "bye",
            "goodbye",
            "see you",
        ]:
            return {
                "handled": True,
                "answer": (
                    "👋 Goodbye!\n\n"
                    "Have a great day.\n"
                    "See you again!"
                )
            }

        if q in [
            "help",
            "features",
            "what can you do",
        ]:
            return {
                "handled": True,
                "answer": (
                    "I can help you with:\n\n"
                    "• Query your database\n"
                    "• Generate SQL\n"
                    "• Explain SQL\n"
                    "• Charts & Analytics\n"
                    "• Reports\n"
                    "• Secure OTP Operations\n"
                    "• Database Management"
                )
            }

        return {
            "handled": False
        }


conversation_service = ConversationService()