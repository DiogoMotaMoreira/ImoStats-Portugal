import streamlit as st
import pandas as pd


from database import carregarDataBase
from utils import *



st.markdown("# ImoStats")
st.markdown("### Dashboard público de custos de vida imobiliário em Portugal")

if 'db_loaded' not in st.session_state:
    carregarDataBase()
    st.session_state['db_loaded'] = True

# opções de dados
op1, op2, op3 = st.columns(3)

option1 = op1.selectbox(
    "Seleciona a cidade",
    (getCidades()),
    index=None
)

option2 = op2.selectbox(
    "Seleciona o tipo de Imóvel",
    (getTiposImovel()),
    index=None
)

if option2:
    df = getSubTiposImovel(option2)
    if df.iloc[0,0]!='':
        option3 = op3.selectbox(
            "Seleciona o subtipo de Imóvel",
            (df),
            index=None
        )
    else: option3 = None
else: option3 = None





# Motrar variações de preços atualmente se está a sub ou descer
col1,col2 = st.columns(2)
col1.metric(label="Preço médio Imovel em Portugal", value=valorMedioPrecoImovel(option2, option3, option1)+ "€", delta=deltaValorMedioPrecoImovel(option2, option3, option1), delta_color="inverse", border=True)
col2.metric(label="Preço médio M^2 em Portugal", value=valorMedioM2(option2, option3, option1) + "€", delta=deltaValorMedioM2(option2, option3, option1), delta_color="inverse", border=True)


# Gráfico de variação de preços ao longo do tempo
df = tabelaPrecoDatas(option2, option3, option1) 
st.line_chart(df)




st.markdown("**Nota:** Os dados introduzidos não são realistas, são gerados aleatoriamente!")

st.markdown("""
            ---
            # Sobre o Projeto
            ### Objetivo do Projeto
            O ImoStats Portugal foi desenvolvido para fornecer um dashboard público e acessível que apresenta uma análise atualizada dos custos de vida relacionados com o mercado imobiliário em Portugal. O objetivo é facilitar a compreensão das tendências de preços de imóveis por cidade, tipo e subtipo, ajudando compradores, investidores e curiosos a tomar decisões informadas.
            ### Fontes de dados
            Os dados utilizados neste projeto são gerados automaticamente por um script sem qualquer direcionamento para o mercado real.
            Os dados são processados e tratados para garantir a qualidade e a relevância das informações apresentadas.
            ### Tecnologias utilizadas
            Este projeto foi desenvolvido com Python, utilizando bibliotecas como Pandas para análise de dados e Streamlit para a criação da interface web interativa. A base de dados é gerida com SQLite para armazenamento local eficiente. O código está disponível para consulta e contribuições.
            
""")