import unittest
from src.chat.message import Message, Role

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.m  = Message("🐡", "🥕")
        self.mu = Message.User("🐉")
        self.ms = Message.System("👿")
        self.md = Message.Developer("👾")
        self.ma = Message.Assistant("🤖")

    def test_role_strings(self):
        self.assertEqual(Role.System.value, "system")
        self.assertEqual(Role.Developer.value, "developer")
        self.assertEqual(Role.User.value, "user")
        self.assertEqual(Role.Assistant.value, "assistant")

    def test_message_creation(self):  
        self.assertEqual(self.m.role, "🐡")
        self.assertEqual(self.m.content, "🥕")

    def test_message_classmethods(self):
        self.assertEqual(self.mu.role, Role.User)
        self.assertEqual(self.ms.role, Role.System)
        self.assertEqual(self.md.role, Role.Developer)
        self.assertEqual(self.ma.role, Role.Assistant)

    def test_message__iter__(self):
        d = dict(self.m)
        self.assertEqual(self.m.role, d["role"])
        self.assertEqual(self.m.content, d["content"])

    def test_message__str__(self):
        self.assertEqual(str(self.m), "🐡: 🥕")
        self.assertEqual(str(self.mu), "user: 🐉")

if __name__ == '__main__':
    unittest.main()