import unittest

from translator import english_to_french, french_to_english


class TestFrench(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bye')

class TestEnglish(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hi'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Au revoir')


unittest.main()




