import unittest

from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    def test1(self):
        """Test english to french"""
        # test when "hello" is given as input the output is Bonjour.
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        # test when " " is given as input the output is "Error: Enter a word".
        self.assertEqual(english_to_french(
            " "), "Error: Enter a word")
        # test when "Bonjour" is given as input the output is "Bonjour".
        self.assertEqual(english_to_french("Bonjour"), "Bonjour")

        """Test french to english"""
        # test when "Bonjour" is given as input the output is "Hello".
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        # test when " " is given as input the output is "Error: Enter a word".
        self.assertEqual(french_to_english(
            " "), "Error: Enter a word")
        # test when "Hello" is given as input the output is "Hello".
        self.assertEqual(french_to_english("Hello"), "Hello")


unittest.main()
