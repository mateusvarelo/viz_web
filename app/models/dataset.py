import pandas as pd

local_arquivo =  {
            'spotify':"/home/mateus/Repositorios/viz_web/dataset/spotify/streamingspotify.csv",
            'youtube':"/home/mateus/Repositorios/viz_web/dataset/youtube/visualizacao.csv"
}
df = pd.read_csv(local_arquivo['spotify'])
print(df.head())
    