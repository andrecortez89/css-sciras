import streamlit as st
import pandas as pd

def load_data():
    # Load the CSV file
    # Adjust the file path if your environment requires it
    return pd.read_csv('data/profilaxia.csv')

def main():
    st.title('Profilaxia Cirúrgica SCIRAS HCSS & PG')
    
    # Load data
    df = load_data()

    # Optionally display the raw data

    # Filtering options directly in the main page
    st.subheader('Selecionar por Especialidade')
    
    # Get unique values from the 'Especialidade' column for filtering
    especialidades = df['Especialidade'].unique()
    especialidade_selection = st.multiselect('Especialidade', especialidades)

    # Display filtered data
    if especialidade_selection:
        filtered_data = df[df['Especialidade'].isin(especialidade_selection)]
        st.dataframe(filtered_data)  # Using st.dataframe for better formatting
    else:
        st.write("Selecione a Especialidade para visualizar.")

if __name__ == '__main__':
    main()