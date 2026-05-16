import mysql.connector

def conectar():

# Conecta no banco de dados
    conexao = mysql.connector.connect(
    host="BD-ACD",
    user="BD250226131",
    password="Bemjw8", 
    database="BD250226131"
)
    return conexao