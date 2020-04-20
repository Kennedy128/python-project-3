import unittest

from credentials import Credential

class TestUser(unittest.TestCase):
   
    def setUp(self):
        
        self.new_credential = Credential("twitter","kennedymbithi12")
    def test_init(self):
         
        self.assertEqual(self.new_credential.account_name,"twitter")
        self.assertEqual(self.new_credential.passwordkey,"kennedymbithi12")
        
if __name__ == '__main__':
    unittest.main()