import unittest


class TestClass(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, 1)


class TestSomethingDifferent(unittest.TestCase):
    def test_nothing(self):
        self.assertAlmostEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
