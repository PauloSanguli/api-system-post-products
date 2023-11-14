from abc import abstractmethod
from abc import ABC
from typing import Type



class IvalidatorPassword(ABC):

    @abstractmethod
    def validate(password: Type[str]) -> dict:
        raise NotImplementedError("Method validate required!")


class IvalidatorEmail(ABC):
    
    @abstractmethod
    def validate(email: Type[str]) -> dict:
        raise NotImplementedError("Method validate required!")


class IvalidatorPhone(ABC):
    
    @abstractmethod
    def validate(phone_number: Type[str]) -> dict:
        raise NotImplementedError("Method validate required!")