import unittest #by default it is there
class MyTestCase(unittest.TestCase):
    def test_something(self): #test key word should be there in the begining are at end
        self.assertEqual(True,True) #add assertion here

    def test_add(self):
        self.assertEqual(30,20+10)

if __name__=='__main__':
    unittest.main()