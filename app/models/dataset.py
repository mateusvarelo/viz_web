import pandas as pd

#Local dos arquivo
local_arquivo =  {
            'spotify':"./dataset/spotify/streamingspotify.csv",
            'youtube':"./dataset/youtube/visualizacao.csv"
}

#Função para ler arquivo csv e  retorna um dataframe, tipo de estrutura tabular que a biblioteca pandas entende.
def df_spotify_genero():
    #Busca arquivo e cria um dataframe com biblioteca pandas 
    df = pd.read_csv(local_arquivo['spotify'])
    
    #Generos mais ouvido no spotify
    df_genero = (
        df.groupby("genero",as_index=False).agg({'artistName_x':'count'})
    ).sort_values(by = 'artistName_x',ascending=False)
   
    #Após fazer agrupamento, apliquei uma ordenação que me trás o maisouvidode forma decrescente
    df_genero =  df_genero.set_index('genero').reset_index()    
    
    #Alterando coluna artistName_x para Count
    df_genero.rename({'artistName_x':'Quantidade'},axis=1,inplace=True)
    
    return df_genero.loc[0:6]#retorno do 7 primeiros registros

#Esta função tem como objetivo extrair dados do arquivo csv Spotify e devolver um df com dados relativos a melhores artista 
def df_spotify_artista():
     #Busca arquivo e cria um dataframe com biblioteca pandas 
     df = pd.read_csv(local_arquivo['spotify'])
     #Pegando apenas dados de artista por quantidade de música reproduzidas.
     df_artista =( 
                    df
                    .groupby('artistName_x',as_index=False)
                    .agg({'trackName':'count'})
        ).sort_values(by='trackName',ascending=False)
     #Após fazer agrupamento, apliquei uma ordenação que me trás o mais ouvidos de forma decrescente
     df_artista =  df_artista.set_index('artistName_x').reset_index()    
    
     #Alterando coluna trackName para Quantidade
     df_artista.rename({'trackName':'Quantidade','artistName_x':'Artista'},axis=1,inplace=True)
     return df_artista.loc[0:6]
