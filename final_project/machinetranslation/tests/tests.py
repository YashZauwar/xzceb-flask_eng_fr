import unittest
from translator import english_to_french, french_to_english

class TestMachineTranslation(unittest.TestCase):

    def test_french_to_english(self):
        #self.assertEqual(french_to_english(None), None)
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    
        self.assertEqual(french_to_english('Hello'), 'Hello')

    def test_english_to_french(self):
        #self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french('Bonjour'), 'Bonjour') 


if __name__ == '__main__':
    unittest.main()
