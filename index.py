##título do programa
el="Eleição"
print (f"{el:^90}\n")
##escolhendo opção do menu principal
print ("Escolha a opção")
menup=int(input(f"\n1- Módulo de gerenciamento\n2-Módulo de votação\n3- Sair\n"))

##menu principal
match menup:
    ##menu de modulo de gerenciamento
    case 1:
        print("Escolha uma opção")
        modulo_gere=int(input(f"\n1-Cadastra novo eleitor\n2- Editar dados do eleitor\n3- Remover eleitor\n4- Buscar eleitor\n5- Listar todos os eleitores\n6- Sair"))
        match modulo_gere:
            case 1:
                ##adiciona novo eleitor
                pass
            case 2:
                ##edita dados dos eleitores
                pass
            case 3:
                ##remove eleitor
                pass
            case 4:
                ##busca algum eleitor por cpf
                busc=input(f"\nDigite o cpf do eleitor:")
                pass
            case 5:
                ##Lista todos os eleitores
                pass
            case 6:
                ##Saída
                print("Saindo...")
            case _:
                print ("Opção inválida")

    case 2:
        pass
    case 3:
        ##saída
        print("Saindo...")
    case _:
        print("Opção inválida")