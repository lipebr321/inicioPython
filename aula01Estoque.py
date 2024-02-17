estoque = {
    100:{
        "descricao":"Placa de vídeo GTX 1660 ti",
        "valor": 950.00,
        "marca": "Gygabyte confia"
       },
    200:{
        "descricao":"Fone Wireless",
        "valor": 50.00,
        "marca": "Sonya"
       },
    300:{
        "descricao":"Carregador Tipo c 100 w",
        "valor": 100.00,
        "marca": "Semsunga"
       } 
}

opcoes = ("1", "2", "3", "4", "0")

def menu():
    print("Digite a opção desejada:")
    print("1 - Listar itens")
    print("2 - Incluir item")
    print("3 - Excluir item")
    print("4 - Editar item")
    print("0 - Sair")
    opcao = input()
    while opcao not in opcoes:
        print("Opção inválida!")
        opcao = input("Digite a opção desejada: ")
    return opcao


def listar():
    for item in estoque.keys():
        print(f"{item} - {estoque[item]['descricao']} - {estoque[item]['marca']} - R$ {estoque[item]['valor']}")

def incluirEditar():
    codigo = int(input("Qual código deseja? "))
    while codigo in estoque:
        opcao = input("Código já cadastrado. Deseja editar o item? (S/N) ").lower()
        if opcao == "s":
            break
        else:
            codigo = input("Digite outro código: ")

    descricao = input("Qual descrição do item? ")
    valor = float(input("Qual valor do item? "))
    marca = input("Qual marca do item? ")

    estoque[codigo] = {
        "descricao":descricao,
        "valor": valor,
        "marca": marca}
    
    listar()

def excluir():
    listar()
    codigo = int(input("Qual código deseja remover?"))
    estoque.pop(codigo)
    print(f"Item de código: {codigo} removido!")
    listar()





print("Bem vindo ao AquiExpress")

while True:
    opcao = menu()

    if opcao == "1":
        listar()
    elif opcao == "2":
        incluirEditar()
    elif opcao == "3":
        excluir()
    elif opcao == "4":
        incluirEditar()
    else:
        quit()