from ..validators import PATTERN_EMAIL
import re
from typing import Type
from dataclasses import (
    dataclass
)


@dataclass(frozen=True)
class validatorEmail():

    def validate(email: Type[str]) -> dict:
        """validate email"""

        email = email.strip()

        result_search_bool = re.search(PATTERN_EMAIL, email)

        if not result_search_bool:
            return {
                "msg":"the email is not valid",
                "status":False
            }

        return {
            "msg":"the email is valid",
            "status":True
        }
