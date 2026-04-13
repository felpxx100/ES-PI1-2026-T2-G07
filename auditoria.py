import mysql.connector 
import os

# Conecta no banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",          # Usuario do banco
    password="",          # Senha do banco
    database="eleicao"    # Nome do banco
)
cursor = conexao.cursor()

# Variável de controle
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
        # Abre o arquivo de texto e mostra na tela
        if os.path.exists("logs_urna.txt"):
            arquivo = open("logs_urna.txt", "r", encoding="utf-8")
            for linha in arquivo.readlines():
                print(linha, end="")
            arquivo.close()
        else:
            print("Nenhum log encontrado.")

    elif opcao_relatorio == "2":
        print("\n--- BOLETIM DE URNA ---")
        # Puxa os candidatos e conta os votos de cada um
        sql = """
            SELECT Candidatos.nome_candidato, Candidatos.digito_candidatos, COUNT(Votos.id_voto) as total
            FROM Candidatos
            LEFT JOIN Votos ON Candidatos.digito_candidatos = Votos.digito_candidato
            GROUP BY Candidatos.nome_candidato, Candidatos.digito_candidatos
            ORDER BY total DESC;
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        
        if len(resultados) == 0:
            print("Nenhum voto registrado.")
        else:
            for candidato in resultados:
                print(f"Nome: {candidato[0]} | Número: {candidato[1]} | Votos: {candidato[2]}")
            print(f"\nVencedor atual: {resultados[0][0]}")

    elif opcao_relatorio == "3":
        print("\n--- VOTOS POR PARTIDO ---")
        # Conta os votos agrupando pelo partido
        sql = """
            SELECT Candidatos.partido_candidatos, COUNT(Votos.id_voto) as total
            FROM Candidatos
            JOIN Votos ON Candidatos.digito_candidatos = Votos.digito_candidato
            GROUP BY Candidatos.partido_candidatos
            ORDER BY total DESC;
        """
        cursor.execute(sql)
        for partido in cursor.fetchall():
            print(f"Partido: {partido[0]} | Votos: {partido[1]}")

    elif opcao_relatorio == "4":
        print("\n--- PRESENÇA ---")
        # Pega total de eleitores
        cursor.execute("SELECT COUNT(*) FROM Eleitores;")
        total_pessoas = cursor.fetchone()[0]
        
        # Pega total de votos confirmados
        cursor.execute("SELECT COUNT(*) FROM Eleitores WHERE ja_votou = TRUE;")
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
        # Conta votos fisicos na urna
        cursor.execute("SELECT COUNT(*) FROM Votos;")
        votos_urna = cursor.fetchone()[0]
        
        # Conta pessoas que assinaram a lista
        cursor.execute("SELECT COUNT(*) FROM Eleitores WHERE ja_votou = TRUE;")
        assinaturas = cursor.fetchone()[0]
        
        print(f"Votos na urna: {votos_urna}")
        print(f"Assinaturas: {assinaturas}")
        
        if votos_urna == assinaturas:
            print("Tudo certo. Urna validada.")
        elif votos_urna > assinaturas:
            print("Problema: Tem mais voto do que gente que votou.")
        else:
            print("Problema: Alguém assinou e não votou.")

    elif opcao_relatorio == "6":
        print("Saindo do relatório...")

    else:
        print("Opção inválida.")

# Fecha o banco de dados
cursor.close()
conexao.close()
