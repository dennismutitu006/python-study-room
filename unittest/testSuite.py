'''
it is recommended u use TestCase implementations to group test according
to features they test. unittest provides a mechanism 4 this: the test suite,
rep by unittest's TestSuite class.
In most cases, calling unittest.main() will do the right thing and collect all the module’s test cases for you and execute them.
However, should you want to customize the building of your test suite,
you can do it yourself:
'''

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ = '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())


'''advantages of placing test code in a separate module
The test module can be run standalone from the command line.

The test code can more easily be separated from shipped code.

There is less temptation to change test code to fit the code it tests without a good reason.

Test code should be modified much less frequently than the code it tests.

Tested code can be refactored more easily.

Tests for modules written in C must be in separate modules anyway, so why not be consistent?

If the testing strategy changes, there is no need to change the source code.
'''
