# Beauty Manager
## 👥 Equipe
- Afonso Mateus de Oliveira Souza - 552193
- Clara Livia Moura de Oliveira - 554010

## 📋 Descrição
Este projeto consiste na API do BeautyManager, uma aplicação de agendamento voltada para o salão de beleza House Pink. 
Além dos propósitos comerciais ele também visa satisfazer os requisitos da disciplina Projeto Integrado I, do curso Sistemas e Mídias Digitais da Universidade Federal do Ceará.

## 🛠️ Tecnologias Utilizadas
As seguintes tecnologias foram utilizadas na construção dessa API:
<ul>
  <li>Python</li>
  <li>FastAPI</li>
  <li>Uvicorn</li>
  <li>Pymong</li>
  <li>MongoDB</li>
</ul>

Outros módulos foram utilizados auxiliarmente, entretando acima listamos as principais para o funcionamento básico da API

## 📦 Instalação
### 1. **Clone o repositório**
```bash
$ git clone https://github.com/afonsomateus21/bm-api.git ou
$ git clone git@github.com:afonsomateus21/bm-api.git se utilizar SSH
cd sua-aplicacao
```

### 2. **Crie um ambiente virtual**
```bash
python3.11 -m venv env
```

### 3. **Ative o ambiente virtual**
- Linux/Mac:
  ```bash
  source env/bin/activate
  ```

- Windows:
  ```bash
  .\env\Scripts\activate
  ```

### 4. **Instale as dependências**
```bash
  pip install -r requirements.txt
```

### 5. **Configure as variáveis de ambiente**
Crie um arquivo .env na raiz do projeto e configure as variáveis de ambiente necessárias, como exemplo:
```bash
  GOOGLE_CLIENT_ID=test
  GOOGLE_CLIENT_SECRET=test
  GOOGLE_REDIRECT_URI=http://localhost:8000/api/auth/google/callback
  SECRET_KEY=test
  DB_USERNAME=db_username
  DB_PASSWORD=db_password
```

## ▶️Como executar a aplicação
### 1. Inicie o servidor
```bash
  uvicorn main:app --reload
``` 

### 2. Acesse a documentação interativa
- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

## 🗂️ Estrutura do projeto
```bash
  bm-api/
  │
  ├── main.py                # Arquivo principal da aplicação
  ├── routers/               # Rotas organizadas por funcionalidades
  │   ├── user/
  │   │   ├── controllers.py # Controladores para usuários
  │   │   ├── services.py    # Lógica de negócios para usuários
  │   │   ├── models.py      # Modelo do usuário
  │   │   ├── validators.py  # Classes validadoras os dados dos usuários
  │   └── offered_services/
  │   │   ├── controllers.py # Controladores para serviços
  │   │   ├── services.py    # Lógica de negócios para serviços
  │   │   ├── models.py      # Modelo do serviço
  │   │   ├── validators.py  # Classes validadoras dos dados dos serviços
  ├── config/
  │   ├── database.py        # Configuração da conexão com o MongoDB
  ├── requirements.txt       # Dependências do projeto
  └── .env                   # Variáveis de ambiente do projeto
```

## 📝 Licença
Este projeto está licenciado sob a MIT License.
