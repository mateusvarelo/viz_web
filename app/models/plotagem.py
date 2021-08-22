"""Cria gráficos a partir dos dados do df"""
import plotly.express as px
import plotly.graph_objects as go

from .dataset import df_spotify_genero,df_spotify_artista,df_youtube_view_meses


"""Cria dict com cores padões para ser usado no gráfico e no layout do dash"""
def cores_padrao():
        colors = {
        'background': '#FFFAFA',
        'text': '#000000'
        }
        return colors   

"""Função para atualizar as cores das figuras, com um padrão de cores"""
def layout_update(obj_update):
    colors = cores_padrao()    
    
    """Atualiza o layout"""
    layout = obj_update.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
    return layout  

"""Cria um gráfico de barra horizontal com dados do dataframe!"""
def cria_fig_horizontal_barra():
     """Primeiros 7 gêneros mais ouvidos """
     
     """Busca  dataframe para plotar gráfico do spotify e cria a figura"""
     df = df_spotify_genero()
     
     """Cria figura a parti do dados do df"""
     fig = go.Figure(go.Bar(
            x=df["Quantidade"],
            y=df["genero"],
             marker=dict(
             color='#32CD32',
            line=dict(color='#2E8B57', width=1)
    ),
            orientation='h'))
     """Chamada da função para atualizar layout """
     layout_update(fig)
     return fig
    


 

"""Criação do gráfico de barra vertical, com dados do dataframe.""" 
def cria_fig_vertical_barra():
     
     """Busca  dataframe para plotar gráfico do spotify."""
     df = df_spotify_artista()
     
     """Cria figura"""
     fig = go.Figure(go.Bar(
            x=df["Artista"],
            y=df["Quantidade"],
             marker=dict(
             color='#32CD32',
            line=dict(color='#2E8B57', width=1)
    ),
            orientation='v'))
     
     """Atualiza layout gráfico""" 
     layout_update(fig)
     
     return fig

"""Cria gráfico de linha a parti do dados do df youtube"""
def cria_grafico_linha_youtube():
        df = df_youtube_view_meses()
        fig =go.Figure(go.Scatter(
                    x = df['mes'],
                    y = df['qtd'],
                    mode = 'lines',
                    name = 'Quantidade')
        )
        return fig
