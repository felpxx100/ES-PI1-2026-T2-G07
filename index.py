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
        print("Escolha uma opção")
        modulo_vot=int(input(f"\n1- Abrir Sistema de Votação\n2- Auditoria do Sistema de Votação\n3- Resultado da Votação\n4- Sair\n"))
        match modulo_vot:
            case 1:
                ##submenu abrir sistema de votação 
                print("\n--- Autenticação do Mesário ---")
                tit_mesario=input(f"Digite o título de eleitor: ")
                cpf_mesario=input(f"Digite os 4 primeiros dígitos do CPF: ")
                chv_mesario=input(f"Digite a chave de acesso: ")
                
                ##fluxo da zerézima apenas visual
                print("\n[ Sistema: Zerézima realizada com sucesso. ]")
                
                ##menu de operação da urna
                print("\nEscolha a opção da Urna")
                menu_urna=int(input(f"\n1- Votar\n2- Encerrar Sistema de Votação\n"))
                
                match menu_urna:
                    case 1:
                        ##votar
                        print("\n--- Identificação do Eleitor ---")
                        tit_eleitor=input(f"Digite o título de eleitor: ")
                        cpf_eleitor=input(f"Digite os 4 primeiros dígitos do CPF: ")
                        chv_eleitor=input(f"Digite a chave de acesso: ")
                        
                        num_cand=input(f"\nDigite o número do candidato: ")
                        print("\n[ Sistema: Voto registrado! ]")
                        pass
                    case 2:
                        ##encerrar sistema de votação
                        print("\n--- Autenticação para Encerramento ---")
                        tit_mesario_enc=input(f"Digite o título de eleitor do mesário: ")
                        cpf_mesario_enc=input(f"Digite os 4 primeiros dígitos do CPF: ")
                        chv_mesario_enc=input(f"Digite a chave de acesso: ")
                        
                        confirma=input(f"\nDeseja realmente encerrar a votação? (Sim/Não): ")
                        print("\n[ Sistema: Votação Encerrada. ]")
                        pass
                    case _:
                        print("Opção inválida")
            case 2:
                ##auditoria do sistema de votação 
                pass
            case 3:
                ##resultado da votação
                pass
            case 4:
                ##saída
                print("Saindo...")
            case _:
                print("Opção inválida")

    case 3:
        ##saída
        print("Saindo...")
    case _:
        print("Opção inválida")