
import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
 
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import gunicorn
load_figure_template("minty")

app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])
server = app.server

data = pd.read_csv("supermarket_sales.csv")
data.info()
data["City"].value_counts().index
# Tranforme the column into datetime
data["Date"] = pd.to_datetime(data["Date"])


#============================================= Layout =======================================

app.layout =  html.Div(children=[
                 dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            html.H2("RBlack", style={"font-family": "Voltaire", "font-size": "60px"}),
                            html.Hr(),

                            html.H5("Cities:"),
                            dcc.Checklist(data["City"].value_counts().index,
                            data["City"].value_counts().index, id="check_city",
                            inputStyle={"margin-right": "5px", "margin-left": "20px"}),
                            html.Hr(),
                            html.H5("Analysis Variable"),
                            dcc.RadioItems(["gross income", "Rating"], "gross income", id="main_variable",
                            inputStyle={"margin-right": "5px", "margin-left": "20px"}),

                        ], style={"height":"90vh", "margin":"20px", "padding":"20px"})

                    ], sm=2),

                    dbc.Col([
                        dbc.Row([
                            dbc.Col([dcc.Graph(id="city_fig"),],sm=4),
                            dbc.Col([dcc.Graph(id="gender_fig"),],sm=4),
                            dbc.Col([dcc.Graph(id="pay_fig"),],sm=4)
                        ]),
                        dbc.Row([dcc.Graph(id="income_per_date_fig")]),
                        dbc.Row([dcc.Graph(id="income_per_product_fig")])

                    ], sm=10)

                ])
            
            ]

        )


#============================================= Callbacks =======================================
@app.callback([
                Output("city_fig", "figure"),
                Output("gender_fig", "figure"),
                Output("pay_fig", "figure"),
                Output("income_per_date_fig", "figure"),
                Output("income_per_product_fig", "figure")

            ],

                [
                    Input("check_city", "value"),
                    Input("main_variable", "value")

                ])

def render_graph(cities, main_variable):

    operation = np.sum if main_variable == "gross income" else np.mean
    data_filtered = data[data["City"].isin(cities)]
    data_city = data_filtered.groupby("City")[main_variable].apply(operation).to_frame().reset_index()
    data_gender = data_filtered.groupby(["Gender", "City"])[main_variable].apply(operation).to_frame().reset_index()
    data_payment = data_filtered.groupby("Payment")[main_variable].apply(operation).to_frame().reset_index()
    data_product_time = data_filtered.groupby("Date")[main_variable].apply(operation).to_frame().reset_index()
    data_product_income = data_filtered.groupby(["Product line", "City"])[main_variable].apply(operation).to_frame().reset_index()

    fig_city = px.bar(data_city, x="City", y=main_variable)
    fig_payment = px.bar(data_payment, y="Payment", x=main_variable, orientation="h")
    fig_gender = px.bar(data_gender, y=main_variable,x="Gender", color="City",barmode="group")
    fig_product_income = px.bar(data_product_income, x= main_variable, y="Product line", color="City", orientation="h", barmode="group")
    fig_product_date = px.bar(data_product_time, y= main_variable, x="Date")

    for fig in [fig_city,fig_payment,fig_gender,fig_product_date]:
        fig.update_layout(margin=dict(l=0,r=0,t=20,b=20),height=200, template="minty")
    
    fig_product_income.update_layout(margin=dict(l=0,r=0,t=20,b=20),height=500)
    
    return fig_city, fig_gender, fig_payment,  fig_product_date, fig_product_income 


#============================================= Run Server =======================================

if __name__ == "__main__":
    app.run_server(debug=False)






