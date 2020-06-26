import unittest
from simplePackage.simpleMath import simpleMath
from simplePackage.dog import dog

class simplePackageTests(unittest.TestCase):

    def test_dogTricks(self):
        dogInstance = dog('Doggo')
        dogInstance.add_trick('sit')
        dogInstance.add_trick('come')
        self.assertTrue(len(dogInstance.tricks) == 2)

    def test_simpleMathSum(self):
        simpleMathInstance = simpleMath(5)
        sum = simpleMathInstance.sumNumbers(6)
        self.assertEqual(sum, 11)

    def test_isupper(self):
        self.assertTrue('foo'.islower())
        self.assertTrue('FOOO'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)