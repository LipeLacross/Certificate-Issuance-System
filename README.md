# Sistema de Emissão de Certificados

O Sistema de Emissão de Certificados é uma aplicação web que permite a criação, gerenciamento e visualização de certificados. É projetado para facilitar a emissão de certificados de conclusão de cursos, treinamentos e outros eventos.

## 🔨 Funcionalidades do Projeto

- **Listar Certificados**: Recupera uma lista de todos os certificados armazenados no sistema.
- **Criar Certificado**: Adiciona um novo certificado com base nas informações fornecidas.
- **Detalhes do Certificado**: Exibe os detalhes de um certificado específico.
- **Atualizar Certificado**: Atualiza as informações de um certificado existente.
- **Deletar Certificado**: Remove um certificado específico do sistema.

### Exemplo Visual do Projeto

![Screenshot 2024-08-18 150159](https://github.com/user-attachments/assets/8083860d-a3c1-4ae3-a62b-3b0ee0d7829e)
![Screenshot 2024-08-18 145650](https://github.com/user-attachments/assets/d168fc0a-06a0-41f5-9ff3-fe5419e16b32)
![Screenshot 2024-08-18 150624](https://github.com/user-attachments/assets/8f8503ad-dafa-49d4-a4b6-5df94417383a)

## ✔️ Técnicas e Tecnologias Utilizadas

- **Flask**: Framework web para criar o servidor da API.
- **SQLAlchemy**: ORM para interagir com o banco de dados MySQL.
- **MySQL**: Banco de dados relacional para armazenar os certificados.
- **Python**: Linguagem de programação principal utilizada no desenvolvimento da aplicação.

## 📁 Estrutura do Projeto

- **app/**: Contém o código fonte da aplicação, incluindo a configuração do banco de dados, modelos, rotas e recursos.
    - **`__init__.py`**: Inicializa o aplicativo Flask e configura o banco de dados.
    - **`database.py`**: Configuração e conexão com o banco de dados.
    - **`models.py`**: Definição dos modelos de dados.
    - **`resources.py`**: Recursos para a API.
    - **`routes.py`**: Definição das rotas da API e lógica de controle.
    - **templates/**: Contém os arquivos HTML utilizados pela aplicação.
- **.venv/**: Ambiente virtual contendo as dependências do projeto.
- **.gitignore**: Arquivo para ignorar arquivos e diretórios no controle de versão.
- **LICENSE**: Licença do projeto.
- **README.md**: Documentação do projeto.
- **requirements.txt**: Lista de dependências do projeto.
- **run.py**: Script para iniciar o servidor Flask.

## 🛠️ Abrir e Rodar o Projeto

1. Clone o repositório para seu ambiente local.
2. Instale as dependências listadas no arquivo `requirements.txt`.
3. Configure o banco de dados MySQL e ajuste as credenciais no arquivo `app/database.py`.
4. Inicie o servidor Flask executando o script `run.py`.

   O servidor estará disponível em `http://127.0.0.1:5000`.

## 🌐 Deploy

Para o deploy em um ambiente de produção, considere utilizar um servidor WSGI como Gunicorn e um servidor web como Nginx. Além disso, configure um banco de dados MySQL acessível para a aplicação e ajuste as configurações de ambiente conforme necessário.

