import os
import sqlite3
import json



# Inserir cidades na tabela
def inserirCidade(conexao, cidade ):
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO cidade (nome) VALUES (?)    
    ''', (cidade, ))



# Inserir imoveis na tabela
def inserirImoveis( conexao ,cidade, tipo_imovel, sub_tipo_imovel, preco, area_m2, data_registo):
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO imovel (
            id_cidade, tipo_imovel, sub_tipo_imovel, preco, area_m2, data_registo
        ) VALUES (?, ?, ?, ?, ?, ?)
    ''', (cidade, tipo_imovel, sub_tipo_imovel, preco, area_m2, data_registo))



def carregarDataBase():
    if not os.path.exists('database/imoveis.db'):
        # Conectar à base de dados (cria o arquivo se ele não existir)
        conexao = sqlite3.connect('database/imoveis.db')
        cursor = conexao.cursor()
        with open('database/intro.sql', 'r', encoding='utf-8') as f:
            script_sql = f.read()

        cursor.executescript(script_sql)

        # fazer leitura de datasets
        with open('dataset/cidades.json', "r", encoding="utf-8") as f:
            f.seek(0)
            cidades = json.load(f)
            

        for codigo, nome in cidades.items():
            inserirCidade(conexao , nome)

        with open('dataset/imoveis.json', "r", encoding="utf-8") as f:
            f.seek(0)
            imoveis = json.load(f)

        for imovel in imoveis:
            cidade = imovel.get('id_cidade')
            tipo = imovel.get('tipo_imovel')
            subtipo = imovel.get('sub_tipo_imovel')
            preco = imovel.get('preco')
            area = imovel.get('area_m2')
            data = imovel.get('data_registo')
            inserirImoveis( conexao, cidade, tipo, subtipo, preco, area, data)
        
        conexao.commit()
        conexao.close()
