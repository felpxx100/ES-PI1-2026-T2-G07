from gerenciamento import pausar_e_limpar 

def cadastrar_candidato(cursor, conexao):

    print("\n--- CADASTRO DE NOVO CANDIDATO ---")
    nome = input("Nome do candidato: ")
    digito = input("Número de votação (dígito numérico): ")
    partido = input("Partido: ")

    cursor.execute(f"SELECT * FROM Candidatos WHERE digito_candidatos = '{digito}'")
    if len(cursor.fetchall()) > 0:
        print("\n[Erro] Já existe um candidato registado com este número.")
    else:
        cursor.execute("INSERT INTO Candidatos (digito_candidatos, nome_candidato, partido_candidatos) VALUES (%s, %s, %s)", (digito, nome, partido))
        conexao.commit()
        print(f"\n[Sucesso] Candidato {nome} cadastrado com o número {digito}!")

    pausar_e_limpar()

def editar_candidato(cursor, conexao):
     
    print("\n--- EDITAR DADOS DO CANDIDATO ---")
    digito = input("Digite o número do candidato que deseja editar: ")

    cursor.execute(f"SELECT nome_candidato, partido_candidatos FROM Candidatos WHERE digito_candidatos = '{digito}'")
    resultado = cursor.fetchall()

    if len(resultado) == 0:
        print("\n[Erro] Candidato não encontrado.")
    else:
        candidato = resultado[0]
        print(f"Dados atuais -> Nome: {candidato[0]} | Partido: {candidato[1]}")
        novo_nome = input("Novo nome (ou aperte ENTER para manter o mesmo): ")
        novo_partido = input("Novo partido (ou aperte ENTER para manter o mesmo): ")

        if novo_nome == "":
            novo_nome = candidato[0]
        if novo_partido == "":
            novo_partido = candidato[1]

        cursor.execute("UPDATE Candidatos SET nome_candidato = %s, partido_candidatos = %s WHERE digito_candidatos = %s", (novo_nome, novo_partido, digito))
        conexao.commit()
        print("\n[Sucesso] Dados do candidato atualizados!")

    pausar_e_limpar()
