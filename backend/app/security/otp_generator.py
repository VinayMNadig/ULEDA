import random


class OTPGenerator:

    @staticmethod
    def generate():

        otp = ""

        for _ in range(6):

            otp += str(
                random.randint(0, 9)
            )

        return otp


otp_generator = OTPGenerator()