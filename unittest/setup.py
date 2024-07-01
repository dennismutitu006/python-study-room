#Tests can be numerous and their set up can be repetitive.
#We can factor out set-up code by implementing a method called setUp()
#This is a method called to prepare the test fixture/called b4 the test methd
#the testing framework will automatically call the method for every test run.
import unittest

class WidgetTestCase(unittest.TestCase):
    def setup(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                            'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                            'wrong size after resize')
