from user import User
import unittest
class TestUser(unittest.TestCase):
    def setUp(self):
        self.myUser= User("Aizo", "12345678")