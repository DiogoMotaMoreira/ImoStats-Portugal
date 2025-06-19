import sqlite3



def valorMedioPrecoImovel(tipo):
    # Conectar à base de dados (cria o arquivo se ele não existir)
    conexao = sqlite3.connect('database/imoveis.db')

    cursor = conexao.cursor()
    # buscar media de preco de valores em imobiliario
    if tipo :
        valor = 0

    else:
        cursor.execute('''
            SELECT AVG(preco) from imovel;
        ''')
        valor = cursor.fetchone()

        conexao.commit()

    conexao.close()
    return "{:.2f}".format(float(valor[0]))
 


def deltaValorMedioPrecoImovel(tipo):
    # Conectar à base de dados (cria o arquivo se ele não existir)
    conexao = sqlite3.connect('database/imoveis.db')

    cursor = conexao.cursor()
    # buscar media de preco de valores em imobiliario
    if tipo :
        valor = 0

    else:
        cursor.execute('''
            SELECT AVG(preco) FROM imovel 
            WHERE data_registo < DATE('now', '-7 days')
        ''')
        x1 = cursor.fetchone()
        cursor.execute('''
            SELECT AVG(preco) from imovel;
        ''')
        x2 = cursor.fetchone()
        conexao.commit()

        valor = float(x1[0])-float(x2[0])

    conexao.close()
    return "{:.2f}".format(valor)

def valorMedioM2():
    conexao = sqlite3.connect('database/imoveis.db')

    cursor = conexao.cursor()

    cursor.execute('''
        SELECT AVG(preco/area_m2) from imovel;
    ''')
    valor = cursor.fetchone()
    conexao.commit()
    conexao.close()

    return "{:.2f}".format(float(valor[0]))

def deltaValorMedioM2():
    conexao = sqlite3.connect('database/imoveis.db')

    cursor = conexao.cursor()

    cursor.execute('''
        SELECT AVG(preco/area_m2) from imovel 
        WHERE data_registo < DATE('now', '-7 days')
    ''')
    x1 = cursor.fetchone()
    cursor.execute('''
        SELECT AVG(preco/area_m2) from imovel;
    ''')
    x2 = cursor.fetchone()
    conexao.commit()

    valor = float(x1[0])-float(x2[0])

    conexao.commit()
    conexao.close()
    return "{:.2f}".format(valor)

    
    