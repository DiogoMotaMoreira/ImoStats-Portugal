import sqlite3
import pandas as pd
from builtins import round



def valorMedioPrecoImovel(tipo, subtipo ,local):
    # Conectar à base de dados (cria o arquivo se ele não existir)
    conexao = sqlite3.connect('database/imoveis.db')

    # buscar media de preco de valores em imobiliario
    query = """
        SELECT AVG(preco)
        FROM imovel
        WHERE (? IS NULL OR tipo_imovel = ?)
        AND (? IS NULL OR sub_tipo_imovel = ?)
        AND (? IS NULL OR id_cidade = (
            SELECT id_cidade from cidade where nome = ?
        ))
    """
    cursor = conexao.execute(query, (tipo, tipo, subtipo, subtipo, local, local))
    valor = cursor.fetchone()[0]

    conexao.commit()

    conexao.close()
    return str(round(valor, 2)) if valor else '0'
 


def deltaValorMedioPrecoImovel(tipo, subtipo ,local):
    # Conectar à base de dados (cria o arquivo se ele não existir)
    conexao = sqlite3.connect('database/imoveis.db')

    # buscar media de preco de valores em imobiliario
    query = """
        SELECT AVG(preco)
        FROM imovel
        WHERE data_registo < DATE('now', '-1 month') 
        AND (? IS NULL OR tipo_imovel = ?)
        AND (? IS NULL OR sub_tipo_imovel = ?)
        AND (? IS NULL OR id_cidade = (
            SELECT id_cidade from cidade where nome  = ?
        ))
    """
    cursor = conexao.execute(query, (tipo, tipo, subtipo, subtipo, local, local))
    x1 = cursor.fetchone()[0]
    query = """
        SELECT AVG(preco)
        FROM imovel
        WHERE (? IS NULL OR tipo_imovel = ?)
        AND (? IS NULL OR sub_tipo_imovel = ?)
        AND (? IS NULL OR id_cidade = (
            SELECT id_cidade from cidade where nome  = ?
        ))
    """
    cursor = conexao.execute(query, (tipo, tipo, subtipo, subtipo, local, local))
    x2 = cursor.fetchone()[0]
    conexao.commit()

    x1 = x1 if x1 else '0'
    x2 = x2 if x2 else '0'


    valor = float(x1)-float(x2)

    conexao.close()
    return str(round(valor,2))

def valorMedioM2(tipo, subtipo ,local):
    conexao = sqlite3.connect('database/imoveis.db')


    query = """
        SELECT AVG(preco/area_m2)
        FROM imovel
        WHERE (? IS NULL OR tipo_imovel = ?)
        AND (? IS NULL OR sub_tipo_imovel = ?)
        AND (? IS NULL OR id_cidade = (
            SELECT id_cidade from cidade where nome  = ?
        ))
    """
    cursor = conexao.execute(query, (tipo, tipo, subtipo, subtipo, local, local))
    valor = cursor.fetchone()[0]
    conexao.commit()
    conexao.close()

    return str(round(valor,2)) if valor else '0'

def deltaValorMedioM2(tipo, subtipo ,local):
    conexao = sqlite3.connect('database/imoveis.db')


    query = """
        SELECT AVG(preco/area_m2)
        FROM imovel
        WHERE data_registo < DATE('now', '-1 month') 
        AND (? IS NULL OR tipo_imovel = ?)
        AND (? IS NULL OR sub_tipo_imovel = ?)
        AND (? IS NULL OR id_cidade = (
            SELECT id_cidade from cidade where nome  = ?
        ))
    """
    cursor = conexao.execute(query, (tipo, tipo, subtipo, subtipo, local, local))
    x1 = cursor.fetchone()[0]
    query = """
        SELECT AVG(preco/area_m2)
        FROM imovel
        WHERE (? IS NULL OR tipo_imovel = ?)
        AND (? IS NULL OR sub_tipo_imovel = ?)
        AND (? IS NULL OR id_cidade = (
            SELECT id_cidade from cidade where nome  = ?
        ))
    """
    cursor = conexao.execute(query, (tipo, tipo, subtipo, subtipo, local, local))
    x2 = cursor.fetchone()[0]
    conexao.commit()

    x1 = x1 if x1 else '0'
    x2 = x2 if x2 else '0'

    valor = float(x1)-float(x2)

    conexao.commit()
    conexao.close()
    return str(round(valor,2))


def tabelaPrecoDatas(tipo, subtipo ,local):
    conexao = sqlite3.connect('database/imoveis.db')
    cursor = conexao.cursor()

    query = """
        SELECT data_registo, preco FROM imovel
        WHERE (? IS NULL OR tipo_imovel = ?)
        AND (? IS NULL OR sub_tipo_imovel = ?)
        AND (? IS NULL OR id_cidade = (
            SELECT id_cidade from cidade where nome  = ?
        ))"""
    df = pd.read_sql_query(query, conexao, params=(tipo, tipo, subtipo, subtipo, local, local))

    conexao.commit()
    conexao.close()

    df["data_registo"] = pd.to_datetime(df["data_registo"])

    df = df.sort_values("data_registo")

    df.set_index("data_registo", inplace=True)
    
    # é preciso agrupar dados por mês para melhorar a visualização dos dados
    df_agrupado = df.resample('M').mean()

    df_agrupado = df_agrupado.interpolate(method='linear')

    return df_agrupado

def getCidades():
    conexao = sqlite3.connect('database/imoveis.db')
    cursor = conexao.cursor()

    query = "SELECT DISTINCT nome FROM cidade"
    df = pd.read_sql_query(query, conexao)

    conexao.commit()
    conexao.close()

    return df

def getTiposImovel():
    conexao = sqlite3.connect('database/imoveis.db')
    cursor = conexao.cursor()

    query = "SELECT DISTINCT tipo_imovel FROM imovel"
    df = pd.read_sql_query(query, conexao)

    conexao.commit()
    conexao.close()

    return df

def getSubTiposImovel(tipo):
    conexao = sqlite3.connect('database/imoveis.db')

    query = "SELECT DISTINCT sub_tipo_imovel FROM imovel WHERE tipo_imovel = ? ORDER BY sub_tipo_imovel"
    df = pd.read_sql_query(query, conexao, params=(tipo,))

    conexao.commit()
    conexao.close()

    return df