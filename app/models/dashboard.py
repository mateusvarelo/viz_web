import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd



def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashboard/',
        external_stylesheets= external_stylesheets
    )
    #create dataframe
    df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
    # Create Dash Layout
    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    
    dash_app.layout = html.Div(id='dash-container',
                               children=[
    html.H1(children='DASHBOARD-MATEUS'),

    html.Div(children='''
        Dash: Confira dados do Mateus em 4 gráficos sobre youtube e spotify .
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

    return dash_app.server