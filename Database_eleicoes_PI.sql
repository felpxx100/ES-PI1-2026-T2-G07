-- Cria o banco de dados se não existir e o seleciona
CREATE DATABASE IF NOT EXISTS eleicao;
USE eleicao;

-- Limpa as tabelas caso já existam 
DROP TABLE IF EXISTS Votos;
DROP TABLE IF EXISTS Eleitores;
DROP TABLE IF EXISTS Candidatos;

-- Criação da Tabela de Eleitores
CREATE TABLE Eleitores(
    id_eleitor INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    titulo_eleitoral VARCHAR(12) NOT NULL UNIQUE, -- UNIQUE para evitar duplicidade 
    nome_eleitor VARCHAR(100) NOT NULL,
    CPF_Eleitor VARCHAR(11) NOT NULL UNIQUE,      -- UNIQUE para evitar duplicidade 
    mesario BOOLEAN NOT NULL DEFAULT FALSE,       -- Indica se é mesário 
    chave_acesso VARCHAR(50) NOT NULL,            -- Chave gerada no cadastro 
    ja_votou BOOLEAN NOT NULL DEFAULT FALSE       -- Controle para evitar voto duplo 
    FOREIGN KEY id_votos REFERENCES Votos(id_votos) -- Chave Estrangeira para identificar o voto
);

-- Criação da Tabela de Candidatos
CREATE TABLE Candidatos(
    id_candidatos INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    digito_candidatos INT(2) NOT NULL UNIQUE,     -- UNIQUE para evitar números iguais 
    nome_candidato VARCHAR(100) NOT NULL,
    partido_candidatos VARCHAR(100) NOT NULL
    FOREIGN KEY id_eleitor REFERENCES Eleitores(id_eleitor) -- Chave Estrangeira para identificar os Eleitores
);

-- Criação da Tabela de Votos 
CREATE TABLE Votos(
    id_voto INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    digito_candidato INT(2) NOT NULL,
    data_hora DATETIME NOT NULL,                  -- Armazena data e hora exatas do voto
    protocolo VARCHAR(50) NOT NULL UNIQUE         -- Comprovante de votação
    FOREIGN KEY id_candidatos REFERENCES Candidatos(id_candidatos) -- Chave Estrangeira para identificar os candidatos
    FOREIGN KEY id_eleitor REFERENCES Eleitores(id_eleitor) -- Chave Estrangeira para identificar os Eleitores
);





-- Inserindo Candidatos Fictícios
INSERT INTO Candidatos (digito_candidatos, nome_candidato, partido_candidatos) VALUES 
(10, 'Alan Turing', 'PDC (Partido da Computação)'),
(20, 'Ada Lovelace', 'PAL (Partido dos Algoritmos)'),
(30, 'Grace Hopper', 'PBD (Partido do Banco de Dados)'),
(99, 'Voto Nulo/Branco', 'Sem Partido');

-- Inserindo Eleitores Fictícios 
INSERT INTO Eleitores (titulo_eleitoral, nome_eleitor, endereco_eleitor, CPF_Eleitor, dt_nascimento, chave_acesso, ja_votou) VALUES 
('004356870906', 'Ana Pereira', 'Rua das Flores, 123', '12345678909', '1990-05-15', TRUE, 'ANPE1234', FALSE),   -- TRUE = Esta é a mesária
('102385010671', 'Carlos Mendes', 'Avenida Central, 45', '98765432100', '1985-10-20', FALSE, 'CAME5678', FALSE), -- FALSE = Eleitor comum
('203496120782', 'Beatriz Souza', 'Praça da Luz, 8', '45612378900', '2000-01-30', FALSE, 'BESO9012', FALSE);
