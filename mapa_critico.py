import streamlit as st

def mapacritico():
    # Função para definir a cor do status
    def get_status_color(value):
        if value > 40:
            return 'Tomato', 'Critico'
        elif value > 30:
            return 'Gold', 'Atencao'
        else:
            return 'MediumSeaGreen', 'Normal'

    # Simulação de valores para cada sistema
    system_values = {
        'Sistema 1': 30,
        'Sistema 2': 42,
        'Sistema 3': 10,
        'Sistema 4': 35,
        'Sistema 5': 20,
        'Sistema 6': 20,
        'Sistema 7': 15,
        'Sistema 8': 20,
        'Sistema 9': 36,
        'Sistema 10': 20,
        'Sistema 11': 20,
        'Sistema 12': 20,
        'Sistema 13': 31,
        'Sistema 14': 42,
        'Sistema 15': 10,
        'Sistema 16': 35,
        'Sistema 17': 20,
        'Sistema 18': 20,
    }

    # Criação das colunas
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    st.markdown("<br>", unsafe_allow_html=True)
    col7, col8, col9, col10, col11, col12 = st.columns(6)
    st.markdown("<br>", unsafe_allow_html=True)
    col13, col14, col15, col16, col17, col18 = st.columns(6)

    # Função para exibir o status em uma coluna
    def display_status(column, system, value):
        color, status = get_status_color(value)
        with column:
            st.markdown(f"""
            <div style="
            background-color: {color}; 
            padding: 2px; 
            color: white; 
            height: 100px; 
            width: 140px; 
            align-items: center; 
            justify-content: center;
            ">
                <h5><center>{system}</center></h5>
                <center>{status}</center>
            </div>
            """, unsafe_allow_html=True)

    # Exibir os status nas colunas

    display_status(col1, 'Sistema 1', system_values['Sistema 1'])
    display_status(col2, 'Sistema 2', system_values['Sistema 2'])
    display_status(col3, 'Sistema 3', system_values['Sistema 3'])
    display_status(col4, 'Sistema 4', system_values['Sistema 4'])
    display_status(col5, 'Sistema 5', system_values['Sistema 5'])
    display_status(col6, 'Sistema 6', system_values['Sistema 6'])

    display_status(col7, 'Sistema 7', system_values['Sistema 7'])
    display_status(col8, 'Sistema 8', system_values['Sistema 8'])
    display_status(col9, 'Sistema 9', system_values['Sistema 9'])
    display_status(col10, 'Sistema 10', system_values['Sistema 10'])
    display_status(col11, 'Sistema 11', system_values['Sistema 11'])
    display_status(col12, 'Sistema 12', system_values['Sistema 12'])

    display_status(col13, 'Sistema 13', system_values['Sistema 13'])
    display_status(col14, 'Sistema 14', system_values['Sistema 14'])
    display_status(col15, 'Sistema 15', system_values['Sistema 15'])
    display_status(col16, 'Sistema 16', system_values['Sistema 16'])
    display_status(col17, 'Sistema 17', system_values['Sistema 17'])
    display_status(col18, 'Sistema 18', system_values['Sistema 18'])
