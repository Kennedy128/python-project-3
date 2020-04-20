import unittest

from credentials import Credential

class TestUser(unittest.TestCase):
   
    def setUp(self):
        
        self.new_credential = Credential("twitter","kennedymbithi12")
    def test_init(self):
         
        self.assertEqual(self.new_credential.account_name,"twitter")
        self.assertEqual(self.new_credential.passwordkey,"kennedymbithi12")
    def test_save_credential(self):
        
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)
    def test_display_credentials(self):
        
        self.assertEqual(Credential.display_credentials(),Credential.credential_list)
    def test_delete_credential(self):
        '''
        test_delete_credential to see if we can remove a 
        credential from credentials list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("test","0893uhjnv")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)
        
        
if __name__ == '__main__':
    unittest.main()