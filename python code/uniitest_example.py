import unittest

def add(a,b):
    return a+b

def is_even(a):
    if a%2==0:
        return True
    else:
        return False

class MyTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(-1,1),0)

    def test_is_even(self):
        self.assertTrue(is_even(4))

    def test_id(self,a,b):
        self.assertIs(a,b)

if __name__ == '__main__' :
    unittest.main()

