import streamlit as st
import Controllers.ChamadoController as ChamadoController
import models.Chamado as chamado

def AdicionarChamado():
    idAlteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        st.title("Alterar chamado")
    else:
        st.title("Abrir chamado")
    
    with st.form(key="include_chamado"):
        input_name = st.text_input(label="Insira seu nome")
        input_enviroment = st.radio("Selecione o ambiente:", ("Homol", "Sandbox", "Produção"))
        input_priority = st.radio("Selecione a prioridade do chamado:", ("Baixa", "Média", "Alta"))
        input_description = st.text_input(label="Descreva o problema")
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        # st.write(f'Nome: {input_name}')
        # st.write(f'Ambiente: {input_enviroment}')
        # st.write(f'Prioridade: {input_priority}')
        # st.write(f'Descrição: {input_describe}')
        # chamado.name = input_name
        # chamado.enviroment = input_enviroment
        # chamado.priority = input_priority
        # chamado.description = input_description

        ChamadoController.IncluirChamado(chamado.Chamado(0, input_name, input_enviroment, input_priority, input_description))
        st.success("Chamado aberto com sucesso")