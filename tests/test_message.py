import pytest
from src.chat.message import Message, Role

@pytest.fixture
def messages():
    return {
        "basic": Message("🐡", "🥕"),
        "user": Message.User("🐉"),
        "system": Message.System("👿"),
        "developer": Message.Developer("👾"),
        "assistant": Message.Assistant("🤖")
    }

def test_role_strings():
    assert Role.System.value == "system"
    assert Role.Developer.value == "developer"
    assert Role.User.value == "user"
    assert Role.Assistant.value == "assistant"

def test_message_creation(messages):  
    assert messages["basic"].role == "🐡"
    assert messages["basic"].content == "🥕"

def test_message_classmethods(messages):
    assert messages["user"].role == Role.User
    assert messages["system"].role == Role.System
    assert messages["developer"].role == Role.Developer
    assert messages["assistant"].role == Role.Assistant

def test_message__iter__(messages):
    d = dict(messages["basic"])
    assert messages["basic"].role == d["role"]
    assert messages["basic"].content == d["content"]

def test_message__str__(messages):
    assert str(messages["basic"]) == "🐡: 🥕"
    assert str(messages["user"]) == "user: 🐉"