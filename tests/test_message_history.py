import pytest
from src.chat.message import Message, MessageHistory

def test_history__len__():
    h = MessageHistory()
    assert len(h) == 0
    h.User("🐡")
    assert len(h) == 1

def test_history__iter__():
    h = MessageHistory()
    assert list(h) == []
    h.User("🐡")
    h.User("🥕")
    i = iter(h)
    first = next(i)
    last = next(i)
    assert first == dict(Message.User("🐡"))
    assert last == dict(Message.User("🥕"))

def test_history__getitem__():
    h = MessageHistory()
    h.User("🐡")
    h.User("🥕")
    assert h[0] == Message.User("🐡")
    assert h[1] == Message.User("🥕")

def test_history__str__():
    h = MessageHistory()
    h.System("🐡")
    assert str(h) == "system: 🐡"
    h.User("🥕")
    assert str(h) == "system: 🐡\nuser: 🥕"

def test_history_append():
    h = MessageHistory()
    m = Message("🐡", "🥕")
    h.append(m)
    assert h[0] == m

def test_history_roles():
    h = MessageHistory()
    h.User("🐉"),
    h.System("👿"),
    h.Developer("👾"),
    h.Assistant("🤖")
    assert h[0].role.value == "user"
    assert h[1].role.value == "system"
    assert h[2].role.value == "developer"
    assert h[3].role.value == "assistant"