import mysql.connector

def conectar():

# Conecta no banco de dados
    conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456", 
    database="eleicao"
)
    return conexao