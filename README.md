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
Atualmente, **41,67%** dos requisitos foram implementados.
<table border="1">
  <thead>
    <tr>
      <th>ID</th>
      <th>Nome</th>
      <th>Descrição</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RF01</td>
      <td>Gerenciar usuário</td>
      <td>Permitir o cadastro, edição, visualização e exclusão de usuários do sistema (ADMIN e CLIENTE).</td>
      <td>Implementado</td>
    </tr>
    <tr>
      <td>RF02</td>
      <td>Cadastrar administradores</td>
      <td>Permitir que usuários do tipo ADMIN criem novos usuários com permissões de administrador (ADMIN).</td>
      <td>Implementado</td>
    </tr>
    <tr>
      <td>RF03</td>
      <td>Gerenciar serviços</td>
      <td>Permitir que usuários ADMIN cadastrem, atualizem, visualizem (ADMIN e CLIENTE) e excluam serviços disponíveis.</td>
      <td>Implementado</td>
    </tr>
    <tr>
      <td>RF04</td>
      <td>Visualizar serviços</td>
      <td>Permitir que usuários CLIENTE e ADMIN visualizem a lista de serviços cadastrados com seus detalhes.</td>
      <td>Implementado</td>
    </tr>
    <tr>
      <td>RF05</td>
      <td>Realizar agendamento</td>
      <td>Permitir que usuários CLIENTE realizem o agendamento de serviços, especificando data e horário.</td>
      <td>Pendente</td>
    </tr>
    <tr>
      <td>RF06</td>
      <td>Cancelar agendamento</td>
      <td>Permitir que usuários ADMIN e CLIENTE cancelem agendamentos de serviços existentes.</td>
      <td>Pendente</td>
    </tr>
    <tr>
      <td>RF07</td>
      <td>Notificar agendamento</td>
      <td>Notificar usuários ADMIN e CLIENTE sobre novos agendamentos realizados no sistema.</td>
      <td>Pendente</td>
    </tr>
    <tr>
      <td>RF08</td>
      <td>Notificar cancelamento</td>
      <td>Notificar usuários ADMIN e CLIENTE sobre cancelamentos de agendamentos no sistema.</td>
      <td>Pendente</td>
    </tr>
    <tr>
      <td>RF09</td>
      <td>Reservar horários</td>
      <td>Permitir que usuários ADMIN reservem horários específicos para CLIENTES VIP.</td>
      <td>Pendente</td>
    </tr>
    <tr>
      <td>RF10</td>
      <td>Cancelar horários</td>
      <td>Permitir que usuários ADMIN cancelem reservas de horários para CLIENTES VIP.</td>
      <td>Pendente</td>
    </tr>
    <tr>
      <td>RF11</td>
      <td>Realizar login</td>
      <td>Permitir que usuários (ADMIN ou CLIENTE) façam login no sistema com suas credenciais.</td>
      <td>Implementado</td>
    </tr>
    <tr>
      <td>RF12</td>
      <td>Realizar logout</td>
      <td>Permitir que usuários (ADMIN ou CLIENTE) façam logout do sistema, encerrando a sessão ativa.</td>
      <td>Pendente</td>
    </tr>
  </tbody>
</table>


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
