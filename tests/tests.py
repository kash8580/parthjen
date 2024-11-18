import unittest
from operations.operations import rev,palin

class testing(unittest.TestCase):
    def test_rev(self):
        self.assertEqual(rev("hello"),"olleh")

    def test_palin(self):
        self.assertTrue(palin("naman"),True)



        

if __name__=="__main__":
    unittest.main()