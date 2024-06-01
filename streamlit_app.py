import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
def load_data():
    # Load the CSV file
    # Adjust the file path if your environment requires it
    return pd.read_csv('data/profilaxia.csv')

def main():
    st.write('<style>table td:nth-child(1) {white-space: normal;}</style>', unsafe_allow_html=True)
    st.title('Profilaxia Cirúrgica SCIRAS HCSS & PG')
    
    # Load data
    df = load_data()

    # Optionally display the raw data

    # Filtering options directly in the main page
    st.subheader('Selecionar por Especialidade')
    
    # Get unique values from the 'Especialidade' column for filtering
    especialidades = df['Especialidade'].unique()
    especialidade_selection = st.multiselect('Especialidade', especialidades)

 
    if especialidade_selection:
        filtered_data = df[df['Especialidade'].isin(especialidade_selection)]
        # Converta DataFrame em HTML e aplique estilo CSS para quebrar texto
        st.markdown(filtered_data.to_html(escape=False, index=False), unsafe_allow_html=True)
    else:
        st.write("Selecione uma Especialidade para visualizar os dados.")
if __name__ == '__main__':
    main()