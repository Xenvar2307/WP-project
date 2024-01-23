import unittest


class TestActionPanel(unittest.TestCase):
    # test if notify gets correct classes
    # if image is always loaded and correct
    def test_something(self):
        self.assertEqual(1, 1)


class TestCharacter(unittest.TestCase):
    # test play animation:
    # number of frames played, return to idle or staying dead

    # automatic updating healthbar, assigning and removing healthbars
    # do it together with take damage and heal methods
    # check if reset is the same as new character with base state

    def test_nothing(self):
        self.assertAlmostEqual(1, 1)


class TestDamageTexts(unittest.TestCase):
    # check if damage text dies after said time
    def test_something(self):
        self.assertAlmostEqual(1, 1)


class TestHealthBar(unittest.TestCase):
    # check raw notify
    def test_something(self):
        self.assertAlmostEqual(1, 1)


class TestHealthBar(unittest.TestCase):
    # check raw notify
    def test_something(self):
        self.assertAlmostEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
