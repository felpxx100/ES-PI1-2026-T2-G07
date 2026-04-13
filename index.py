import mysql.connector

# Conecta no banco de dados 
try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",          # Usuario do banco
        password="",          # Senha do banco
        database="eleicao"    # Nome do banco
    )
    cursor = conexao.cursor()
    print("[Sistema: Conexão com banco de dados estabelecida com sucesso.]")
except mysql.connector.Error as err:
    print(f"[Erro: Não foi possível conectar ao banco de dados: {err}]")

##título do programa
el="Eleição"
print (f"{el:^90}\n")

# Variável de controle do menu principal
menup = 0

##menu principal
while menup != 3:
    print ("\n--- MENU PRINCIPAL ---")
    print ("Escolha a opção")
    menup=int(input(f"1- Módulo de gerenciamento\n2- Módulo de votação\n3- Sair\n"))

    match menup:
        ##menu de modulo de gerenciamento
        case 1:
            modulo_gere = 0
            while modulo_gere != 11:
                print("\n--- MÓDULO DE GERENCIAMENTO ---")
                print("Escolha uma opção")
                modulo_gere=int(input(f"1- Cadastra novo eleitor\n2- Editar dados do eleitor\n3- Remover eleitor\n4- Buscar eleitor\n5- Listar todos os eleitores\n6- Cadastrar novo candidato\n7- Editar dados do candidato\n8- Remover candidato\n9- Buscar candidato\n10- Listar todos os candidatos\n11- Voltar\n"))
                
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
                        busc=input(f"\nDigite o cpf do eleitor: ")
                        pass
                    case 5:
                        ##Lista todos os eleitores
                        pass
                    case 6:
                        ##adiciona novo candidato
                        pass
                    case 7:
                        ##edita dados dos candidatos
                        pass
                    case 8:
                        ##remove candidato
                        pass
                    case 9:
                        ##busca algum candidato
                        busc_cand=input(f"\nDigite o número do candidato: ")
                        pass
                    case 10:
                        ##Lista todos os candidatos
                        pass
                    case 11:
                        ##Saída do submenu
                        print("Voltando ao Menu Principal...")
                    case _:
                        print ("Opção inválida")

        case 2:
            modulo_vot = 0
            while modulo_vot != 4:
                print("\n--- MÓDULO DE VOTAÇÃO ---")
                print("Escolha uma opção")
                modulo_vot=int(input(f"1- Abrir Sistema de Votação\n2- Auditoria do Sistema de Votação\n3- Resultado da Votação\n4- Voltar\n"))
                
                match modulo_vot:
                    case 1:
                        ##submenu abrir sistema de votação 
                        print("\n--- Autenticação do Mesário ---")
                        tit_mesario=input(f"Digite o título de eleitor: ")
                        cpf_mesario=input(f"Digite os 4 primeiros dígitos do CPF: ")
                        chv_mesario=input(f"Digite a chave de acesso: ")
                        
                        ##fluxo da zerézima apenas visual
                        print("\n[ Sistema: Zerézima realizada com sucesso. ]")
                        
                        menu_urna = 0
                        ##menu de operação da urna
                        while menu_urna != 2:
                            print("\nEscolha a opção da Urna")
                            menu_urna=int(input(f"1- Votar\n2- Encerrar Sistema de Votação\n"))
                            
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
                        menu_auditoria = 0
                        while menu_auditoria != 3:
                            print("\n--- AUDITORIA DO SISTEMA ---")
                            menu_auditoria=int(input("1- Exibição de Logs de Ocorrências\n2- Exibição dos Protocolos de Votação\n3- Voltar\n"))
                            match menu_auditoria:
                                case 1:
                                    pass
                                case 2:
                                    pass
                                case 3:
                                    print("Voltando...")
                                case _:
                                    print("Opção inválida")
                                    
                    case 3:
                        ##resultado da votação
                        menu_resultados = 0
                        while menu_resultados != 5:
                            print("\n--- RESULTADO DA VOTAÇÃO ---")
                            menu_resultados=int(input("1- Boletim de Urna\n2- Estatística de Comparecimento\n3- Votos por Partido\n4- Validação de Integridade\n5- Voltar\n"))
                            match menu_resultados:
                                case 1:
                                    pass
                                case 2:
                                    pass
                                case 3:
                                    pass
                                case 4:
                                    pass
                                case 5:
                                    print("Voltando...")
                                case _:
                                    print("Opção inválida")
                                    
                    case 4:
                        ##saída do submenu
                        print("Voltando ao Menu Principal...")
                    case _:
                        print("Opção inválida")

        case 3:
            ##saída
            print("Saindo do sistema...")
        case _:
            print("Opção inválida")

# Fecha o banco de dados ao sair do programa
try:
    cursor.close()
    conexao.close()
except NameError:
    pass
