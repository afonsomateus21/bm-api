# Beauty Manager

## 📋 Descrição
Este projeto consiste na API do BeautyManager, uma aplicação de agendamento voltada para o salão de beleza House Pink. 
Além dos propósitos comerciais ele também visa satisfazer os requisitos da disciplina Projeto Integrado I, do curso Sistemas e Mídias Digitais da Universidade Federal do Ceará.

## 👥 Equipe
- Afonso Mateus de Oliveira Souza - 552193
- Clara Livia Moura de Oliveira - 554010

## 🧑‍🏫 Professores Supervisores
- Cátia Luzia Oliveira da Silva
- Henrique Sérgio Lima Pequeno

## 📝 Requisitos
Atualmente, **100%** dos requisitos foram implementados.
<table border="1">
  <thead>
    <tr>
      <th>ID</th>
      <th>Nome</th>
      <th>Descrição</th>
      <th>Status</th>
      <th>Implementado em</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RF01</td>
      <td>Gerenciar usuário</td>
      <td>Permitir o cadastro, edição, visualização e exclusão de usuários do sistema (ADMIN e CLIENTE).</td>
      <td>Implementado</td>
      <td><a href="https://github.com/afonsomateus21/bm-api/blob/main/routers/user/controllers.py">Ver implementação</a></td>
    </tr>
    <tr>
      <td>RF02</td>
      <td>Cadastrar administradores</td>
      <td>Permitir que usuários do tipo ADMIN criem novos usuários com permissões de administrador (ADMIN).</td>
      <td>Implementado</td>
      <td><a href="https://github.com/afonsomateus21/bm-api/blob/main/routers/user/controllers.py">Ver implementação</a></td>
    </tr>
    <tr>
      <td>RF03</td>
      <td>Gerenciar serviços</td>
      <td>Permitir que usuários ADMIN cadastrem, atualizem, visualizem (ADMIN e CLIENTE) e excluam serviços disponíveis.</td>
      <td>Implementado</td>
      <td><a href="https://github.com/afonsomateus21/bm-api/blob/main/routers/offered_services/controllers.py">Ver implementação</a></td>
    </tr>
    <tr>
      <td>RF04</td>
      <td>Visualizar serviços</td>
      <td>Permitir que usuários CLIENTE e ADMIN visualizem a lista de serviços cadastrados com seus detalhes.</td>
      <td>Implementado</td>
      <td><a href="https://github.com/afonsomateus21/bm-api/blob/main/routers/offered_services/controllers.py">Ver implementação</a></td>
    </tr>
    <tr>
      <td>RF05</td>
      <td>Realizar agendamento</td>
      <td>Permitir que usuários CLIENTE realizem o agendamento de serviços, especificando data e horário.</td>
      <td>Implementado</td>
      <td><a href="https://github.com/afonsomateus21/bm-api/blob/main/routers/appointments/controllers.py">Ver implementação</a></td>
    </tr>
    <tr>
      <td>RF06</td>
      <td>Cancelar agendamento</td>
      <td>Permitir que usuários ADMIN e CLIENTE cancelem agendamentos de serviços existentes.</td>
      <td>Implementado</td>
      <td><a href="https://github.com/afonsomateus21/bm-api/blob/main/routers/appointments/controllers.py">Ver implementação</a></td>
    </tr>
    <tr>
      <td>RF07</td>
      <td>Notificar agendamento</td>
      <td>Notificar usuários ADMIN e CLIENTE sobre novos agendamentos realizados no sistema.</td>
      <td>Implementado</td>
      <td><a href="https://github.com/afonsomateus21/bm-api/blob/main/routers/appointments/services.py7">Ver implementação</a></td>
    </tr>
    <tr>
      <td>RF08</td>
      <td>Notificar cancelamento</td>
      <td>Notificar usuários ADMIN e CLIENTE sobre cancelamentos de agendamentos no sistema.</td>
      <td>Implementado</td>
      <td><a href="https://github.com/afonsomateus21/bm-api/blob/main/routers/appointments/services.py">Ver implementação</a></td>
    </tr>
    <tr>
      <td>RF09</td>
      <td>Reservar horários</td>
      <td>Permitir que usuários ADMIN reservem horários específicos para CLIENTES VIP.</td>
      <td>Implementado</td>
      <td><a href="https://github.com/afonsomateus21/bm-api/blob/main/routers/appointments/controllers.py">Ver implementação</a></td>
    </tr>
    <tr>
      <td>RF10</td>
      <td>Cancelar horários</td>
      <td>Permitir que usuários ADMIN cancelem reservas de horários para CLIENTES VIP.</td>
      <td>Implementado</td>
      <td><a href="https://github.com/afonsomateus21/bm-api/blob/main/routers/appointments/controllers.py">Ver implementação</a></td>
    </tr>
    <tr>
      <td>RF11</td>
      <td>Realizar login</td>
      <td>Permitir que usuários (ADMIN ou CLIENTE) façam login no sistema com suas credenciais.</td>
      <td>Implementado</td>
      <td><a href="https://github.com/afonsomateus21/bm-api/blob/main/routers/user/controllers.py">Ver implementação</a></td>
    </tr>
    <tr>
      <td>RF12</td>
      <td>Realizar logout</td>
      <td>Permitir que usuários (ADMIN ou CLIENTE) façam logout do sistema, encerrando a sessão ativa.</td>
      <td>Implementado</td>
      <td><a href="https://github.com/afonsomateus21/bm-api/blob/main/routers/user/controllers.py">Ver implementação</a></td>
    </tr>
  </tbody>
