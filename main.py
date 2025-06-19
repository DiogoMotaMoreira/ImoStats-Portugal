import streamlit as st

from database import carregarDataBase
from utils import *



st.markdown("# ImoStats")
st.markdown("### Dashboard público de custos de vida imobiliário em Portugal")

carregarDataBase()


# Motrar variações de preços attualmente se está a sub ou descer
# calcular preço médio de mercado -> value
# calcular a variação -> delta
col1,col2, col3 = st.columns(3)

col1.metric(label="Preço médio Imovel em Portugal", value=valorMedioPrecoImovel(None)+ "€", delta=deltaValorMedioPrecoImovel(None), delta_color="inverse", border=True)

col2.metric(label="Preço médio M^2 em Portugal", value=valorMedioM2() + "€", delta=deltaValorMedioM2(), delta_color="inverse", border=True)

