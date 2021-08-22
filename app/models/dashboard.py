import dash
import dash_core_components as dcc
import dash_html_components as html


from .plotagem import cria_fig_vertical_barra,cores_padrao,cria_fig_horizontal_barra,cria_grafico_linha_youtube

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
    #Gráfico de barra ertical com dados de genêros, primeiros 7 generos mais ouvidos
    fig_bar_vertical  = cria_fig_vertical_barra()
  

    fig_barh_horizontal = cria_fig_horizontal_barra()  
    
    
    fig_line_youtube = cria_grafico_linha_youtube()
    
    dash_app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Dashboard',
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ), html.H4(
        children='Vamos ver o que diz os dados de utilização das plataformas youtube e spotify sobre Mateus :).',
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash:Confira dados do Mateus em 3 gráficos.',
             style={
        'textAlign': 'left',
        'color': colors['text']
    }),
    html.Div(children='Gráfico-01: Classificados em order decrescente, gêneros preferidos do Mateus na plataforma SPOTIFY.O FORRÓ está em primeiro lugar.',
             style={
        'textAlign': 'left',
        'color': colors['text']
    })
   ,
    dcc.Graph(
        id='example-graph-1',
        figure=fig_barh_horizontal
    ),
    html.Div(children='Gráfico-02: Artistas preferidos :).',
             style={
        'textAlign': 'left',
        'color': colors['text']
    }),


    dcc.Graph(
        id='example-graph-2',
        figure=fig_bar_vertical 
    ),
    dcc.Graph(
        id='example-graph-',
        figure=fig_line_youtube
    ),
    html.A(children='Voltar para início',
             href = "https://vizwebdash.herokuapp.com/"
    ),
    
  ]
    )
    


    return dash_app.server