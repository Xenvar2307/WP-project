import unittest
import pygame
from main import *


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


class TestDamageTexts_with_factory(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        self.font = pygame.font.SysFont("Caslon Antique", 30)
        self.sprite_group = pygame.sprite.Group()
        self.DamageTextFactory = DamageTextFactory_normal(0, 0, self.font)
        self.sprite_group.add(self.DamageTextFactory.factory(1, white))
        self.sprite_group.add(self.DamageTextFactory.factory(12, white))

    def tearDown(self):
        pass

    # check if damage text dies after said time
    def test_life_duration(self):
        self.assertEqual(len(self.sprite_group), 2)
        for i in range(DamageTextLife_normal - 1):
            self.sprite_group.update()

        self.assertEqual(len(self.sprite_group), 2)
        self.sprite_group.update()
        self.assertEqual(len(self.sprite_group), 0)
        self.sprite_group.add(self.DamageTextFactory.factory(1, white))
        self.assertEqual(len(self.sprite_group), 1)


class TestDamageTexts_withoutfactory(unittest.TestCase):
    def setUp(self) -> None:
        pygame.init()
        self.font = pygame.font.SysFont("Caslon Antique", 30)
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(BasicDamageText(0, 0, "1", self.font, white, 6))
        self.sprite_group.add(BasicDamageText(0, 0, "1", self.font, white, 7))

    def tearDown(self):
        pass

    # check if damage text dies after said time
    def test_life_duration(self):
        self.assertEqual(len(self.sprite_group), 2)
        for i in range(6):
            self.sprite_group.update()

        self.assertEqual(len(self.sprite_group), 1)
        self.sprite_group.update()
        self.assertEqual(len(self.sprite_group), 0)
        self.sprite_group.add(BasicDamageText(0, 0, "1", self.font, white, 0))
        self.assertEqual(len(self.sprite_group), 1)


class TestHealthBar(unittest.TestCase):
    # check raw notify
    def setUp(self):
        pygame.init()
        self.test_character1 = Basic_Character(
            "test name 1", 15, 15, 3, 3, 3, None, None, None, 0, 0, None
        )
        self.test_character2 = Basic_Character(
            "test name 2", 20, 20, 3, 3, 3, None, None, None, 0, 0, None
        )
        self.font = pygame.font.SysFont("Caslon Antique", 30)
        self.HealthBar_normal = Health_bar_normal(self.test_character1, self.font)
        self.HealthBar_action_panel = Health_bar_action_panel(self.font)
        self.HealthBar_action_panel

    def test_normalHB_auto_notify(self):
        # same at setup?
        self.assertEqual(
            self.test_character1.current_hp, self.HealthBar_normal.current_hp
        )
        # same after getting hurt normally
        self.test_character1.take_damage(1)
        self.assertEqual(
            self.test_character1.current_hp, self.HealthBar_normal.current_hp
        )
        self.test_character1.take_damage(self.test_character1.max_hp)
        self.assertEqual(
            self.test_character1.current_hp, self.HealthBar_normal.current_hp
        )
        self.test_character1.heal(self.test_character1.max_hp + 1)
        self.assertEqual(
            self.test_character1.current_hp, self.HealthBar_normal.current_hp
        )
        self.test_character1.heal(1)
        self.assertEqual(
            self.test_character1.current_hp, self.HealthBar_normal.current_hp
        )
        self.test_character1.take_damage(10)
        self.assertEqual(
            self.test_character1.current_hp, self.HealthBar_normal.current_hp
        )
        self.test_character1.heal(4)
        self.assertEqual(
            self.test_character1.current_hp, self.HealthBar_normal.current_hp
        )

    def test_action_panelHB_character_change(self):
        self.HealthBar_action_panel.notify(self.test_character1)
        self.assertEqual(
            self.test_character1.current_hp, self.HealthBar_action_panel.current_hp
        )
        self.HealthBar_action_panel.notify(self.test_character2)
        self.assertEqual(
            self.test_character2.current_hp, self.HealthBar_action_panel.current_hp
        )
        self.test_character1.take_damage(2)
        self.assertEqual(
            self.test_character2.current_hp, self.HealthBar_action_panel.current_hp
        )
        self.HealthBar_action_panel.notify(self.test_character1)
        self.assertEqual(
            self.test_character1.current_hp, self.HealthBar_action_panel.current_hp
        )


if __name__ == "__main__":
    unittest.main()
