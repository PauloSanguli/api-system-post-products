from typing import Type
from dataclasses import dataclass



@dataclass(frozen=True)
class validatorPassword():

    def validate(password: Type[str]) -> bool:
        """validate password"""

        password = password.strip()
        password_lenght = len(password)

        LENGHT_PASSWORD_MIN = 8
        LENGHT_PASSWORD_MAX = 40

        if password == "":
            return {
                "msg":"the password is not valid",
                "status": False
            }
        
        if password_lenght < LENGHT_PASSWORD_MIN:
            return {
                "msg":"the password is not valid",
                "status": False
            }

        if password_lenght > LENGHT_PASSWORD_MAX:
            return {
                "msg":"the password is not valid",
                "status": False
            }

        return {
                "msg":"the password is valid",
                "status": True
            }
