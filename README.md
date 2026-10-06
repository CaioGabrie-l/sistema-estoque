# Sistema de Controle de Estoque

Projeto desenvolvido em Python como parte dos meus estudos em Análise e Desenvolvimento de Sistemas.

A ideia foi criar um sistema simples de controle de estoque para praticar programação na prática, desde a lógica básica até a organização de dados e persistência em arquivos.

## Sobre o projeto

O sistema funciona pelo terminal e permite cadastrar e gerenciar produtos, controlar entradas e saídas do estoque e consultar algumas informações através de relatórios.

Durante o desenvolvimento, fui adicionando novas funcionalidades conforme aprendia novos conceitos de Python.

## Funcionalidades

- Cadastro de produtos
- Cadastro de vários produtos
- Listagem de produtos
- Busca por nome
- Alteração de produtos por ID ou nome
- Remoção de produtos por ID ou nome
- Entrada de estoque
- Saída de estoque
- Validação de dados
- Verificação de estoque insuficiente
- Prevenção de produtos duplicados
- Histórico de movimentações
- Relatórios do estoque
- Identificação de produtos com estoque baixo
- Identificação de produtos sem estoque
- Cálculo do valor total do estoque
- Salvamento automático dos dados

## Tecnologias utilizadas

- Python
- JSON
- Git
- GitHub

Também utilizei algumas bibliotecas que já fazem parte do Python, como:

- `json`
- `os`
- `datetime`

## Como executar

Clone o repositório:

```bash
git clone https://github.com/CaioGabrie-l/sistema-estoque.git
```

Entre na pasta:

```bash
cd sistema-estoque
```

Execute o programa:

```bash
python main.py
```

## Estrutura do projeto

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

A pasta `.venv` é utilizada apenas no ambiente local e não é enviada para o GitHub.

## Salvamento dos dados

Os produtos cadastrados são armazenados no arquivo `produtos.json`.

O histórico de entradas, saídas e cadastros fica no arquivo `historico.json`.

Dessa forma, os dados continuam disponíveis mesmo depois de fechar o programa.

## O que pratiquei neste projeto

Esse foi um dos meus primeiros projetos maiores em Python e serviu para colocar em prática conceitos que estou estudando.

Entre eles:

- Variáveis e tipos de dados
- Condicionais
- Laços de repetição
- Listas
- Dicionários
- Funções
- Tratamento de erros
- Validação de entradas
- Manipulação de arquivos
- JSON
- Organização de código
- Git e GitHub

## Próximos passos

Algumas coisas que pretendo estudar e utilizar em projetos futuros:

- Banco de dados
- SQL
- SQLite
- Testes automatizados
- APIs
- FastAPI
- Interfaces web

Essas funcionalidades não fazem parte da versão atual do projeto.

## Objetivo

O principal objetivo deste projeto foi aprender Python desenvolvendo algo do início ao fim, e começar a montar meu portfólio enquanto avanço nos estudos de Análise e Desenvolvimento de Sistemas.

## Autor

**Caio Gabriel**

Estudante de Análise e Desenvolvimento de Sistemas.