</table>


Aqui está a versão atualizada do seu README com as explicações adicionais sobre os requisitos necessários para executar o projeto, como a instalação do Python e a configuração das chaves de autenticação:

---

## 🛠️ Tecnologias Utilizadas
As seguintes tecnologias foram utilizadas na construção dessa API:
<ul>
  <li>Python</li>
  <li>FastAPI</li>
  <li>Uvicorn</li>
  <li>Pymongo</li>
  <li>MongoDB</li>
</ul>

Outros módulos foram utilizados auxiliarmente, entretanto acima listamos as principais para o funcionamento básico da API.

---

## 📦 Instalação

### **Pré-requisitos**
Antes de começar, certifique-se de que você possui os seguintes requisitos instalados e configurados:
1. **Python 3.11**: Instale o Python a partir do [site oficial](https://www.python.org/downloads/).
2. **Banco de Dados MongoDB**: Instale e configure um banco MongoDB local ou utilize um serviço em nuvem como o [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
3. **Chaves de Autenticação**:
   - **Google OAuth**: Obtenha as credenciais (`GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`) no [Google Cloud Console](https://console.cloud.google.com/).
   - **Supabase**: Obtenha as chaves (`SUPABASE_SERVICE_ROLE_KEY`, `SUPABASE_PROJECT_URL`) no painel do seu projeto no [Supabase](https://supabase.com/).
   - **Brevo**: Obtenha a chave da API (`BREVO_API_KEY`) no painel do [Brevo](https://www.brevo.com/).

---

### 1. **Clone o repositório**
```bash
$ git clone https://github.com/afonsomateus21/bm-api.git
# ou, se utilizar SSH:
$ git clone git@github.com:afonsomateus21/bm-api.git
cd bm-api
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
Crie um arquivo `.env` na raiz do projeto e configure as variáveis de ambiente necessárias. Exemplo:
```bash
GOOGLE_CLIENT_ID=sua_chave_google_client_id
GOOGLE_CLIENT_SECRET=sua_chave_google_client_secret
GOOGLE_REDIRECT_URI=http://localhost:8000/api/auth/google/callback
SECRET_KEY=sua_chave_secreta
DB_USERNAME=usuario_do_banco
DB_PASSWORD=senha_do_banco
SUPABASE_SERVICE_ROLE_KEY=sua_chave_supabase
SUPABASE_PROJECT_URL=sua_url_supabase
BREVO_API_KEY=sua_chave_brevo
```

---

## ▶️ Como executar a aplicação

### 1. **Inicie o servidor**
```bash
uvicorn main:app --reload
```

### 2. **Acesse a documentação interativa**
- **Swagger UI**: http://localhost:8000/docs
- **Redoc**: http://localhost:8000/redoc

---

## 🗂️ Estrutura do projeto
```bash
bm-api/
├── README.md
├── __pycache__
│   └── main.cpython-311.pyc
├── config
│   ├── __pycache__
│   │   ├── database.cpython-311.pyc
│   │   └── email.cpython-311.pyc
│   ├── database.py
│   └── email.py
├── estrutura.txt
├── main.py
├── requirements.txt
└── routers
    ├── appointments
    │   ├── __pycache__
    │   │   ├── controllers.cpython-311.pyc
    │   │   ├── models.cpython-311.pyc
    │   │   ├── services.cpython-311.pyc
    │   │   └── validators.cpython-311.pyc
    │   ├── controllers.py
    │   ├── models.py
    │   ├── services.py
    │   └── validators.py
    ├── offered_services
    │   ├── __pycache__
    │   │   ├── controllers.cpython-311.pyc
    │   │   ├── models.cpython-311.pyc
    │   │   ├── services.cpython-311.pyc
    │   │   └── validators.cpython-311.pyc
    │   ├── controllers.py
    │   ├── models.py
    │   ├── services.py
    │   └── validators.py
    └── user
        ├── __pycache__
        │   ├── controllers.cpython-311.pyc
        │   ├── models.cpython-311.pyc
        │   ├── services.cpython-311.pyc
        │   └── validators.cpython-311.pyc
        ├── controllers.py
        ├── models.py
        ├── services.py
        └── validators.py
```

---

## 💻 Front End
O front-end deste projeto está disponível em: [bm-web](https://github.com/afonsomateus21/bm-web/).

---

## 📝 Licença
Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
