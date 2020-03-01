import unittest

class assertTest(unittest.TestCase):

    def test_assert(self):
        a={'hemraj','arjun','amruth'}
        #self.assertIn('arjun',a)
        self.assertNotIn('arjun',a)


if __name__ == '__main__':
    unittest.main()