# 📦 Sistema de Controle de Estoque

Sistema de controle de estoque desenvolvido em **Python**, com o objetivo de praticar lógica de programação, estruturas de dados, validação de entradas, manipulação de arquivos e organização de código.

O sistema permite cadastrar e gerenciar produtos, controlar entradas e saídas de estoque, consultar informações e gerar relatórios.

## 🚀 Funcionalidades

- ✅ Cadastro de produtos
- ✅ Cadastro de vários produtos
- ✅ Listagem de produtos
- ✅ Busca de produtos por nome
- ✅ Busca sem diferenciação entre letras maiúsculas e minúsculas
- ✅ Alteração de produtos
- ✅ Remoção de produtos
- ✅ Entrada de estoque
- ✅ Saída de estoque
- ✅ Validação de dados
- ✅ Prevenção de produtos duplicados
- ✅ Controle de estoque insuficiente
- ✅ Histórico de movimentações
- ✅ Relatórios do estoque
- ✅ Identificação de produtos com estoque baixo
- ✅ Identificação de produtos sem estoque
- ✅ Cálculo do valor total do estoque
- ✅ Salvamento automático dos dados em arquivos JSON

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **JSON**
- **Git**
- **GitHub**

### Bibliotecas utilizadas

- `json`
- `os`
- `datetime`

Todas fazem parte da biblioteca padrão do Python.

## 📂 Estrutura do projeto

```text
sistema-estoque/
│
├── main.py
├── produtos.json
├── historico.json
├── README.md
├── .gitignore
└── .venv/
```

> A pasta `.venv/` é utilizada apenas no ambiente local e não deve ser enviada para o GitHub.

## ▶️ Como executar

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entrar na pasta

```bash
cd sistema-estoque
```

### 3. Executar o sistema

```bash
python main.py
```

## 💻 Menu principal

```text
=============================================
          SISTEMA DE ESTOQUE
=============================================
1 - Cadastro de produtos
2 - Listar produtos
3 - Buscar produto
4 - Alterar produto
5 - Remover produto
6 - Entrada de estoque
7 - Saída de estoque
8 - Relatórios
9 - Histórico
0 - Sair
=============================================
```

## 💾 Armazenamento

Os produtos são armazenados no arquivo:

```text
produtos.json
```

O histórico das movimentações é armazenado em:

```text
historico.json
```

Dessa forma, os dados continuam disponíveis mesmo depois que o programa é encerrado.

## 📊 Relatórios

O sistema apresenta informações como:

- quantidade total de produtos;
- quantidade total de itens em estoque;
- valor total do estoque;
- produto mais caro;
- produto com maior quantidade em estoque;
- produtos com estoque baixo;
- produtos sem estoque.

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido como parte do meu aprendizado em **desenvolvimento de software com Python**, com foco em transformar conceitos básicos de programação em uma aplicação funcional.

Durante o desenvolvimento foram utilizados conceitos como:

- variáveis;
- condicionais;
- estruturas de repetição;
- listas;
- dicionários;
- funções;
- tratamento de exceções;
- manipulação de arquivos;
- JSON;
- organização de código;
- validação de dados.

## 🔮 Possíveis melhorias futuras

O projeto poderá futuramente receber novas versões com:

- banco de dados SQLite;
- SQL;
- testes automatizados;
- API REST;
- FastAPI;
- autenticação de usuários;
- interface gráfica ou web;
- dashboards e gráficos.

Essas funcionalidades não fazem parte da versão atual.

## 👨‍💻 Autor

**Caio Gabriel**

Projeto desenvolvido para estudos e composição de portfólio em desenvolvimento de software.