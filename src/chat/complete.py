from src.client.client import Client
from src.chat.message import Message, MessageHistory

# TODO - tools
# TODO - a way for logging token usage, response id, finish_reason
# TODO - multiple completion options?
def complete(
    client:Client, 
    messages:list[Message]|list[dict]|MessageHistory, 
    model:str=None
)->Message:
    if not model:
        model = client.model
    if not model:
        raise ValueError("No model provided by client.model or model argument")

    if type(messages) is list:
        if len(messages) == 0:
            return None # TODO - is this actually to spec?
        if type(messages[0]) is Message:
            messages = [dict(m) for m in messages]
    elif type(messages) is MessageHistory:
        messages = list(messages)      

    completion = client.request(
        endpoint="/chat/completions",
        method="POST",
        payload={
            "model": model,
            "messages": messages
        }
    )
    try:
        completion = completion["choices"][0]["message"]
    except:
        # TODO - this part
        pass
    if completion["refusal"] is not None:
        raise Exception(f"Refusal '{c['refusal']}'")
    # TODO - annotations/url_citation
    return Message(completion["role"], completion["content"])
