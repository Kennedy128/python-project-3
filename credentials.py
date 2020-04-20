class Credential:
    
    credential_list = [] 
    
    def __init__(self,account_name,passwordkey):
        '''
        creates new instances using the init method
        '''
        self.account_name = account_name
        self.passwordkey = passwordkey
    def save_credential(self):
        '''
        it saves the credential by adding it to the list using the append method
        '''
        
        Credential.credential_list.append(self)
    @classmethod
    def display_credentials(cls):
        '''
        it displays the credentials in the list
        '''
        
        return cls.credential_list
    @classmethod
    def delete_credential(cls,account):
        '''
        deletes a credential
        '''
        for credential in cls.credential_list:
            if credential.account_name == account:
                return credential
        
        
   