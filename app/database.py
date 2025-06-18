import sqlite3

# Inserir cidades na tabela
def inserirCidade(cidade ):
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO cidade (nome) VALUES (?)    
    ''', (cidade))

    conexao.commit()
    conexao.close()

# Inserir imoveis na tabela
def inserirImoveis(cidade, tipo_imovel, sub_tipo_imovel, preco, area_m2, data_registo):
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO imovel (id_cidade, tipo_imovel, sub_tipo_imovel,preco, area_m2, data_registo) VALUES (?, ?, ?, ?, ?, ?)
    ''', (cidade, tipo_imovel, sub_tipo_imovel,preco, area_m2, data_registo))

    conexao.commit()
    conexao.close()



# Conectar à base de dados (cria o arquivo se ele não existir)
conexao = sqlite3.connect('imoveis.db')

# fazer leitura de datasets




