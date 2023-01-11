import dash 
from dash import dcc
from dash import html
from datetime import datetime as dt
import pandas as pd
import numpy as np
import plotly.express as px
import base64
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
app=dash.Dash(__name__)
server=app.server
imgfile=r'D:\Work\Dash Stock App\assets\Best-Stocks.jpeg'
with open(imgfile, "rb") as image_file:
    img_data = base64.b64encode(image_file.read())
    img_data = img_data.decode()
    logo_img = "{}{}".format("data:image/jpg;base64, ", img_data)
app.head = html.Link(rel='stylesheet', href='assets/stylesheet.css')
app.layout=html.Div(children=
    [
        html.Div(children=
          [
            html.P("Welcome to Stonks!", className="start"),
            html.Div(children=[
              #Stock Code
              html.Label("Stock Code:"),
              dcc.Input(id='code',type='text'),
              html.Button('Submit',id='sub',value='submit',className='btn')

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
              html.Button('Stock Price',id='stp',className='btn'),
              # Indicators button
              html.Button('Indicators',id='sti',className='btn'),
              # Number of days of forecast input
              html.Br(),
              dcc.Input('Number of Days',type='text',id='stn'),
              # Forecast button
              html.Button('Forecast',id='stf',className='btn')

            ]),
          ],
        className="nav child"),

        html.Div(children=
          [
            html.Div(children=
                  [  # Logo
                    html.Img(src=logo_img,id='logo',width="50px",height="50px"),
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
        className="content child")
    ], className="parent"
)

if __name__ == '__main__':
    app.run_server(debug=True)