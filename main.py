import json
import os
from datetime import datetime

ARQUIVO_PRODUTOS = "produtos.json"
ARQUIVO_HISTORICO = "historico.json"

produtos = []
historico = []


def carregar_dados():
    global produtos, historico

    if os.path.exists(ARQUIVO_PRODUTOS):
        try:
            with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as arquivo:
                produtos = json.load(arquivo)
        except (json.JSONDecodeError, FileNotFoundError):
            produtos = []

    if os.path.exists(ARQUIVO_HISTORICO):
        try:
            with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as arquivo:
                historico = json.load(arquivo)
        except (json.JSONDecodeError, FileNotFoundError):
            historico = []


def salvar_dados():
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, ensure_ascii=False, indent=4)

    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, ensure_ascii=False, indent=4)


def gerar_id():
    if not produtos:
        return 1

    return max(produto["id"] for produto in produtos) + 1


def buscar_por_id(id_produto):
    for produto in produtos:
        if produto["id"] == id_produto:
            return produto

    return None


def buscar_por_nome(nome):
    resultados = []

    for produto in produtos:
        if nome.lower() in produto["nome"].lower():
            resultados.append(produto)

    return resultados


def localizar_produto():
    """
    Permite localizar um produto usando ID ou nome.
    Retorna o produto encontrado ou None.
    """

    while True:
        entrada = input("Digite o ID ou nome do produto: ").strip()

        if not entrada:
            print("Digite um ID ou nome válido!")
            continue

        # Primeiro tenta localizar pelo ID
        try:
            id_produto = int(entrada)
            produto = buscar_por_id(id_produto)

            if produto is None:
                print("Produto não encontrado!")
                return None

            return produto

        except ValueError:
            pass

        # Se não for número, procura pelo nome
        resultados = buscar_por_nome(entrada)

        if not resultados:
            print("Produto não encontrado!")
            return None

        # Encontrou apenas um produto
        if len(resultados) == 1:
            return resultados[0]

        # Encontrou vários produtos
        print("\nForam encontrados vários produtos:")

        for produto in resultados:
            print(
                f"ID: {produto['id']} | "
                f"Nome: {produto['nome']} | "
                f"Quantidade: {produto['quantidade']}"
            )

        try:
            id_produto = int(
                input("\nDigite o ID do produto desejado: ").strip()
            )
        except ValueError:
            print("Digite um ID válido!")
            continue

        produto = buscar_por_id(id_produto)

        if produto is None or produto not in resultados:
            print("ID inválido para os produtos encontrados!")
            continue

        return produto


def registrar_movimentacao(produto, tipo, quantidade):
    movimentacao = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "produto_id": produto["id"],
        "produto": produto["nome"],
        "tipo": tipo,
        "quantidade": quantidade,
        "estoque_atual": produto["quantidade"]
    }

    historico.append(movimentacao)


