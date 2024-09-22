import os
import pandas as pd

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

def extract():
    print('==> EXTRACT')
    df_tratada = ''
    return df_tratada

def transform(df_data):
    print('==> TRANSFORM')
    df_resultado = ''
    return df_resultado

def load(df_data):
    print('==> LOAD')
    pass

if __name__ == '__main__':
    # Extraccion
    df_extracted = extract()

    # Transformacion
    df_transformed = transform(df_extracted)

    # Carga
    load(df_transformed)