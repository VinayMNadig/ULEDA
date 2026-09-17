class ResponseBuilder:

    @staticmethod
    def success(answer, sql="", data=None, **kwargs):

        if data is None:
            data = []

        response = {

            "success": True,

            "answer": answer,

            "sql": sql,

            "data": data,

            "requires_permission": False

        }

        response.update(kwargs)

        return response

    @staticmethod
    def error(message):

        return {

            "success": False,

            "answer": message,

            "sql": "",

            "data": [],

            "requires_permission": False

        }

    @staticmethod
    def otp(sql, request_id, query_type):

        return {

            "success": False,

            "answer": "OTP verification required.",

            "sql": sql,

            "data": [],

            "requires_permission": True,

            "request_id": request_id,

            "query_type": query_type

        }