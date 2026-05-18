import datetime
import datetime
import random
# Importando a função que você já criou no outro arquivo!
from gerenciamento import pausar_e_limpar 
def registrar_log(mensagem):
 
    #Regista um evento no ficheiro de log da urna com a data e hora exatas.
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Abre o ficheiro em modo de adição ("a" - append)
    arquivo = open("logs_urna.txt", "a", encoding="utf-8")
    arquivo.write(f"[{agora}] {mensagem}\n")
    arquivo.close()

def validar_credenciais(cursor, titulo, cpf_4_digitos, chave, perfil_exigido):
    # Verifica no banco de dados se as credenciais inseridas estão corretas.
    cursor.execute(f"SELECT CPF_Eleitor, mesario FROM Eleitores WHERE titulo_eleitoral = '{titulo}' AND chave_acesso = '{chave}'")
    resultado = cursor.fetchall()
    
    if len(resultado) > 0:
        cpf_banco = resultado[0][0]
        e_mesario = resultado[0][1]
        
        # Verifica se os 4 primeiros dígitos correspondem
        if cpf_banco[0:4] == cpf_4_digitos:
            if perfil_exigido == "mesario" and e_mesario == 1:
                return True
            elif perfil_exigido == "eleitor":
                return True
                
    return False

def abrir_votacao(conexao, cursor):
    """
    Efetua a autenticação do mesário, executa a Zerézima e abre a urna.

    Args:
        conexao (mysql.connector.connection.MySQLConnection): A conexão atual com o banco de dados.
        cursor (mysql.connector.cursor.MySQLCursor): O cursor para execução de comandos SQL.

    Returns:
        bool: Retorna True se a votação foi aberta com sucesso, False em caso de falha na validação.
    """
    print("\n--- ABERTURA DO SISTEMA DE VOTAÇÃO ---")
    titulo = input("Digite o título de eleitor do mesário: ")
    cpf_4 = input("Digite os 4 primeiros dígitos do CPF: ")
    chave = input("Digite a chave de acesso: ")

    # Validação das credenciais do mesário antes de iniciar a Zerézima
    if validar_credenciais(cursor, titulo, cpf_4, chave, "mesario") == False:
        print("\n[Erro] Falha na validação do mesário. Acesso negado.")
        registrar_log("ALERTA: Tentativa de acesso negado")
        pausar_e_limpar()
        return False

    # Processo de Zerézima: Limpa votos anteriores e reseta status dos eleitores
    cursor.execute("DELETE FROM Votos")
    cursor.execute("UPDATE Eleitores SET ja_votou = FALSE")
    conexao.commit()
    
    print("\n--- ZERÉZIMA CONCLUÍDA ---")
    # Consulta a lista de candidatos para exibir o total zerado
    cursor.execute("SELECT digito_candidatos, nome_candidato FROM Candidatos")
    candidatos = cursor.fetchall()
    
    if len(candidatos) > 0:
        for cand in candidatos:
            print(f"Candidato: {cand[1]} | Número: {cand[0]} | Votos: 0")
    else:
        print("Nenhum candidato registado na base de dados.")

    # Registo oficial da abertura no ficheiro de logs
    registrar_log("ABERTURA: Votação iniciada com sucesso. Total de votos zerado.")
    print("\n[Sistema] Votação aberta com sucesso!")
    pausar_e_limpar()
    return True
