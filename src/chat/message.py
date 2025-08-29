
from dataclasses import dataclass, asdict
from enum import Enum

class Role(Enum):
    System = "system"
    Developer = "developer"
    User = "user"
    Assistant = "assistant"

    def __str__(self):
        return self.value

@dataclass
class Message:
    role:Role|str
    content:str

    @classmethod
    def User(cls, content:str):
        return cls(Role.User, content)
    
    @classmethod
    def System(cls, content:str):
        return cls(Role.System, content)
    
    @classmethod
    def Developer(cls, content:str):
        return cls(Role.Developer, content)

    @classmethod
    def Assistant(cls, content:str):
        return cls(Role.Assistant, content)

    def __iter__(self):
        return iter([
            ("role", self.role if type(self.role) is str else self.role.value),
            ("content", self.content),
        ])

    def __str__(self):
        return f"{self.role}: {self.content}"