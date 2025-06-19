import random
import json
from datetime import datetime, timedelta

# Lista de tipos de imóveis
tipos_imovel = ['Moradia Isolada', 'Moradia em Banda', 'Moradia Germinada', 'Apartamentos', 'Quintas e Herdades', 'Armazéns', 'Garagens', 'Lojas', 'Terrenos']
subtipos_imovel =['T0', 'T1', 'T2', 'T3', 'T4']


with open('ImoStats-Portugal/dataset/cidades.json', "r", encoding="utf-8") as f:
    cidades = json.load(f)


# Função para gerar uma data aleatória
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Datas entre 2015 e hoje
start_date = datetime(2015, 1, 1)
end_date = datetime.now()

def asSubType(tipo):
    types = ['Moradia Isolada', 'Moradia em Banda', 'Moradia Germinada', 'Apartamentos', 'Quintas e Herdades']
    return types.__contains__(tipo)

# Gerar os imóveis
imoveis = []
for i in range(1, 5001):
    tipo =  random.choice(tipos_imovel)
    if asSubType(tipo): subtipo = random.choice(subtipos_imovel)
    else: subtipo = ''
    # fazer uma função pra verificar se é moradia, quinta ou apartamento pra por o subtipo
    imovel = {
        "id_imovel": i,
        "id_cidade": random.randint(1, 73),
        "tipo_imovel": tipo,
        "sub_tipo_imovel": subtipo,
        "preco": round(random.uniform(30000, 1000000), 2),
        "area_m2": round(random.uniform(30, 500), 2),
        "data_registo": random_date(start_date, end_date).strftime("%Y-%m-%d %H:%M:%S")
    }
    imoveis.append(imovel)

# Exportar para JSON
with open("ImoStats-Portugal/dataset/imoveis.json", "w", encoding="utf-8") as f:
    json.dump(imoveis, f, ensure_ascii=False, indent=2)
