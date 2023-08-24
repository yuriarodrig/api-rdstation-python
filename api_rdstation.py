import requests

class RdStation(object):
    def __init__(self, token, refresh_token, client_id, client_secret):
        self.token = token
        self.refresh_token = refresh_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.header = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
    def update_token(self, token_new, refresh_token_new):
        TOKEN_API = 'Caminho para salvar token'
        with open(TOKEN_API, 'w') as file:
            file.write(f"{token_new}\n{refresh_token_new}")
            
    def validate_token(self):
        url = "https://api.rd.services/auth/token"
        
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token
        }
        
        response = requests.post(url, json=payload, headers=self.header)
        
        if response.status_code == 200:
            token_new = response.json()['access_token']
            refresh_token_new = response.json()['refresh_token']
            self.update_token(token_new, refresh_token_new)
        else:
            print(response.status_code)
            print(response.text)
    
    def create_contact(self, payload):
        url = "https://api.rd.services/platform/contacts"
        response = requests.post(url, json=payload, headers=self.header)
        
        if response.status_code == 200:
            print('Contato criado com sucesso!')
            print(response.text)
            return True
        elif response.status_code == 401:
            print(response.text)
            print('Token expirado')
            self.validate_token()
            return False
        else:
            print(response.text)
            return True
        
    def update_contact(self, email, payload):
        email_encoded = email.replace('@', '%40')
        url = f"https://api.rd.services/platform/contacts/email:{email_encoded}"
        response = requests.patch(url, json=payload, headers=self.header)
        
        if response.status_code == 200:
            print(response.text)
            print('Contato atualizado com sucesso!')
            return True
        else:
            print(response.status_code)
            print(response.text)
            return False
