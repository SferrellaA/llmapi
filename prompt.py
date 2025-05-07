
from dataclasses import dataclass, asdict
from enum import Enum

class Role(Enum):
    System = "system"
    User = "user"
    Assistant = "assistant"

@dataclass
class Message:
    role:Role
    content:str

    @classmethod
    def User(cls, content:str):
        return cls(
            role=Role.User, 
            content=content
        )
    
    @classmethod
    def System(cls, content:str):
        return cls(
            role=Role.System, 
            content=content
        )

    @classmethod
    def Assistant(cls, content:str):
        return cls(
            role=Role.Assistant, 
            content=content
        )

    def __str__(self):
        return str({
            "role": self.role.value, 
            "content": self.content,
        })