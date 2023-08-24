# API RD Station Python

Este repositório contém um conjunto de ferramentas e scripts para interagir com a API da RD Station, uma plataforma amplamente utilizada para automação de marketing, integração de dados e gerenciamento de leads. Com estas ferramentas, você pode facilmente criar, atualizar e gerenciar contatos na sua conta da RD Station.

## Pré-requisitos

Antes de começar a usar esta biblioteca e os scripts, certifique-se de:

1. Criar um aplicativo na RD Station e obter as credenciais (client_id e client_secret) necessárias.
2. Ter um ambiente Python configurado no seu sistema.
3. Instalar a biblioteca `python-dotenv` usando o seguinte comando:

```bash
pip install python-dotenv
```

## Configuração do dotenv
O arquivo .env contém as informações sensíveis que serão usadas pela biblioteca e pelos scripts, como tokens de acesso e informações de autenticação. Embora não seja recomendado incluir este arquivo no repositório, você pode criar um arquivo .env no diretório raiz do projeto e preencher as informações necessárias da seguinte maneira:

```bash
TOKEN_RD=seu_token_aqui
REFRESH_TOKEN=seu_refresh_token_aqui
RD_ID=seu_client_id_aqui
RD_SECRET=seu_client_secret_aqui
```

Certifique-se de substituir os valores seu_token_aqui, seu_refresh_token_aqui, seu_client_id_aqui e seu_client_secret_aqui pelas informações reais obtidas na configuração do aplicativo na RD Station.

## Utilizando a API
Após configurar o ambiente, você pode usar a classe RdStation do arquivo api_rdstation.py para interagir com a API da RD Station. A classe fornece métodos para criar e atualizar contatos, além de gerenciar a validação e renovação de tokens.

Exemplo de Criação de Contato:
```bash
# Criar uma instância da classe RdStation
rd_station = RdStation(TOKEN_RD, REFRESH_TOKEN, RD_ID, RD_SECRET)

# Criar um payload para o novo contato
payload_create = {
    "nome": "yuri",
    "tags": ["teste", "api"] 
}

# Criar o contato usando a API
rd_station.create_contact(payload_create)
```

Exemplo de Atualização de Contato:
```bash
# Criar uma instância da classe RdStation
rd_station = RdStation(TOKEN_RD, REFRESH_TOKEN, RD_ID, RD_SECRET)

# Criar um payload para atualizar o contato
payload_update = {
    "tags":["atualizacao", "contato"]
}

# Atualizar o contato usando a API
rd_station.update_contact('email@example.com', payload_update)
```

Certifique-se de personalizar os payloads com as informações relevantes para o contato que você deseja criar ou atualizar.

Com essas ferramentas e exemplos, você estará pronto para utilizar a API da RD Station para automatizar suas ações de marketing e gerenciamento de contatos. Lembre-se de proteger suas informações sensíveis usando o python-dotenv e de seguir as práticas recomendadas de segurança ao lidar com credenciais e dados de usuário.



