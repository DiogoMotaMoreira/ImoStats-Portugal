

CREATE TABLE cidade(
    id_cidade INTEGER  PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(150)
);

CREATE TABLE imovel (
    id_imovel INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cidade INTEGER NOT NULL,
    tipo_imovel TEXT NOT NULL,
    sub_tipo_imovel TEXT,
    preco REAL NOT NULL,
    area_m2 REAL NOT NULL,
    data_registo DATETIME NOT NULL,
    FOREIGN KEY (id_cidade) REFERENCES cidade(id_cidade)
);
