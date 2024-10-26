import json


def adicionar_contato(lista_contatos, nome: str, telefone: str, email: str, favorito: str = "Não") -> None:
    contato = {"Nome": nome, "Telefone": telefone, "Email": email, "Favorito": favorito}

    lista_contatos.append(contato)

    with open('contatos.json', 'w') as arquivo:
        json.dump(lista_contatos, arquivo, indent=4)

    print(f"Contato {nome} adicionado com sucesso!")


def visualizar_contatos(lista_contatos):
    indice = 1

    for contato in lista_contatos:
        print(
            f"{indice} - Nome: {contato["Nome"]} - Telefone: {contato['Telefone']} - Email: {contato['Email']} - "
            f"Favorito: {contato['Favorito']}"
        )
        indice += 1


def editar_contato(lista_contato, indice, alteracao, item_alterado):
    indice_ajustado = ajustar_indice_contato(indice)
    lista_contato[indice_ajustado][alteracao] = item_alterado

    with open('contatos.json', 'w') as arquivo:
        json.dump(lista_contato, arquivo, indent=4)

    print("Contato alterado com sucesso!")


def favoritar_contato(lista_contato, indice):
    indice_ajustado = ajustar_indice_contato(indice)

    if lista_contato[indice_ajustado]["Favorito"] == "Nao":
        lista_contato[indice_ajustado]["Favorito"] = "Sim"
        print(f"Contato {lista_contato[indice_ajustado]["Nome"]} favoritado com sucesso!")
    else:
        lista_contato[indice_ajustado]["Favorito"] = "Nao"
        print(f"Contato {lista_contato[indice_ajustado]["Nome"]} retirado dos favoritos!")

    with open('contatos.json', 'w') as arquivo:
        json.dump(lista_contato, arquivo, indent=4)


def deletar_contato(lista_contato, indice):
    indice_ajustado = ajustar_indice_contato(indice)
    lista_contato.pop(indice_ajustado)

    with open('contatos.json', 'w') as arquivo:
        json.dump(lista_contato, arquivo, indent=4)


def exibir_favoritos(lista_contatos) -> None:
    for contato in lista_contatos:
        if contato["Favorito"] == "Sim":
            print(
                f"Nome: {contato["Nome"]} - Telefone: {contato['Telefone']} - Email: {contato['Email']} - "
                f"Favorito: {contato['Favorito']}"
            )


def ajustar_indice_contato(indice):
    return int(indice) - 1


def main():
    try:
        with open('contatos.json', 'r') as arquivo:
            lista_contatos = json.load(arquivo)
    except FileNotFoundError:
        lista_contatos = []
        with open('contatos.json', 'w') as arquivo:
            json.dump(lista_contatos, arquivo, indent=4)

    while True:
        print(
            "\nSelecione uma das opções: "
            "\n1 - Visualizar contatos"
            "\n2 - Adicionar contatos"
            "\n3 - Editar contatos"
            "\n4 - Favoritar contato"
            "\n5 - Exibir favoritos"
            "\n6 - Deletar contato"
            "\n7 - Sair"
        )

        escolha = input("\nDigite a sua escolha: ")

        if escolha == "1":
            visualizar_contatos(lista_contatos)
        elif escolha == "2":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            email = input("Digite o email do contato: ")
            adicionar_contato(lista_contatos, nome, telefone, email)
        elif escolha == "3":
            indice = input("Digite o número do contato a ser alterado: ")
            alteracao = input("Digite o que deseja alterar: Nome, Telefone ou Email: ")
            item_alterado = input(f"Digite o novo {alteracao} do contato: ")
            editar_contato(lista_contatos, indice, alteracao, item_alterado)
        elif escolha == "4":
            indice = input("Digite o número do contato a ser favoritado: ")
            favoritar_contato(lista_contatos, indice)
        elif escolha == "5":
            exibir_favoritos(lista_contatos)
        elif escolha == "6":
            indice = input("Digite o número do contato a ser excluído: ")
            deletar_contato(lista_contatos, indice)
        elif escolha == "7":
            break


if __name__ == "__main__":
    main()
