# pip install streamlit
# streamlit hello

from os import write
from numpy.core.fromnumeric import size
import streamlit as st
import Controllers.ChamadoController as ChamadoController
import pandas as pd
import Pages.Chamados.Adicionar as PageAdicionarChamado
import Pages.Chamados.Consultar as PageConsultarChamado

st.title("Sistema de abertura de chamados")
st.header("Sistema de abertura de chamados")

st.sidebar.title("Menu")
page_chamado = st.sidebar.selectbox("Chamados", ["Adicionar", "Consultar"])

if page_chamado == "Consultar":
    PageConsultarChamado.ConsultarChamados()

if page_chamado == "Adicionar": 
    PageAdicionarChamado.AdicionarChamado()


