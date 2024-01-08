import unittest
from scr.main import add_numbers


class TestMain(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
