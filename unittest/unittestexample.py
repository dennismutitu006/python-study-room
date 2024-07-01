import unittest
''' a module called unittest is imported to enable creation of test cases
new classes using the TestCase base class in the unittest.
'''
#the section below is a short script to test three string methods

class TestStringMethods(unittest.TestCase):
    '''we are using the TestCase in unittest as our base class'''
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        #check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
