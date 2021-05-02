import pandas as pd
import numpy as np

url = 'https://www.datos.gov.co/resource/gt2j-8ykr.json?$limit=2000'
df = pd.read_json(url)

def df_to_html(df):
    return df.to_html()


def get_date_limits(df):
    return [df['fecha_reporte_web'].iloc[0], df['fecha_reporte_web'].iloc[-1]]


def get_df_html():
    return df_to_html(get_df())


def get_df():
    return df


def query_estado_general():
    return df_to_html(df['estado'].value_counts().to_frame())


def query_estado_por_departamento():
    return df_to_html(df.groupby('departamento_nom')['estado'].value_counts().to_frame())


def query_pais_viajado_por_departamento():
    return df_to_html(df.groupby(['departamento_nom', 'pais_viajo_1_nom'])
                      ['estado'].count().to_frame())


def query_estado_general_departamento(departamento):
    return df_to_html(df['estado'][df['departamento_nom'] == str(departamento)].value_counts().to_frame())


def get_tipo_contagio():
    return df['fuente_tipo_contagio'].value_counts().index.values.tolist()


def query_tipo_de_contagio_en_departamento(tipo_contagio, departamento):
    return df[(df['fuente_tipo_contagio'] == tipo_contagio) &
              (df['departamento_nom'] == departamento)].shape[0]


def query_tipo_de_contagio_por_departamento(tipo_contagio):
    return df_to_html(df[df['fuente_tipo_contagio'] == tipo_contagio].groupby(['departamento_nom'])[
        'fuente_tipo_contagio'].count().to_frame())

 