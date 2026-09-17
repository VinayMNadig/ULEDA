class ResultFormatter:

    @staticmethod
    def format_select(data):

        rows = len(data)

        if rows == 0:
            return {
                "answer":
                "No matching records were found.\n\n"
                "Try another search or use different keywords."
            }

        if rows == 1:
            return {
                "answer":
                "Found 1 matching record."
            }

        return {
            "answer":
            f"Found {rows} matching records."
        }

    @staticmethod
    def format_update(query_type, affected_rows):

        if affected_rows == 0:
            return {
                "answer":
                f"{query_type} completed.\n"
                "No rows were affected."
            }

        return {
            "answer":
            f"{query_type} completed successfully.\n"
            f"{affected_rows} row(s) affected."
        }


result_formatter = ResultFormatter()