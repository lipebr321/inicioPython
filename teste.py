minha_lista = []

while True:
    entrada_usuario = input("Digite um item para adicionar à lista (ou 'sair' para encerrar): ")

    if entrada_usuario.lower() == 'sair':
        break

    minha_lista.append(entrada_usuario)

    escolha = input("Deseja cadastrar outro item (digite 's' para sim ou 'n' para não)? ")

    if escolha.lower() != 's':
        break


for lista in minha_lista:
 print(lista)
