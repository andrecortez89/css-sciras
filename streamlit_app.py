import streamlit as st
import pandas as pd

# Set page config with a logo and theme colors
st.set_page_config(
    page_title="SCIRAS Hospitais Casa de Saúde",
    page_icon=":hospital:",
    layout="wide",
    menu_items={

    }
)

# Define theme for the app
primaryColor="#FF4B4B"
backgroundColor="#FFF8E1"
secondaryBackgroundColor="#F2E2CE"
textColor="#312F2F"
font="sans serif"

st.write('<style>table td:nth-child(1) {white-space: normal;}</style>', unsafe_allow_html=True)
st.image("data/logo.png", width=75)  # Adjust width as needed
st.title('Manuais SCIRAS Hospitais Casa de Saúde Santos e Praia Grande, SP')

def load_data():
    return pd.read_csv('data/profilaxia.csv')

def main():
    df = load_data()
    st.subheader('Consulta Rápida')
    st.subheader('Profilaxia Cirúrgica')
    st.write("A 1° dose de antimicrobiano deve ser administrada aproximadamente entre 30 minutos e 1h antes do início da cirurgia.")
    especialidades = df['Especialidade'].unique()
    especialidade_selection = st.multiselect('Especialidade', especialidades)

    if especialidade_selection:
        filtered_data = df[df['Especialidade'].isin(especialidade_selection)]
        st.markdown(filtered_data.to_html(escape=False, index=False), unsafe_allow_html=True)
    else:
        st.write("Selecione uma Especialidade para visualizar a padronização.")

    

    st.subheader('Manual de Prevenção de Infecções')
    st.write("Clique no link abaixo para abrir:")

    # URL or local path to your PDF file
    pdf_file_path = 'data/Manual de Prevenção de Infecções Relacionadas à Assistência a Saúde (IRAS) (1).pdf'

    try:
        with open(pdf_file_path, "rb") as pdf_file:
            btn = st.download_button(
                label="Manual  PDF",
                data=pdf_file,
                file_name="manual_sciras_css.pdf",
                mime="application/octet-stream"
            )
    except Exception as e:
        st.error(f"Error: {e}")



if __name__ == '__main__':
    main()
