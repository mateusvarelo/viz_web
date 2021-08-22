"""Leitura e retorno de um df pandas"""
import pandas as pd

"""Local dos arquivo"""
local_arquivo =  {
            'spotify':"./dataset/spotify/streamingspotify.csv",
            'youtube':"./dataset/youtube/visualizacao.csv"
}

"""Funções para ler arquivo csv e  retorna um dataframe pronto para plotar gráficos, tipo de estrutura tabular que a biblioteca pandas entende e a plotly."""

"""Função para alterar nome da coluna do df"""
def altera_coluna_nome(df,antigo_nome,novo_nome):
    df.rename({antigo_nome:novo_nome},axis = 1,inplace=True)
    return df

"""Lendo csv spotify"""
def df_spotify_genero():
    """Busca arquivo e cria um dataframe com biblioteca pandas """
    df = pd.read_csv(local_arquivo['spotify'])
    
    """Generos mais ouvido no spotify"""
    df_genero = (
        df.groupby("genero",as_index=False).agg({'artistName_x':'count'})
    ).sort_values(by = 'artistName_x',ascending=False)
   
    """Após fazer agrupamento, apliquei uma ordenação que me trás o maisouvidode forma decrescente"""
    df_genero =  df_genero.set_index('genero').reset_index()    
    
    """Alterando coluna artistName_x para Count"""
    df_genero = altera_coluna_nome(df_genero,'artistName_x','Quantidade')
    
    return df_genero.loc[0:6]#retorno do 7 primeiros registros

"""Esta função tem como objetivo extrair dados do arquivo csv Spotify e devolver um df com dados relativos a melhores artista """
def df_spotify_artista():
     
     """Busca arquivo e cria um dataframe com biblioteca pandas """
     df = pd.read_csv(local_arquivo['spotify'])
     
     """Filtrando apenas dados de artista por quantidade de música reproduzidas."""
     df_artista =( 
                    df
                    .groupby('artistName_x',as_index=False)
                    .agg({'trackName':'count'})
        ).sort_values(by='trackName',ascending=False)
     
     """Após fazer agrupamento, apliquei uma ordenação que me trás o mais ouvidos de forma decrescente"""
     df_artista =  df_artista.set_index('artistName_x').reset_index()    
    
     """Alterando coluna trackName para Quantidade e artistName_x para Artista"""
     df_artista = altera_coluna_nome(df_artista,'trackName','Quantidade') 
     df_artista = altera_coluna_nome(df_artista,'artistName_x','Artista')
     
     return df_artista.loc[0:6]

"""Limpa dados do dataframe, altera data, aplica nome ao mês etc."""
def aplica_limpeza_df(df):
    import calendar
    """Converter para tipo datetime """
    df['data_visualizacao'] =pd.to_datetime(df['data_visualizacao'])
    
    """Busca o número do mês"""
    df['mes'] = df['data_visualizacao'].dt.month
    
    """Agrupa por mês  e quantidade de visualização"""
    df = df.groupby('mes',as_index=False).agg({'nome_video':'count'})
    
    """Altera nome de colunas"""
    df = altera_coluna_nome(df,'nome_video','qtd')
    
    """Ordena por número do mês"""
    df.sort_values(by = 'mes',inplace=True)
    
    """Aplica nome para mês após organizado"""
    df['mes'] = df['mes'].apply(lambda x:calendar.month_name[x])
    
    return df
 
"""Função para buscar dado do csv do youtube e retorna um df tratado, pronto para plotar um gráfico"""
def df_youtube_view_meses():
     df = pd.read_csv(local_arquivo['youtube'])
     df = aplica_limpeza_df(df)
     return df



