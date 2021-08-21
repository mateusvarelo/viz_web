from .dataset import df_spotify
import plotly.express as px

#Cores padões
def cores_padrao():
        colors = {
        'background': '#F8F8FF',
        'text': '#111111'
        }
        return colors    

#Criação de figuras, ou melhor dos gráficos que serão lançados no layout do app dash
def layout_update(obj_update):
    colors = cores_padrao()    
    layout = obj_update.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
    return layout  

def cria_figura():
     #figura 01, primeiros 7 generos mais 
     #Busca  dataframe para plotar gráfico do spotify e cria a figura 
     df = df_spotify()
     trace1  = px.bar(
                 df, 
                 x="genero", 
                 y="Quantidade",
                 barmode="relative",
                 text = 'Quantidade',
                 opacity=.8,
               )
     #Atualiza cores gráfico 1
     layout_update(trace1)
     return trace1


