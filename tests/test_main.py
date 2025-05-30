import unittest
from app.main import say_hello

class TestHello(unittest.TestCase):
    def test_default(self):
        self.assertEqual(say_hello(), "Hello, World!")

    def test_custom_name(self):
        self.assertEqual(say_hello("Alice"), "Hello, Alice!")

if __name__ == "__main__":
    unittest.main()