def cadastrar_produto():
    print("\n=== CADASTRAR PRODUTO ===")

    nome = input("Nome do produto: ").strip()

    if not nome:
        print("O nome não pode ficar vazio!")
        return False

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print("Esse produto já está cadastrado!")
            return False

    try:
        preco = float(input("Preço do produto: "))
    except ValueError:
        print("Digite um preço válido!")
        return False

    if preco <= 0:
        print("O preço deve ser maior que zero!")
        return False

    try:
        quantidade = int(input("Quantidade em estoque: "))
    except ValueError:
        print("Digite uma quantidade válida!")
        return False

    if quantidade < 0:
        print("A quantidade não pode ser negativa!")
        return False

    produto = {
        "id": gerar_id(),
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

    if quantidade > 0:
        registrar_movimentacao(produto, "CADASTRO", quantidade)

    salvar_dados()

    print("\nProduto cadastrado com sucesso!")
    print(f"ID: {produto['id']}")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")
    print(
        f"Valor em estoque: "
        f"R$ {produto['preco'] * produto['quantidade']:.2f}"
    )

    return True


def menu_cadastro():
    while True:
        print("\n=== CADASTRO DE PRODUTOS ===")
        print("1 - Cadastrar produto")
        print("2 - Cadastrar vários produtos")
        print("0 - Menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto()

            print("\n1 - Cadastrar outro produto")
            print("0 - Menu principal")

            escolha = input("Escolha uma opção: ").strip()

            if escolha == "1":
                continue

            elif escolha == "0":
                return

            else:
                print("Opção inválida!")

        elif opcao == "2":
            cadastrar_varios_produtos()

        elif opcao == "0":
            return

        else:
            print("Opção inválida!")


def cadastrar_varios_produtos():
    while True:
        print("\n=== CADASTRAR VÁRIOS PRODUTOS ===")

        cadastrar_produto()

        print("\n------------------------------")
        print("1 - Cadastrar outro produto")
        print("0 - Menu principal")
        print("------------------------------")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            continue

        elif opcao == "0":
            return

        else:
            print("Opção inválida!")


def listar_produtos():
    while True:
        print("\n=== PRODUTOS CADASTRADOS ===")

        if not produtos:
            print("Nenhum produto cadastrado.")

        else:
            valor_total = 0
            quantidade_total = 0

            for produto in produtos:
                valor_produto = produto["preco"] * produto["quantidade"]

                print(f"\nID: {produto['id']}")
                print(f"Nome: {produto['nome']}")
                print(f"Preço: R$ {produto['preco']:.2f}")
                print(f"Quantidade: {produto['quantidade']}")
                print(f"Valor em estoque: R$ {valor_produto:.2f}")
                print("-" * 30)

                valor_total += valor_produto
                quantidade_total += produto["quantidade"]

            print("\n=== RESUMO ===")
            print(f"Produtos cadastrados: {len(produtos)}")
            print(f"Quantidade total: {quantidade_total}")
            print(f"Valor total do estoque: R$ {valor_total:.2f}")

        print("\n0 - Menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            return

        print("Opção inválida!")


def buscar_produto():
    while True:
        print("\n=== BUSCAR PRODUTO ===")

        nome_busca = input("Digite o nome do produto: ").strip()

        if not nome_busca:
            print("Digite algum nome para pesquisar.")
            continue

        resultados = buscar_por_nome(nome_busca)

        if not resultados:
            print("\nProduto não encontrado!")
            print("Digite outro nome para pesquisar.")
            print("\n0 - Menu principal")

            opcao = input(
                "Digite o nome novamente ou 0 para voltar: "
            ).strip()

            if opcao == "0":
                return

            nome_busca = opcao
            resultados = buscar_por_nome(nome_busca)

            if not resultados:
                print("\nProduto não encontrado!")
                continue

        print(f"\nProdutos encontrados: {len(resultados)}")

        for produto in resultados:
            print("\n--------------------")
            print(f"ID: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']}")
            print(
                f"Valor em estoque: "
                f"R$ {produto['preco'] * produto['quantidade']:.2f}"
            )

        print("\n0 - Menu principal")
        print("1 - Fazer nova busca")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            return

        elif opcao == "1":
            continue

        else:
            print("Opção inválida!")


def alterar_produto():
    while True:
        print("\n=== ALTERAR PRODUTO ===")

        produto = localizar_produto()

        if produto is None:
            print("\n1 - Tentar novamente")
            print("0 - Menu principal")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                continue

            elif opcao == "0":
                return

            else:
                print("Opção inválida!")

            continue

        print("\nProduto atual:")
        print(f"ID: {produto['id']}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")

        print("\nDeixe vazio para manter o valor atual.")

        novo_nome = input("Novo nome: ").strip()

        if novo_nome:
            nome_duplicado = False

            for outro in produtos:
                if (
                    outro["id"] != produto["id"]
                    and outro["nome"].lower() == novo_nome.lower()
                ):
                    nome_duplicado = True
                    break

            if nome_duplicado:
                print("Já existe outro produto com esse nome!")

            else:
                produto["nome"] = novo_nome

        novo_preco = input("Novo preço: ").strip()

        if novo_preco:
            try:
                novo_preco = float(novo_preco)

                if novo_preco <= 0:
                    print("O preço deve ser maior que zero!")
                    continue

                produto["preco"] = novo_preco

            except ValueError:
                print("Preço inválido!")
                continue

        nova_quantidade = input("Nova quantidade: ").strip()

        if nova_quantidade:
            try:
                nova_quantidade = int(nova_quantidade)

                if nova_quantidade < 0:
                    print("A quantidade não pode ser negativa!")
                    continue

                produto["quantidade"] = nova_quantidade

            except ValueError:
                print("Quantidade inválida!")
                continue

        salvar_dados()

        print("\nProduto alterado com sucesso!")

        print("\n1 - Alterar outro produto")
        print("0 - Menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            continue

        elif opcao == "0":
            return

        else:
            print("Opção inválida!")


def remover_produto():
    while True:
        print("\n=== REMOVER PRODUTO ===")

        produto = localizar_produto()

        if produto is None:
            print("\n1 - Tentar novamente")
            print("0 - Menu principal")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                continue

            elif opcao == "0":
                return

            else:
                print("Opção inválida!")

            continue

        print(f"\nID: {produto['id']}")
        print(f"Produto: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")

        confirmacao = input(
            "\nTem certeza que deseja remover? (s/n): "
        ).lower()

        if confirmacao != "s":
            print("Operação cancelada.")

        else:
            produtos.remove(produto)
            salvar_dados()

            print("Produto removido com sucesso!")

        print("\n1 - Remover outro produto")
        print("0 - Menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            continue

        elif opcao == "0":
            return

        else:
            print("Opção inválida!")


def entrada_estoque():
    while True:
        print("\n=== ENTRADA DE ESTOQUE ===")

        try:
            id_produto = int(input("ID do produto: "))

        except ValueError:
            print("Digite um ID válido!")
            continue

        produto = buscar_por_id(id_produto)

        if produto is None:
            print("Produto não encontrado!")
            continue

        try:
            quantidade = int(input("Quantidade de entrada: "))

        except ValueError:
            print("Digite uma quantidade válida!")
            continue

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero!")
            continue

        produto["quantidade"] += quantidade

        registrar_movimentacao(
            produto,
            "ENTRADA",
            quantidade
        )

        salvar_dados()

        print("\nEntrada registrada!")
        print(f"Produto: {produto['nome']}")
        print(f"Estoque atual: {produto['quantidade']}")

        print("\n1 - Registrar outra entrada")
        print("0 - Menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            continue

        elif opcao == "0":
            return

        else:
            print("Opção inválida!")


def saida_estoque():
    while True:
        print("\n=== SAÍDA DE ESTOQUE ===")

        try:
            id_produto = int(input("ID do produto: "))

        except ValueError:
            print("Digite um ID válido!")
            continue

        produto = buscar_por_id(id_produto)

        if produto is None:
            print("Produto não encontrado!")
            continue

        try:
            quantidade = int(input("Quantidade de saída: "))

        except ValueError:
            print("Digite uma quantidade válida!")
            continue

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero!")
            continue

        if quantidade > produto["quantidade"]:
            print(
                f"Estoque insuficiente! "
                f"Disponível: {produto['quantidade']}"
            )
            continue

        produto["quantidade"] -= quantidade

        registrar_movimentacao(
            produto,
            "SAÍDA",
            quantidade
        )

        salvar_dados()

        print("\nSaída registrada!")
        print(f"Produto: {produto['nome']}")
        print(f"Estoque atual: {produto['quantidade']}")

        print("\n1 - Registrar outra saída")
        print("0 - Menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            continue

        elif opcao == "0":
            return

        else:
            print("Opção inválida!")


def relatorios():
    while True:
        print("\n=== RELATÓRIOS ===")

        if not produtos:
            print("Nenhum produto cadastrado.")

        else:
            valor_total = sum(
                produto["preco"] * produto["quantidade"]
                for produto in produtos
            )

            quantidade_total = sum(
                produto["quantidade"]
                for produto in produtos
            )

            produto_mais_caro = max(
                produtos,
                key=lambda produto: produto["preco"]
            )

            maior_estoque = max(
                produtos,
                key=lambda produto: produto["quantidade"]
            )

            estoque_baixo = [
                produto
                for produto in produtos
                if 0 < produto["quantidade"] <= 5
            ]

            sem_estoque = [
                produto
                for produto in produtos
                if produto["quantidade"] == 0
            ]

            print(f"\nProdutos cadastrados: {len(produtos)}")
            print(f"Quantidade total: {quantidade_total}")
            print(f"Valor total: R$ {valor_total:.2f}")

            print("\nProduto mais caro:")
            print(
                f"{produto_mais_caro['nome']} - "
                f"R$ {produto_mais_caro['preco']:.2f}"
            )

            print("\nMaior quantidade em estoque:")
            print(
                f"{maior_estoque['nome']} - "
                f"{maior_estoque['quantidade']} unidades"
            )

            print("\n=== ESTOQUE BAIXO ===")

            if estoque_baixo:
                for produto in estoque_baixo:
                    print(
                        f"{produto['nome']} - "
                        f"{produto['quantidade']} unidades"
                    )

            else:
                print("Nenhum produto com estoque baixo.")

            print("\n=== SEM ESTOQUE ===")

            if sem_estoque:
                for produto in sem_estoque:
                    print(produto["nome"])

            else:
                print("Nenhum produto sem estoque.")

        print("\n0 - Menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            return

        print("Opção inválida!")


def mostrar_historico():
    while True:
        print("\n=== HISTÓRICO DE MOVIMENTAÇÕES ===")

        if not historico:
            print("Nenhuma movimentação registrada.")

        else:
            for movimento in reversed(historico):
                print("\n------------------------------")
                print(f"Data: {movimento['data']}")
                print(f"Produto: {movimento['produto']}")
                print(f"Tipo: {movimento['tipo']}")
                print(f"Quantidade: {movimento['quantidade']}")
                print(
                    f"Estoque atual: "
                    f"{movimento['estoque_atual']}"
                )

        print("\n0 - Menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            return

        print("Opção inválida!")


def menu():
    print("\n" + "=" * 45)
    print("          SISTEMA DE ESTOQUE")
    print("=" * 45)
    print("1 - Cadastro de produtos")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Alterar produto")
    print("5 - Remover produto")
    print("6 - Entrada de estoque")
    print("7 - Saída de estoque")
    print("8 - Relatórios")
    print("9 - Histórico")
    print("0 - Sair")
    print("=" * 45)


carregar_dados()


while True:
    menu()

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        menu_cadastro()

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        buscar_produto()

    elif opcao == "4":
        alterar_produto()

    elif opcao == "5":
        remover_produto()

    elif opcao == "6":
        entrada_estoque()

    elif opcao == "7":
        saida_estoque()

    elif opcao == "8":
        relatorios()

    elif opcao == "9":
        mostrar_historico()

    elif opcao == "0":
        salvar_dados()
        print("\nSistema encerrado!")
        break

    else:
        print("Opção inválida!")