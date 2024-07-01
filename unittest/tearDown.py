#This method tidies up after the test method has been run
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
'''if the setUp method succeeded teardown will be run regardless of
the outcome of test method whether they succ or failed.
the above working environ is a test fixture.
