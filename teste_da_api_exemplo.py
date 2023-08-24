import os
from dotenv import load_dotenv, find_dotenv
from api_rdstation import RdStation

# Carregar variáveis de ambiente do arquivo .env
load_dotenv(find_dotenv())
TOKEN_RD = os.getenv('TOKEN_RD', 'seu_token_aqui')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN', 'seu_refresh_token_aqui')
RD_ID = os.getenv('RD_ID', 'seu_client_id_aqui')
RD_SECRET = os.getenv('RD_SECRET', 'seu_client_secret_aqui')

# Criar uma instância da classe RdStation
rd_station = RdStation(TOKEN_RD, REFRESH_TOKEN, RD_ID, RD_SECRET)

# Testar a criação de um contato
payload_create = {
    "legal_bases": [
        {
            "category": "communications",
            "type": "consent",
            "status": "granted",
        }
    ],
    'name': 'Nome do Contato',
    'email': 'email@example.com',
    'personal_phone': '+55 123456789',
    'mobile_phone': '+55 123456789',
    'tags': ['tag1', 'tag2']
}

rd_station.create_contact(payload_create)



###########################################################################################################



# Testar a atualização de um contato
payload_update = {
    'name': 'Novo Nome do Contato',
    'tags': ['nova_tag']
}

rd_station.update_contact('email@example.com', payload_update)
