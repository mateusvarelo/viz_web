import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd



def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    external_stylesheets = ['/home/mateus/Repositorios/viz_web/app/static/css/bootstrap.min.css']
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashboard/',
        external_stylesheets= external_stylesheets
    )
    colors = {
    'background': '#F8F8FF',
    'text': '#111111'
}
    #create dataframe
    df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
    # Create Dash Layout
    #figura 01
    fig = px.bar(df, x="Fruit", y="Amount", barmode="relative")
    
    fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
    
    #figura 02
    fig2 = px.bar(df, x="Fruit", y="Amount", barmode="relative",title = 'Canais mais visualizados')
    fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
    
    dash_app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Dashboard',
        style={
            'textAlign': 'left',
            'color': colors['text']
        }
    ), html.H4(
        children='Melhores artistas',
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
        figure=fig
    ),
    html.Div(children='Gráfico-02: Canais mais acessados.',
             style={
        'textAlign': 'left',
        'color': colors['text']
    }),


    dcc.Graph(
        id='example-graph-2',
        figure=fig2
    )
,html.A(children='Voltar para inicio',
             href = "https://vizwebdash.herokuapp.com/"
    )])
    


    return dash_app.server