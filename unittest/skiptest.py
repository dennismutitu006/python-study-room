'''skipping a test is a matter of using skip() decorator.
or one of its conditional variants , calling TestCase.skipTest()
within a setup() or raising skipTest directly.
'''
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouln't happen")

    @unittest.skipIf(mylib.__version__< (1, 3),
                        "not supported in this library version")
    def test_format(self):
        #Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

     def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass

'''nb classes can be skipped just like methods'''
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
'''expectedFailure() decorator for expected failures'''
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
