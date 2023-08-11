import streamlit as st
import Controllers.ChamadoController as ChamadoController
import Pages.Chamados.Adicionar as PageAdicionarChamado

def ConsultarChamados():
    paramID = st.experimental_get_query_params()
    if paramID == {}: 
        colunas = st.columns((1, 2, 1, 1, 2, 1, 1))
        campos = ['Nº', 'Nome', 'Ambiente', 'Prioridade', 'Descrição', 'Excluir', 'Editar']
        for col, campo_nome in zip(colunas, campos):
            col.write(campo_nome)

        for item in ChamadoController.SelecionarTodos():
            col1, col2, col3, col4, col5, col6 = st.columns((1, 2, 1, 1, 2, 1, 1))
            col1.write(item.id)
            col2.write(item.name)
            col3.write(item.enviroment)
            col4.write(item.priority)
            col5.write(item.description)
            button_space_excluir = col6.empty()
            on_click_excluir = button_space_excluir.button('Excluir', 'btnExcluir' + str(item.id))
            button_space_editar = col7.empty()
            on_click_editar = button_space_editar.button('Editar', 'btnEditar' + str(item.id))

            if on_click_excluir:
                ChamadoController.Excluir(item.id)
                button_space_excluir.button('Excluído', 'btnExcluir' + str(item.id))

            if on_click_editar:
                st.experimental_set_query_params(
                    id=[item.id]
                )
                st.experimental_rerun()
    else:
        PageAdicionarChamado.AdicionarChamado()





    # caso quisesse utilizar a biblioteca pandas
    #import pandas as pd

    # st.title("Consultar chamados")

    # costumerList = []

    # for item in ChamadoController.SelecionarTodos():
    #     costumerList.append([item.name, item.enviroment, item.priority, item.description])

    # dataFrame = pd.DataFrame(
    #     costumerList,
    #     columns=['Name', 'Enviroment', 'Priority', 'Description']
    # )

    # st.table(dataFrame)