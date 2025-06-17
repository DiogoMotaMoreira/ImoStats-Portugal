

CREATE TABLE cidade(
    id_cidade INTEGER AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150)
);

CREATE TABLE imovel(
    id_imovel INTEGER AUTO_INCREMENT PRIMARY KEY,
    id_cidade INTEGER NOT NULL,
    tipo_imovel VARCHAR(150) NOT NULL,
    preco DOUBLE(15 , 2) NOT NULL,
    area_m2 DOUBLE(8,2) NOT NULL,
    data_registo DATETIME NOT NULL, 
    FOREIGN KEY (id_cidade) REFERENCES cidade(id_cidade)
);