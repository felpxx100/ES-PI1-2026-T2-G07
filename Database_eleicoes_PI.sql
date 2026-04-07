CREATE TABLE Eleitores(
id_eleitor INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
titulo_eleitoral VARCHAR(12) NOT NULL,
nome_eleitor VARCHAR(100) NOT NULL,
endereco_eleitor VARCHAR(100) NOT NULL,
CPF_Eleitor VARCHAR(11) NOT NULL,
dt_nascimento DATE NOT NULL,
email_eleitor VARCHAR(50) NOT NULL
)


CREATE TABLE Candidatos(
id_candidatos INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
digito_candidatos INT(02) NOT NULL,
nome_candidato VARCHAR(100),
partido_candidatos VARCHAR(100)
)  


