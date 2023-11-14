from dataclasses import (
    dataclass
)





RESPONSE_ERROR = {
    "msg":"invalid name",
    "status":False
}

RESPONSE_TRUE = {
    "msg":"name valid",
    "status":True
}

@dataclass(frozen=True)
class validatorName():
    
   def validate(name: str) -> dict:
        name = name.strip()
        if name == "":
            return RESPONSE_ERROR
        
        return RESPONSE_TRUE

