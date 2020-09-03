from Class import Dog
import unittest

class TestStringMethods(unittest.TestCase):

    def test_bark(self):
      d = Dog('Tim',8,'happy')
      self.assertEqual(d.bark(), print("Bark Bark Bark"))

    def test_is_tired(self):
      d = Dog('Tim',8,'happy')
      self.assertEqual(d.is_tired(), print("sleeping Zzz"))

    def test_is_happy(self):
      d = Dog('Tim',8,'happy')
      self.assertEqual(d.is_happy(), print("wags tail"))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
