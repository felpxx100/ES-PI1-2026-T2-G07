import mysql.connector 
import os

# Conecta no banco de dados 
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eleicao"
)
cursor = conexao.cursor()

# Variável de controle de loop
opcao_relatorio = "0"

while opcao_relatorio != "6":
    print("\n--- MENU DE AUDITORIA E RESULTADOS ---")
    print("1 - Mostrar Logs")
    print("2 - Boletim de Urna")
    print("3 - Votos por Partido")
    print("4 - Total de Votos (Presença)")
    print("5 - Checar Fraude na Urna")
    print("6 - Sair")
    opcao_relatorio = input("Escolha uma opção: ")

    if opcao_relatorio == "1":
        print("\n--- LOGS ---")
        if os.path.exists("logs_urna.txt"):
            arquivo = open("logs_urna.txt", "r", encoding="utf-8")
            for linha in arquivo.readlines():
                print(linha, end="")
            arquivo.close()
        else:
            print("Nenhum log encontrado.")

    elif opcao_relatorio == "2":
        print("\n--- BOLETIM DE URNA ---")
        
        cursor.execute("SELECT digito_candidatos, nome_candidato FROM Candidatos")
        candidatos = cursor.fetchall()
        
        if len(candidatos) == 0:
            print("Nenhum candidato registrado.")
        else:
            vencedor_nome = ""
            maior_voto = -1
            
            for candidato in candidatos:
                digito = candidato[0]
                nome = candidato[1]
                
                # Conta votos de cada candidato um por um
                cursor.execute(f"SELECT COUNT(*) FROM Votos WHERE digito_candidato = {digito}")
                total_votos = cursor.fetchone()[0]
                
                print(f"Nome: {nome} | Número: {digito} | Votos: {total_votos}")
                
                if total_votos > maior_voto:
                    maior_voto = total_votos
                    vencedor_nome = nome
                    
            print(f"\nVencedor atual: {vencedor_nome} com {maior_voto} votos computados.")

    elif opcao_relatorio == "3":
        print("\n--- VOTOS POR PARTIDO ---")
        
        cursor.execute("SELECT partido_candidatos, digito_candidatos FROM Candidatos")
        candidatos = cursor.fetchall()
        
        partidos_nomes = []
        partidos_votos = []
        
        for candidato in candidatos:
            partido = candidato[0]
            digito = candidato[1]
            
            # Conta os votos pra este dígito
            cursor.execute(f"SELECT COUNT(*) FROM Votos WHERE digito_candidato = {digito}")
            votos = cursor.fetchone()[0]
            
            # Agrupa manualmente na lista
            achou = False
            for i in range(len(partidos_nomes)):
                if partidos_nomes[i] == partido:
                    partidos_votos[i] += votos
                    achou = True
            
            if not achou:
                partidos_nomes.append(partido)
                partidos_votos.append(votos)
        
        # Exibe os resultados agrupados
        for i in range(len(partidos_nomes)):
            print(f"Partido: {partidos_nomes[i]} | Votos Totais: {partidos_votos[i]}")

    elif opcao_relatorio == "4":
        print("\n--- PRESENÇA ---")
        cursor.execute("SELECT COUNT(*) FROM Eleitores")
        total_pessoas = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM Eleitores WHERE ja_votou = TRUE")
        votaram = cursor.fetchone()[0]
        
        if total_pessoas > 0:
            porcentagem = (votaram / total_pessoas) * 100
            print(f"Cadastrados: {total_pessoas}")
            print(f"Votaram: {votaram}")
            print(f"Presença: {porcentagem:.2f}%")
        else:
            print("Sem eleitores cadastrados.")

    elif opcao_relatorio == "5":
        print("\n--- CHECAGEM DA URNA ---")
        cursor.execute("SELECT COUNT(*) FROM Votos")
        votos_urna = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM Eleitores WHERE ja_votou = TRUE")
        assinaturas = cursor.fetchone()[0]
        
        print(f"Votos físicos contados na urna: {votos_urna}")
        print(f"Assinaturas de eleitores que votaram: {assinaturas}")
        
        if votos_urna == assinaturas:
            print("Tudo certo. Urna validada e íntegra.")
        elif votos_urna > assinaturas:
            print("Problema grave: Tem mais votos do que assinaturas de presença.")
        else:
            print("Problema grave: Mais pessoas assinaram do que votos depositados.")

    elif opcao_relatorio == "6":
        print("Saindo do relatório...")

    else:
        print("Opção inválida.")

cursor.close()
conexao.close()
