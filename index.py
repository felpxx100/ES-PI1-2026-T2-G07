import mysql.connector
import gerenciamento
import os

def pausar_e_limpar():
    """Pausa e limpa a tela no arquivo principal."""
    input("\n[ Pressione ENTER para continuar... ]")
    os.system('cls' if os.name == 'nt' else 'clear')

# Conecta no banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456", 
    database="eleicao"
)
cursor = conexao.cursor()
os.system('cls' if os.name == 'nt' else 'clear')
print("[Sistema: Conexão com banco de dados estabelecida com sucesso.]")

## título do programa
el="Eleição"
print(f"{el:^90}\n")
pausar_e_limpar()

# Variável de controle do menu principal
menup = 0

## menu principal
while menup != 3:
    print("\n--- MENU PRINCIPAL ---")
    print("Escolha a opção")
    menup = int(input("1- Módulo de gerenciamento\n2- Módulo de votação\n3- Sair\n"))
    os.system('cls' if os.name == 'nt' else 'clear')

    match menup:
        ## menu de modulo de gerenciamento
        case 1:
            modulo_gere = 0
            while modulo_gere != 11:
                print("\n--- MÓDULO DE GERENCIAMENTO ---")
                print("Escolha uma opção")
                modulo_gere = int(input("1- Cadastra novo eleitor\n2- Editar dados do eleitor\n3- Remover eleitor\n4- Buscar eleitor\n5- Listar todos os eleitores\n6- Cadastrar novo candidato\n7- Editar dados do candidato\n8- Remover candidato\n9- Buscar candidato\n10- Listar todos os candidatos\n11- Voltar\n"))
                os.system('cls' if os.name == 'nt' else 'clear')
                
                match modulo_gere:
                    case 1:
                        gerenciamento.cadastrar_eleitor(cursor, conexao)
                    case 2:
                        print("Função em desenvolvimento.")
                        pausar_e_limpar()
                    case 3:
                        print("Função em desenvolvimento.")
                        pausar_e_limpar()
                    case 4:
                        gerenciamento.buscar_eleitor(cursor)
                    case 5:
                        gerenciamento.listar_eleitores(cursor)
                    case 6:
                        print("Função em desenvolvimento.")
                        pausar_e_limpar()
                    case 7:
                        print("Função em desenvolvimento.")
                        pausar_e_limpar()
                    case 8:
                        print("Função em desenvolvimento.")
                        pausar_e_limpar()
                    case 9:
                        busc_cand = input("\nDigite o número do candidato: ")
                        print("Função em desenvolvimento.")
                        pausar_e_limpar()
                    case 10:
                        print("Função em desenvolvimento.")
                        pausar_e_limpar()
                    case 11:
                        print("Voltando ao Menu Principal...")
                        pausar_e_limpar()
                    case _:
                        print("Opção inválida")
                        pausar_e_limpar()

        case 2:
            modulo_vot = 0
            while modulo_vot != 4:
                print("\n--- MÓDULO DE VOTAÇÃO ---")
                print("Escolha uma opção")
                modulo_vot = int(input("1- Abrir Sistema de Votação\n2- Auditoria do Sistema de Votação\n3- Resultado da Votação\n4- Voltar\n"))
                os.system('cls' if os.name == 'nt' else 'clear')
                
                match modulo_vot:
                    case 1:
                        print("\n--- Autenticação do Mesário ---")
                        tit_mesario = input("Digite o título de eleitor: ")
                        cpf_mesario = input("Digite os 4 primeiros dígitos do CPF: ")
                        chv_mesario = input("Digite a chave de acesso: ")
                        
                        print("\n[ Sistema: Zerézima realizada com sucesso. ]")
                        pausar_e_limpar()
                        
                        menu_urna = 0
                        while menu_urna != 2:
                            print("\nEscolha a opção da Urna")
                            menu_urna = int(input("1- Votar\n2- Encerrar Sistema de Votação\n"))
                            os.system('cls' if os.name == 'nt' else 'clear')
                            
                            match menu_urna:
                                case 1:
                                    print("\n--- Identificação do Eleitor ---")
                                    tit_eleitor = input("Digite o título de eleitor: ")
                                    cpf_eleitor = input("Digite os 4 primeiros dígitos do CPF: ")
                                    chv_eleitor = input("Digite a chave de acesso: ")
                                    
                                    num_cand = input("\nDigite o número do candidato: ")
                                    print("\n[ Sistema: Voto registrado! ]")
                                    pausar_e_limpar()
                                case 2:
                                    print("\n--- Autenticação para Encerramento ---")
                                    tit_mesario_enc = input("Digite o título de eleitor do mesário: ")
                                    cpf_mesario_enc = input("Digite os 4 primeiros dígitos do CPF: ")
                                    chv_mesario_enc = input("Digite a chave de acesso: ")
                                    
                                    confirma = input("\nDeseja realmente encerrar a votação? (Sim/Não): ")
                                    print("\n[ Sistema: Votação Encerrada. ]")
                                    pausar_e_limpar()
                                case _:
                                    print("Opção inválida")
                                    pausar_e_limpar()
                    
                    case 2:
                        menu_auditoria = 0
                        while menu_auditoria != 3:
                            print("\n--- AUDITORIA DO SISTEMA ---")
                            menu_auditoria = int(input("1- Exibição de Logs de Ocorrências\n2- Exibição dos Protocolos de Votação\n3- Voltar\n"))
                            os.system('cls' if os.name == 'nt' else 'clear')
                            match menu_auditoria:
                                case 1: 
                                    print("Função em desenvolvimento.")
                                    pausar_e_limpar()
                                case 2: 
                                    print("Função em desenvolvimento.")
                                    pausar_e_limpar()
                                case 3: 
                                    print("Voltando...")
                                case _: 
                                    print("Opção inválida")
                                    pausar_e_limpar()
                                    
                    case 3:
                        menu_resultados = 0
                        while menu_resultados != 5:
                            print("\n--- RESULTADO DA VOTAÇÃO ---")
                            menu_resultados = int(input("1- Boletim de Urna\n2- Estatística de Comparecimento\n3- Votos por Partido\n4- Validação de Integridade\n5- Voltar\n"))
                            os.system('cls' if os.name == 'nt' else 'clear')
                            match menu_resultados:
                                case 1: 
                                    print("Função em desenvolvimento.")
                                    pausar_e_limpar()
                                case 2: 
                                    print("Função em desenvolvimento.")
                                    pausar_e_limpar()
                                case 3: 
                                    print("Função em desenvolvimento.")
                                    pausar_e_limpar()
                                case 4: 
                                    print("Função em desenvolvimento.")
                                    pausar_e_limpar()
                                case 5: 
                                    print("Voltando...")
                                case _: 
                                    print("Opção inválida")
                                    pausar_e_limpar()
                                    
                    case 4:
                        print("Voltando ao Menu Principal...")
                        pausar_e_limpar()
                    case _:
                        print("Opção inválida")
                        pausar_e_limpar()

        case 3:
            print("Saindo do sistema...")
        case _:
            print("Opção inválida")
            pausar_e_limpar()

cursor.close()
conexao.close()