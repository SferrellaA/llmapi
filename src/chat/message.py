
from dataclasses import dataclass, asdict
from enum import Enum

class Role(Enum):
    System = "system"
    User = "user"
    Assistant = "assistant"

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
    def Assistant(cls, content:str):
        return cls(Role.Assistant, content)

    def toDict(self)->dict[str,str]:
        return {
            "role": self.role if type(self.role) is str else self.role.value,
            "content": self.content,
        }

    def __str__(self):
        return str(self.toDict())