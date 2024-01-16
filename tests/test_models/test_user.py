import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_inheritance(self):
        """Test if User is a subclass of BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """Test if User has the correct attributes."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_attribute_types(self):
        """Test if User attributes are of the correct type."""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_attribute_initialization(self):
        """Test if User attributes are correctly initialized."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
