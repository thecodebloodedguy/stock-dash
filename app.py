import dash 
from dash import dcc
from dash import html
from datetime import datetime as dt
import pandas as pd
import numpy as np
import plotly.express as px
import base64
app=dash.Dash(__name__)
server=app.server
imgfile=r'\assests\Best-Stocks.jpeg'
with open(imgfile, "rb") as image_file:
    img_data = base64.b64encode(image_file.read())
    img_data = img_data.decode()
    logo_img = "{}{}".format("data:image/jpg;base64, ", img_data)
app.head = [html.Link(rel='stylesheet', href='assets/stylesheet.css')]
app.layout=html.Div(children=
    [
        html.Div(children=
          [
            html.P("Welcome to Stonks!", className="start"),
            html.Div(children=[
              #Stock Code
              html.Label("Stock Code:"),
              dcc.Input(id='code',type='text'),
              html.Button('Submit',id='sub',value='submit')

            ]),
            html.Div(children=[
              # Date range picker input
                html.Label(
                    'Start Date'
                ),
                dcc.DatePickerRange(id='dat')
            ]),
            html.Div(children=[
              # Stock price button
              html.Button('Stock Price',id='stp'),
              # Indicators button
              html.Button('Indicators',id='sti'),
              # Number of days of forecast input
              html.Br(),
              dcc.Input('Number of Days',type='text',id='stn'),
              # Forecast button
              html.Button('Forecast',id='stf')

            ]),
          ],
        className="nav"),

        html.Div(children=
          [
            html.Div(children=
                  [  # Logo
                    html.Img(src=logo_img,id='logo'),
                    # Company Name
                    html.H1('Stonks Market',id='c_name')
                  ],
                className="header"),
            html.Div( #Description
              id="description", className="decription_ticker"),
            html.Div(children=[
                # Stock price plot
            ], id="graphs-content"),
            html.Div(children=[
                # Indicator plot
            ], id="main-content"),
            html.Div(children=[
                # Forecast plot
            ], id="forecast-content")
          ],
        className="content")
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)