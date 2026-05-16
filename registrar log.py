import datetime
import random
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