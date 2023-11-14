from dataclasses import(
    dataclass
) 

RESPONSE_FALSE = {
    "msg":"cell phone invalid",
    "status":False
}

RESPONSE_TRUE = {
    "msg":"cell phone valid",
    "status":True
}

@dataclass(frozen=True)
class validatorPhoneNumber():
    def validate(phone: str) -> dict:
        global RESPONSE_TRUE
        global RESPONSE_FALSE

        phone = phone.strip()
        if phone == "":
            return RESPONSE_FALSE
        condition = phone[0] != '9' or len(phone) != 9
        if condition:
            return RESPONSE_FALSE.copy()
        else:
            return RESPONSE_TRUE.copy()

