# Invista Me

Sistema básico de gestão de investimentos desenvolvido em Django.

## 🚀 Sobre o Projeto

Projeto inicial Django para implementações de futuras features relacionadas ao controle de investimentos pessoais.

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.1.5
- **Banco de Dados**: SQLite
- **Linguagem**: Python
- **Template Engine**: Django Templates

## 📋 Funcionalidades Atuais

- Listagem de investimentos
- Criação de novos investimentos
- Visualização de detalhes
- Painel administrativo

## ⚙️ Pré-requisitos

- Python 3.8+
- pip

## 🚀 Como Executar

1. **Clone o repositório**
```bash
git clone https://github.com/Aqueiroz2/Django.git
cd projeto_invista_me
```

2. **Instale as dependências**
```bash
pip install django
```

3. **Execute as migrações**
```bash
python manage.py migrate
```

4. **Inicie o servidor**
```bash
python manage.py runserver
```

5. **Acesse a aplicação**
- http://127.0.0.1:8000/ - Página principal
- http://127.0.0.1:8000/admin/ - Painel administrativo

## 📁 Estrutura do Projeto

```
projeto_invista_me/
├── invista_me/                 # App principal
│   ├── models.py              # Modelo Investimento
│   ├── views.py               # Views da aplicação
│   ├── admin.py               # Configuração admin
│   └── templates/             # Templates HTML
└── projeto_invista_me/        # Configurações do projeto
```

## 🔮 Próximos Passos

- Implementar autenticação de usuários
- Adicionar validações de dados
- Melhorar interface de usuário
- Implementar relatórios e gráficos
- Adicionar testes automatizados

## 📝 Licença

Este projeto está sob a licença MIT.
