from dataclasses import dataclass, field
from enum import Enum

# TODO - should I just cut this and go with strings like methods?
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
        yield ("role", self.role.value if type(self.role) is Role else self.role)
        yield ("content", self.content)

    def __str__(self):
        return f"{self.role}: {self.content}"

@dataclass
class MessageHistory:
    messages:list[Message] = field(default_factory=list)

    def append(self, message:Message):
        self.messages.append(message)
    
    def User(self, content:str):
        self.append(Message.User(content))
    
    def System(self, content:str):
        self.append(Message.System(content))

    def Developer(self, content:str):
        self.append(Message.Developer(content))

    def Assistant(self, content:str):
        self.append(Message.Assistant(content))

    def __len__(self):
        return len(self.messages)
    
    def __iter__(self):
        for message in self.messages:
            yield dict(message)
        #return iter(self.messages)
    
    def __getitem__(self, index:int):
        return self.messages[index]
    
    def __str__(self):
        return "\n".join([str(m) for m in self.messages])