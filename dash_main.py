from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import math

df = pd.read_csv('nor_pop_2.csv', sep=";")
df['kommune'] = df['region'].map(lambda x: " ".join(x.split(' ')[1:]))

app = Dash()
server = app.server

app.layout = [
    html.H1(children='Prosjektert befolkningsvekst i Norske kommuner',
            style={'textAlign': 'center'}),
    dcc.Dropdown(sorted(df.kommune.unique()),
                 'Bergen', id='dropdown-selection'),
    dcc.Graph(id='graph-content'),
    html.Div(id='drag-info', style={'marginTop': 20, 'fontSize': 16})
]


@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.kommune == value]
    fig = px.line(dff, x='år', y='Hovedalternativet (MMMM)')

    # Enable box select mode for dragging
    fig.update_layout(
        dragmode='select',  # or 'lasso' for freeform selection
        selectdirection='h'  # 'h' for horizontal, 'v' for vertical, 'any' for both
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)
