import pytest
from src.chat.message import Message, Role

def test_role_strings():
    assert Role.System.value == "system"
    assert Role.Developer.value == "developer"
    assert Role.User.value == "user"
    assert Role.Assistant.value == "assistant"

def test_message_creation():  
    m = Message("🐡", "🥕")
    assert m.role == "🐡"
    assert m.content == "🥕"

def test_message_classmethods():
    assert Message.User("🐉").role == Role.User
    assert Message.System("👿").role == Role.System
    assert Message.Developer("👾").role == Role.Developer
    assert Message.Assistant("🤖").role == Role.Assistant

def test_message__iter__():
    m = Message("🐡", "🥕")
    d = dict(m)
    assert m.role == d["role"]
    assert m.content == d["content"]

def test_message__str__():
    assert str(Message("🐡", "🥕")) == "🐡: 🥕"
    assert str(Message.User("🐉")) == "user: 🐉"
