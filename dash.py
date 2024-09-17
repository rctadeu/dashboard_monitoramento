import streamlit as st
from streamlit_option_menu import option_menu

from mapa_critico import mapacritico
from documentos import doc

# Configuração da página
st.set_page_config(
    page_title="Meu Dashboard",
    #page_icon=":bar_chart:",
    layout="wide"
)

# Configuração do menu de navegação
with st.sidebar:
    st.markdown(f"""
            <div style="font-size: 35px">Dashboard</div>
            """, unsafe_allow_html=True)
    st.write('fghdsgfhdjskh jfdhjfdhvhj vbvhdfhk')
    selected = option_menu(
        menu_title=None,  # Se quiser um título no menu, coloque aqui
        options=["Mapa Critico", "Estatisticas", "Documentos"],  # Opções do menu
        icons=["bar-chart", "bar-chart", "filetype-doc"],  # Ícones para as opções
        #menu_icon="cast",  # Ícone do menu
        default_index=0,  # Índice da opção selecionada por padrão
        styles={
            "container": {"padding": "5px", "background-color": "#262730"},
            "icon": {"color": "white", "font-size": "15px"},
            "nav-link": {"font-size": "12px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "gray"},
        }
    )

# Definir o conteúdo da página com base na seleção do menu
if selected == "Mapa Critico":
    mapacritico()
elif selected == "Estatisticas":
    st.title("Estatísticas por Sistema")
elif selected == "Documentos":
    doc()
