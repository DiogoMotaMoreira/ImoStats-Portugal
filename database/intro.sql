

CREATE TABLE cidade(
    id_cidade INTEGER AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150)
);

CREATE TABLE imovel(
    id_imovel INTEGER AUTO_INCREMENT PRIMARY KEY,
    id_cidade INTEGER NOT NULL,
    tipo_imovel VARCHAR(50) NOT NULL,
    sub_tipo_imovel VARCHAR(50),
    preco DOUBLE(15 , 2) NOT NULL,
    area_m2 DOUBLE(8,2) NOT NULL,
    data_registo DATETIME NOT NULL, 
    FOREIGN KEY (id_cidade) REFERENCES cidade(id_cidade)
);