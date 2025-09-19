import json

class argument:
    name:str
    kind:str|type
    desc:str|None
    required:bool

    def marshall(self)->tuple[str, dict, bool]:
        """a dict of the parameter and a bool of if it's required"""
        d = {"type": self.kind if type(self.kind) is str else str(self.kind)}
        # TODO - is there an official enum of tool types?
        if self.desc:
            d["description"] = self.desc
        return (self.name, d, self.required)

class tool:
    name:str
    kind:str|type
    desc:str|None
    args:list[argument]|None

    @classmethod
    def fromCallable(cls, call:callable):
        raise NotImplementedError

    def toDict(self)->dict:
        d = {
            "type": "function",
            "name": self.name,
        }
        if self.desc:
            d["description"] = self.desc
        if self.args:
            properties = {}
            required = []
            for arg in self.args:
                n, d, r = arg.marshall()
                properties[n] = d
                if r:
                    required.append(n)
            d["parameters"] = {
                "type": self.kind if type(self.kind) is str else str(self.kind),
                "properties": properties,
                "required": required,
                "additionalProperties": False
            }
        return d
    
    def toJson(self)->str:
        return json.loads(self.toDict())