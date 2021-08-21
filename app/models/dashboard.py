import dash
import dash_core_components as dcc
import dash_html_components as html
from .plotagem import cria_figura,cores_padrao

"""Nesse modulo será possivel criar um layout para a pagina  do dashboard"""


def init_dashboard(server):
    """Create a Plotly Dash dashboard como um servidor dash."""
    #Estilo css para a pagina
    external_stylesheets = ['../static/css/bootstrap.min.css']
    #App dash
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashboard/',
        external_stylesheets= external_stylesheets
    )
  
    #cores_padrão
    colors = cores_padrao()
    
    # Create Dash Layout
    #figura 01, primeiros 7 generos mais ouvidos
    trace1  = cria_figura()
  

    trace2 = cria_figura()   
    dash_app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Dashboard',
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ), html.H4(
        children='Vamos ver o que trás os dados de utilização da plataforms youtube e spotify.',
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: Confira dados do Mateus em 4 gráficos sobre youtube e spotify .',
             style={
        'textAlign': 'left',
        'color': colors['text']
    }),


    dcc.Graph(
        id='example-graph-1',
        figure=trace1 
    ),
    html.Div(children='Gráfico-02: Canais mais acessados.',
             style={
        'textAlign': 'left',
        'color': colors['text']
    }),


    dcc.Graph(
        id='example-graph-2',
        figure=trace2 
    )
,html.A(children='Voltar para inicio',
             href = "https://vizwebdash.herokuapp.com/"
    )])
    


    return dash_app.server