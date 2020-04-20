class Credential:
    
    credential_list = [] 
    
    def __init__(self,account_name,passwordkey):
        self.account_name = account_name
        self.passwordkey = passwordkey
    def save_credential(self):
        
        Credential.credential_list.append(self)
    @classmethod
    def display_credentials(cls):
        
        return cls.credential_list
    @classmethod
    def delete_credential(cls,account):
        '''
        delete a credential
        '''
        for credential in cls.credential_list:
            if credential.account_name == account:
                return credential
        
        
   