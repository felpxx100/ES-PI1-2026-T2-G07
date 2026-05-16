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
