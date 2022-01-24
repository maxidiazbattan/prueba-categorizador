import pandas as pd
import pickle, gzip, pickletools, joblib
import streamlit as st 


def load_mappings():
    mapps = joblib.load('rf_rep_ya_model.joblib')
    return mapps

mapps = load_mappings()

mapp = mapps['integer_mapping']
familias = mapps['familias']
marcas = mapps['marcas']

filepath = "random_forest.pkl"
with gzip.open(filepath, 'rb') as f:
    p = pickle.Unpickler(f)
    model = p.load()


def prediction(data):

    df = data.copy()

    if 'categoria' in df.columns:
        missing_target_values = df[df['categoria'].isna()].index
        df = df.drop(missing_target_values, axis = 0).reset_index(drop=True)

        df = df[['id', 'familia', 'marca']].dropna(axis = 0).reset_index(drop=True)
        #array = df.values
    else:
        df = df[['id', 'familia', 'marca']].dropna(axis = 0).reset_index(drop=True)
        #array = df.values

    prediction=model.predict(df)
    
    preds = list()

    for p in prediction:
        for k, v in mapp.items():
            if v == p:
                preds.append(k)

    preds = pd.Series(preds, name='predicciones')
    df = pd.concat([df,preds], axis=1)

    dicc_map = dict(df['predicciones'].value_counts())
    df['predictions_rep'] = df['predicciones'].map(dicc_map)
    df['categorización manual'] = df['predictions_rep'].apply(lambda x: 'Si' if x < 25 else 'No')
    
    df = df[['id', 'familia', 'marca', 'predicciones', 'categorización manual']]

    return df

@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')

def main():
    
    html_temp = """
    <div style="background-color:tomato;padding:10px;border-radius: 5px;">
    <h2 style="color:white;text-align:center;">Categorizador RepuestosYa</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    file = st.file_uploader('', type=['csv'])
    show_file = st.empty()

    if not file:
        show_file.info('Por favor sube un archivo ' + ','.join(['csv']) )
        return

    data = pd.read_csv(file)
    st.subheader('Muestra del archivo')
    st.dataframe(data.sample(5))
    file.close()
   
    result=""
    if st.button("Predecir"):
        
        with st.spinner('Espere un momento...'):
            result=prediction(data)
        st.success('Listo!')
        
        st.subheader('Muestra del archivo')
        st.dataframe(result.sample(5))

        csv = convert_df(result)
        st.download_button("Descargar archivo",
                           csv,
                           "predicciones.csv",
                           "text/csv",
                           key='download-csv')

if __name__=='__main__':
    main()
