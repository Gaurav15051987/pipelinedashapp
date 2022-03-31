#!/usr/bin/env python
# coding: utf-8

# In[6]:


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, Output, State
from datetime import datetime as dt
from datetime import date
import pandas as pd
import numpy as np
import time
import urllib
import dash_table
import pandas as pd
import dash_bootstrap_components as dbc
from operator import itemgetter
import plotly.graph_objs as go
# from dash_extensions import Download
from dash.exceptions import PreventUpdate
from datetime import date
import calendar
from calendar import monthrange
import os
import datetime as dt
import plotly.express as px
from datetime import datetime
from sort_dataframeby_monthorweek import *
from sorted_months_weekdays import *
import dash_auth   
#from apps import assistivebuilder, custombuilder
#import reusable_components as rc
today = date.today()
# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'Admin': 'DashApp@Test'
}
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}]
)

app.config.suppress_callback_exceptions = True

server = app.server
app.config.suppress_callback_exceptions = True

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
def load_data():
    DATA = (r'Recommendation_Analysis_Data.csv')
    #DATA = (r'/home/jupyter/Final_Scripts/Recommendation/Recommendation_Analysis_Data.csv')
    df = pd.read_csv(DATA)
    df['Full_Base']='Full Base'
    df['Type_ALL']='All'
    df['Validity_ALL']='All'
    df['Total Recharge Count']=1
    df['Count Cust']=1
    #df['Date']=pd.to_datetime(df["TRX_DATE"]).dt.strftime('%Y-%m-%d')
    df=df.drop(df[['Product_Description','Offer_Type']],axis=1)
    return df

global cgp,tgp,inc,cg2,tg2
df = load_data()
df1=df
df['Active Customer']=1
df10=df.groupby('CG/TG', as_index=False)['Active Customer'].agg({'Churn_count': 'count'})
x=df10['Churn_count'][0]
y=df10['Churn_count'][1]
df=df.drop_duplicates(subset='CONSUMER_ID', keep="last")
df4=df.groupby('CG/TG', as_index=False)['Active Customer'].agg({'Churn_count': 'count'})
print(df4)
a=df4['Churn_count'][0]
b=df4['Churn_count'][1]

df1['Active Customer']=1
df5=df1.groupby('CG/TG', as_index=False)['Active Customer'].agg({'Churn_count': 'count'})

c=df5['Churn_count'][0]
d=df5['Churn_count'][1]
cgp1=(a/c)*100
tgp1=(b/d)*100
cgp="{0:.0f}%".format((a/c)*100)
tgp="{0:.0f}%".format((b/d)*100)
inc="{0:.0f}%".format((tgp1-cgp1)/cgp1*100)
################################################
totalcg_base=50000
totaltg_base=950000
num_days = monthrange(2019, 2)[1]
df['Date']=pd.to_datetime(df['TRX_DATE'],errors = 'coerce')
most_end_date = df['Date'].max()
lastdate=pd.to_datetime(most_end_date)
lastday=pd.Timedelta(days=30)
lastbegdate=lastdate-lastday
df2=df[(df["Date"] >=pd.to_datetime(lastbegdate))]
df2.to_csv("Active.csv")
#totalcg_base=50000
#totaltg_base=95000
df6=df2.groupby('CG/TG', as_index=False)['Active Customer'].agg({'Churn_count': 'count'})
print(df6)
g = df6['Churn_count'][0]
f = df6['Churn_count'][1]
print(g,f)
cgp2 = (g/totalcg_base)*100
tgp2=(f/totaltg_base)*100
cg3="{:.1f}".format((g/totalcg_base)*100)
tg3="{:.1f}".format((f/totaltg_base)*100)
#cg3=(g/totalcg_base)*100
#tg3=(f/totaltg_base)*100
inc1="{0:.0f}%".format((tgp2-cgp2)/cgp2*100)
print(cg3,tg3,inc1)
################################################
totalcg_base=50000
totaltg_base=950000
num_days = monthrange(2019, 2)[1]
df['Date']=pd.to_datetime(df['TRX_DATE'],errors = 'coerce')
most_end_date = df['Date'].max()
lastdate=pd.to_datetime(most_end_date)
lastday=pd.Timedelta(days=30)
lastbegdate=lastdate-lastday
df3=df[(df["Date"] >=pd.to_datetime(lastbegdate))]
#totalcg_base=50000
#totaltg_base=95000
df7=df3.groupby('CG/TG', as_index=False)['PRICE'].agg({'Churn_count': 'sum'})
print(df7)
h = df7['Churn_count'][0]
i = df7['Churn_count'][1]
print(g,f)
cgp4 = (g/totalcg_base)*100
tgp4=(f/totaltg_base)*100
cg4="{:.1f}".format((h/totalcg_base)*100)
tg4="{:.1f}".format((i/totaltg_base)*100)
#cg3=(g/totalcg_base)*100
#tg3=(f/totaltg_base)*100
inc3="{0:.0f}%".format((tgp4-cgp4)/cgp4*100)
print(cg4,tg4,inc3)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


index_page = html.Div([
        html.Div([
        html.Div([
            html.H2(children='Recommendation Engine Dashboard',
                    className='fix_label', style={'font-family': 'Arial',
                                                  'font-size': '33px', 'color': 'black', 'fontWeight': 'bold',
                                                  'textAlign': 'center'}), ],
            className='create_container3 twelve columns', id='title1'), ]),
    html.Div([
        html.Div([
            html.Div([html.Div([html.Span("Active Customers",className='font-bold text-title',
                             style={'font-size': '16px', 'margin-left': '10px', 'fontWeight': 'bold'}),],className="card_inner1"),],
                     className="on-the-center"),

#             html.Div([html.P("Active Customers",
#                              style={'font-size': '16px', 'margin-left': '10px', 'fontWeight': 'bold'})],
#                      className="on-the-center"),

            html.Div([
                html.Div([html.Label("CG", style={'font-size': '9px', 'margin-left': '25px'},id="target4"),
                         dbc.Tooltip("Total Customer Count"+" " + str(x),style={'text-align': 'center', 'fontWeight': 'bold', 'background':         '#000000','color': '#ffffff', 'fontSize': 8},target="target4"),], className="on-the-left"),
                html.Div([html.P("", style={'font-size': '9px', 'color': 'green'}), ], className="on-the-center"),
                html.Div([html.P("TG", style={'font-size': '9px', 'margin-right': '25px'},id="target5"),
                         dbc.Tooltip("Total Customer Count"+" " + str(y),style={'text-align': 'center', 'fontWeight': 'bold', 'background':         '#000000','color': '#ffffff', 'fontSize': 8},target="target5"),
                         ], className="on-the-right")
            ], className="same-line"),

            html.Div([  # html.Div(id='none',children=[],style={'display': 'none'}),
                html.Div([html.P(a, style={'font-size': '14px', 'fontWeight': 'bold', 'margin-top': '10px',
                                           'margin-left': '20px'}), ], className="on-the-left"),
                html.Div([html.P(b, style={'font-size': '14px', 'fontWeight': 'bold', 'margin-top': '10px',
                                           'margin-right': '20px'}), ], className="on-the-right")
            ], className="same-line"),

            html.Div([  # html.Div(id='none1',children=[],style={'display': 'none1'}),
                html.Div([html.P(cgp, style={'font-size': '14px', 'fontWeight': 'bold', 'margin-top': '20px',
                                             'margin-left': '20px'}), ], className="on-the-left"),
                html.Div([html.P(inc, style={'font-size': '14px', 'color': 'green', 'fontWeight': 'bold',
                                             'margin-top': '20px'}), ], className="on-the-center"),
                html.Div([html.P(tgp, style={'font-size': '14px', 'fontWeight': 'bold', 'margin-top': '20px',
                                             'margin-right': '20px'}), ], className="on-the-right")
            ], className="same-line"),
            html.Br(),
            html.Br(),
            html.Div([dcc.Graph(id='pie-chart1', style={'height': '360px', "width": "100%"}
                                , config={'displayModeBar': 'hover'}),
                      html.Div(id='none', children=[], style={'display': 'none'}), ], ),

            #         html.Div([html.P(children='Tenure for last 3 months',
            #         style={'textAlign': 'center','fontWeight': 'bold','margin-top': '10px'})],className='poll-name'),

            # html.Div([html.P(children="Tenure for last 3 months",
            # style={'font-size': '14px','fontWeight': 'bold','margin-top': '10px','textAlign': 'center'}),],className='poll-name'),

        ], className='create_container2 three columns',
            style={'height': '490px', "width": "31%"}),
        #######  #######################
        html.Div([
            html.Div([html.Div([html.Span("Total Pack Count",className='font-bold text-title',
                             style={'font-size': '16px', 'margin-left': '10px', 'fontWeight': 'bold'}),],className="card_inner1"),],
                     className="on-the-center"),
            
#             html.Div([html.P("Total Pack Count",
#                              style={'font-size': '16px', 'margin-left': '10px', 'fontWeight': 'bold'})],
#                      className="on-the-center"),

            html.Div([
                html.Div([html.P("CG", style={'font-size': '9px', 'margin-left': '25px'},id="target6"),
                         dbc.Tooltip("Total Customer Count"+" " + str(x),style={'text-align': 'center', 'fontWeight': 'bold', 'background':         '#000000','color': '#ffffff', 'fontSize': 8},target="target6"),], className="on-the-left"),
     
                html.Div([html.P("", style={'font-size': '9px', 'color': 'green'}), ], className="on-the-center"),
                html.Div([html.P("TG", style={'font-size': '9px', 'margin-right': '25px'},id="target7"),
                         dbc.Tooltip("Total Customer Count"+" " + str(y),style={'text-align': 'center', 'fontWeight': 'bold', 'background':         '#000000','color': '#ffffff', 'fontSize': 8},target="target7"),                         
                         ], className="on-the-right"),
            ], className="same-line"),

            html.Div([
                html.Div([html.Label(g, style={'font-size': '13px', 'fontWeight': 'bold', 'margin-top': '5px',
                                               'margin-left': '20px'}), ], className="on-the-left"),
                html.Div([html.Label(f, style={'font-size': '13px', 'fontWeight': 'bold', 'margin-top': '5px',
                                               'margin-right': '20px'}), ], className="on-the-right")
            ], className="same-line"),

            html.Div([
                html.Div([html.P(str("(") + cg3 + str("/cust") + str(")"),
                                 style={'font-size': '13px', 'fontWeight': 'bold', 'margin-top': '20px',
                                        'margin-left': '20px'}), ], className="on-the-left"),
                html.Div([html.P(str("(") + inc1 + str("/cust") + str(")"),
                                 style={'font-size': '13px', 'color': 'green', 'fontWeight': 'bold',
                                        'margin-top': '20px'}), ], className="on-the-center"),
                html.Div([html.P(str("(") + tg3 + str("/cust") + str(")"),
                                 style={'font-size': '13px', 'fontWeight': 'bold', 'margin-top': '20px',
                                        'margin-right': '20px'}), ], className="on-the-right")
            ], className="same-line"),

            html.Br(),
            html.Br(),
            dcc.Graph(id='pie-chart2', style={'height': '350px', "width": "100%"}
                      , config={'displayModeBar': 'hover'}),
            html.Div(id='none1', children=[], style={'display': 'none1'}),
            html.Div(id='none2', children=[], style={'display': 'none2'}),
            #         html.Div([html.P(children='Tenure for last 3 months',
            #         style={'textAlign': 'center','fontWeight': 'bold','margin-top': '10px'})],className='poll-name'),

            # html.Div([html.P(children="Tenure for last 3 months",
            # style={'font-size': '14px','fontWeight': 'bold','margin-top': '10px','textAlign': 'center'}),],className='poll-name'),

        ], className='create_container2 three columns',
            style={'height': '490px', "width": "31%"}),
        ##############################################3

        #############################

        html.Div([
            html.Div([html.Div([html.Span("Total Revenue",className='font-bold text-title',
                             style={'font-size': '16px', 'margin-left': '10px', 'fontWeight': 'bold'}),],className="card_inner1"),],
                     className="on-the-center"),

            html.Div([
                html.Div([html.P("CG", style={'font-size': '9px', 'margin-left': '25px'},id="target8"), 
                         dbc.Tooltip("Total Customer Count"+" " + str(x),
                                     style={'text-align': 'center', 'fontWeight': 'bold', 'background':         '#000000','color': '#ffffff', 'fontSize': 8},target="target8"),                         
                         ], className="on-the-left"),
                html.Div([html.P("", style={'font-size': '9px', 'color': 'green'}), ], className="on-the-center"),
                html.Div([html.P("TG", style={'font-size': '9px', 'margin-right': '25px'},id="target9"),
                         dbc.Tooltip("Total Customer Count"+" " + str(y),
                          style={'text-align': 'center', 'fontWeight': 'bold', 'background':'#000000','color': '#ffffff', 'fontSize': 8},target="target9"),                         
                         ], className="on-the-right")
            ], className="same-line"),

            html.Div([
                html.Div([html.P(h, style={'font-size': '13px', 'fontWeight': 'bold', 'margin-top': '5px',
                                           'margin-left': '20px'}), ], className="on-the-left"),
                html.Div([html.P(i, style={'font-size': '13px', 'fontWeight': 'bold', 'margin-top': '5px',
                                           'margin-right': '20px'}), ], className="on-the-right")
            ], className="same-line"),

            html.Div([
                html.Div([html.P(str("(") + cg4 + str("/cust") + str(")"),
                                 style={'font-size': '13px', 'fontWeight': 'bold', 'margin-top': '20px',
                                        'margin-left': '20px'}), ], className="on-the-left"),
                html.Div([html.P(str("(") + inc3 + str("/cust") + str(")"),
                                 style={'font-size': '13px', 'color': 'green', 'fontWeight': 'bold',
                                        'margin-top': '20px'}), ], className="on-the-center"),
                html.Div([html.P(str("(") + tg4 + str("/cust") + str(")"),
                                 style={'font-size': '13px', 'fontWeight': 'bold', 'margin-top': '20px',
                                        'margin-right': '20px'}), ], className="on-the-right")
            ], className="same-line"),

            html.Br(),
            html.Br(),
            dcc.Graph(id='pie-chart3', style={'height': '350px', "width": "100%"}
                      , config={'displayModeBar': 'hover'}),

            #         html.Div([html.P(children='Tenure for last 3 months',
            #         style={'textAlign': 'center','fontWeight': 'bold','margin-top': '10px'})],className='poll-name'),

            # html.Div([html.P(children="Tenure for last 3 months",
            # style={'font-size': '14px','fontWeight': 'bold','margin-top': '10px','textAlign': 'center'}),],className='poll-name'),

        ], className='create_container2 three columns',
            style={'height': '490px', "width": "31%"}),
    
        ]),
    ################################

    html.Br(),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Link(html.A('Click here to analyze and compare the trends of TG/CG/Full base and save your report',
                           style={'color': '#ffffff', 'text-decoration': 'none'},),
                           href='/page-1'), ], className="card_inner"),
            ], className="create_container4 four columns",
                style={'textAlign': 'center', 'margin-left': '100px', 'background': '#808080'}),

            html.Div([
                html.Div([dcc.Link(html.A('Click here to know more about which products are profitable',
                                 style={'color': '#ffffff', 'text-decoration': 'none'}), href='/page-2'),
                          ], className="card_inner"), ], className="create_container4 four columns",
                style={'textAlign': 'center', 'margin-left': '200px', 'background': '#008b8b'}),
        ], className="row flex-display"),
        # html.Br(),

    ]),
#     dcc.Link('Go to Page 1', href='/page-1'),
#     html.Br(),
#     dcc.Link('Go to Page 2', href='/page-2'),


    ], id="mainContainer",
    style={
        "display": "flex",
        "flex-direction": "column"
    })

    


page_1_layout = html.Div([
        html.Div([
    html.Div([[]],className='split left'),
    html.Div([[]],className='split right'),
    html.Div([
        html.Div([
        html.H2('Analyze Trends',
                                              className="card_inner",style={'font-family': 'Arial',
                            'font-size': '40px','color': '#000000', 'fontWeight': 'bold','textAlign': 'center'}),
           html.H2('Compare Trends',
                                              className="card_inner",style={'font-family': 'Arial',
                            'font-size': '40px','color': '#000000', 'fontWeight': 'bold','textAlign': 'center'})
            ],className='items1'),
             ],),



           html.Br(),
            html.Div([
            html.Label('Customer Base',className='p',style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold'}),

            html.Label('Date Range: ',
                            style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold'},className='p'),


            html.Label('Customer Base',className='p2',style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold'}),

            html.Label('Date Range: ',
                            style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold'},className='p2'),],className='items'),

#            html.Label('Select Granularity on which the data is aggregated',className='p1',
#                                              style={'font-family': 'Helvetica','justify':"center",
#                            'color': 'black','fontWeight': 'bold'}),],className='items'),


    html.Div([
    html.Div([
            dcc.Dropdown(
                id='demo_dropdown',
                options=[#{'label': i, 'value': i} for i in df['CG/TG'].unique()

                    {'label': 'Full Base', 'value': 'Full Base'},
                    {'label': 'CG', 'value': 'CG'},
                    {'label': 'TG', 'value': 'TG'}
                ],
                value=[],
                multi=True,
                ),],),

            html.Div([
                dcc.DatePickerRange(
                                id='date_picker_sales',
                                #start_date =date(2021, 4, 1) ,
                                #end_date = date.today(),
                                #min_date_allowed = min_dt,
                                #max_date_allowed = max_dt,
                                start_date_placeholder_text = 'Start date',
                                display_format='YYYY-MM-DD',
                                first_day_of_week = 1,
                                end_date_placeholder_text = 'End date',
                                style = {'font-size' : '14px','font-family': 'Helvetica','width':'105%',
                                         'border-radius': 'inherit'}),
                        ], style = {'margin-top' : '0px','height': "14px"},
                        ),


    html.Div([
            dcc.Dropdown(
                id='demo_dropdown2',
                options=[
                    {'label': 'Full Base', 'value': 'Full Base'},
                    {'label': 'CG', 'value': 'CG'},
                    {'label': 'TG', 'value': 'TG'}
                ],
                value=[],
                multi=True,
                ),],),

            html.Div([
                dcc.DatePickerRange(
                                id='date_picker_sales1',
                                #start_date =dt.date(dt.now()) ,
                                #end_date = date.today(),
                                #start_date =dt.date(dt.now()) ,
                                #end_date = date.today(),
                                #min_date_allowed = min_dt,
                                #max_date_allowed = max_dt,
                                start_date_placeholder_text = 'Start date',
                                display_format='YYYY-MM-DD',
                                first_day_of_week = 1,
                                end_date_placeholder_text = 'End date',
                                style = {'font-size' : '14px','font-family': 'Helvetica','width':'105%',
                                         'border-radius': 'inherit'}),
                        ], style = {'margin-top' : '0px','height': "14px"},
                        ),
    ],className='items'),

###############################################

        html.Br(),
        html.Div([
        html.Div([

                html.Label('Product Type',className='p',
                                              style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold'}),

            html.Label('Product Validity: ',
                            style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold'},className='p'),

               html.Label('Product Type',className='p2',
                                              style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold'}),

            html.Label('Product Validity: ',
                            style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold'},className='p2'),] ,className='items'),

            html.Div([

               html.Div([
                        dcc.Dropdown(
                            id='demo_dropdown4',
                            options=[
                                {'label': 'All', 'value': 'All'},
                                {'label': 'Data', 'value': 'Data'},
                                {'label': 'Voice', 'value': 'Voice'},
                                {'label': 'Combo', 'value': 'Combo'}
                            ],
                            value=[],
                            multi=True,
                    ),]),
               html.Div([
                        dcc.Dropdown(
                            id='demo_dropdown6',
                            options=[
                                {'label': 'All', 'value': 'All'},
                                {'label': 'Daily', 'value': 'Daily'},
                                {'label': 'Weekly', 'value': 'Weekly'},
                                {'label': 'Monthly', 'value': 'Monthly'}
                            ],
                            value=[],
                            multi=True,
                    ),]),


               html.Div([
                        dcc.Dropdown(
                            id='demo_dropdown5',
                            options=[
                                {'label': 'All', 'value': 'All'},
                                {'label': 'Data', 'value': 'Data'},
                                {'label': 'Voice', 'value': 'Voice'},
                                {'label': 'Combo', 'value': 'Combo'}
                            ],
                            value=[],
                            multi=True,
                    ),]),
               html.Div([
                        dcc.Dropdown(
                            id='demo_dropdown9',
                            options=[
                                {'label': 'All', 'value': 'All'},
                                {'label': 'Daily', 'value': 'Daily'},
                                {'label': 'Weekly', 'value': 'Weekly'},
                                {'label': 'Monthly', 'value': 'Monthly'}
                            ],
                            value=[],
                            multi=True,
                    ),]),

            ],className='items'),
        ]),

#####################################
        html.Br(),
        html.Div([

        html.Div([

                html.Label('Performance Indicator',
                                              style={'font-family': 'Helvetica','justify':"center",'text-align': 'center',
                            'color': '#000000','fontWeight': 'bold','font-size':'30px'},className='items4'),

#            html.Label('Select Granularity on which the data is aggregated',className='p',
#                                              style={'font-family': 'Helvetica','justify':"center",
#                            'color': '#F8F8FF','fontWeight': 'bold'}),

               html.Label('Performance Indicator',
                                              style={'font-family': 'Helvetica','justify':"center",'text-align': 'center',
                            'color': '#000000','fontWeight': 'bold','font-size':'30px'},className='items6'),

#            html.Label('Select Granularity on which the data is aggregated',className='p2',
#                                              style={'font-family': 'Helvetica','justify':"center",
#                            'color': '#F8F8FF','fontWeight': 'bold'}),
          ],className="row flex-display"),

    html.Div([

               html.Div([
                        dcc.Dropdown(
                            id='demo_dropdown7',
                            options=[
                                {'label': 'Active Base', 'value': 'Active'},
                                {'label': 'Total Recharge Count', 'value': 'TRC'},
                                {'label': 'Total Revenue', 'value': 'TR'},
                                {'label': 'Total Data Benefits', 'value': 'TDB'},
                                {'label': 'Total Voice Benefits', 'value': 'TVB'},
                                {'label': 'Total Data Price', 'value': 'TDP'},
                                {'label': 'Total Voice Price', 'value': 'TVP'},
                                {'label': 'Total Combo Price', 'value': 'TCP'}
                            ],
                            value=[],
                            #multi=True,
                    ),],className='items4'),
#              html.Div([
#                       dcc.Dropdown(
##                          id='demo-dropdown3',
#                          options=[
#                              {'label': 'Weekly', 'value': 'Weekly'},
#                              {'label': 'Monthly', 'value': 'Monthly'},
#                              {'label': 'Quarterly', 'value': 'Quarterly'},
#
#                          ],
#                          value='All',
#                          multi=True,
#                  ),]),
               html.Div([
                        dcc.Dropdown(
                            id='demo_dropdown8',
                            options=[
                                {'label': 'Active Base', 'value': 'Active'},
                                {'label': 'Total Recharge Count', 'value': 'TRC'},
                                    {'label': 'Total Revenue', 'value': 'TR'},
                                {'label': 'Total Data Benefits', 'value': 'TDB'},
                                {'label': 'Total Voice Benefits', 'value': 'TVB'},
                                {'label': 'Total Data Price', 'value': 'TDP'},
                                {'label': 'Total Voice Price', 'value': 'TVP'},
                                {'label': 'Total Combo Price', 'value': 'TCP'}

                            ],
                            value=[],
                            #multi=True,

                    ),],className='items6'),

#               html.Div([
#                        dcc.Dropdown(
#                            id='demo-dropdown1',
#                            options=[
#                                {'label': 'Weekly', 'value': 'Weekly'},
#                                {'label': 'Monthly', 'value': 'Monthly'},
#                                {'label': 'Quarterly', 'value': 'Quarterly'},
#
#                            ],
#                            value='All',
#                            multi=True,
#                    ),]),

                ],className="row flex-display"),






#         html.Br(),
#         html.Div([
#         html.Div([
#                  html.Label('Qurtarly-Monthly-Weekly Comparison Figure',className='p3',
#                                              style={'font-family': 'Helvetica','justify':"center",'font-size': '18px',
#                            'color': '#F8F8FF','fontWeight': 'bold'}),]),
#
#        html.Div([html.Label('Qurtarly-Monthly-Weekly Comparison Figure',className='p4',
#                                              style={'font-family': 'Helvetica','justify':"center",'font-size': '18px',
#                            'color': '#F8F8FF','fontWeight': 'bold'})]),],className='items5'),
#

        html.Div([
        html.Div([
                html.Label('Daily, Weekly or Monthly or Week Day Trend',
                           style={'text-align': 'center', 'color': '#000000','font-size': '15px',
                                                              'fontWeight': 'bold'}, id="target1"),
                  dcc.Dropdown(id='radio_items3',
                                 options=[
                                     {'label': 'Daily Trend', 'value': 'day'},
                                     {'label': 'Weekly Trend', 'value': 'week'},
                                     {'label': 'Monthly Trend', 'value': 'month'},
                                     {'label': 'WeekDay Trend', 'value': 'dayname'},
                                 ],
                                 value="",
                                 ),
                  dcc.RadioItems(id='radio_items4',
                                 options=[
                                     {'label': 'Line Chart', 'value': 'B'},
                                     {'label': 'Bar Chart', 'value': 'A'},

                                 ],
                                 value="B",
                                 labelStyle={'display': 'inline-block'},
                                 style={'text-align': 'center', 'color': '#000000','fontWeight': 'bold'}
                                 ),


                dcc.Graph(id='bar-chart4',style={'height': '360px',"width": "100%"}),],
                 className='create_container6 eight column',style={'height': '400px',"width": "42%"}),

        html.Div([
                html.Label('Daily, Weekly or Monthly or Week Day Trend',
                           style={'text-align': 'center', 'color': '#000000','font-size': '15px',
                                                              'fontWeight': 'bold'}, id="target2"),
                  dcc.Dropdown(id='radio_items5',
                                 options=[
                                     {'label': 'Daily Trend', 'value': 'day'},
                                     {'label': 'Weekly Trend', 'value': 'week'},
                                     {'label': 'Monthly Trend', 'value': 'month'},
                                     {'label': 'WeekDay Trend', 'value': 'dayname'},
                                 ],
                                 value="",
                                 ),
                  dcc.RadioItems(id='radio_items6',
                                 options=[
                                     {'label': 'Line Chart', 'value': 'B'},
                                     {'label': 'Bar Chart', 'value': 'A'},

                                 ],
                                 value="B",
                                 labelStyle={'display': 'inline-block'},
                                 style={'text-align': 'center', 'color': '#000000','fontWeight': 'bold'}
                                 ),

                dcc.Graph(id ='bar-chart5',style={'height': '360px',"width": "100%"}),],
                className='create_container7 eight column',style={'height': '400px',"width": "42%"}),

        ],className="row flex-display"),]),
#############################################
#        html.Br(),
#        html.Div([
#
#        html.Div([
#
#                html.Label('Day Of Week Trend',
#                                              style={'font-family': 'Helvetica','justify':"center",'text-align': 'center',
#                            'color': '#F8F8FF','fontWeight': 'bold','font-size': '40px'},className='items4'),
#
#               html.Label('Day Of Week Trend',
#                                              style={'font-family': 'Helvetica','justify':"center",'text-align': 'center',
#                            'color': '#F8F8FF','fontWeight': 'bold','font-size': '40px'},className='items6'),#
#
#          ],className="row flex-display"),


        html.Br(),
        html.Div([
    html.Div([
        dash_table.DataTable(

            id='table',

            tooltip={i: {'value': i, 'use_with': 'both'  # both refers to header & data cell
                         } for i in df.columns},
            # tooltip_header={i: i for i in df.columns},
            # style_cell={'textAlign': 'Center',
            #            'blackSpace': 'normal','height': 'auto'},
            # fixed_rows={'headers': True},
            # style_as_list_view=True,
            style_cell={
                'blackSpace': 'normal','minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'height': 'auto', 'text-align': 'left','textOverflow': 'ellipsis',
            },
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],

            page_current=0,
            page_size=25,
            page_action='native',
            sort_action='native',
            filter_action='native',
            column_selectable="single",
            sort_mode='multi',
            row_deletable=True,
            # export_format="csv",
            style_filter={'backgroundColor': 'white', 'color': 'white'},
            style_table={'maxHeight': '350px', 'overflowX': 'scroll', 'minWidth': '100%','width': '100%'},
            style_header={'backgroundColor': 'rgb(30, 30, 30)', 'color': 'white'},
            tooltip_delay=0,
            tooltip_duration=None,
            css=[{"selector": ".column-header", "rule": 'display: "none"'}]),],
            className='create_container6 eight column',style={'height': '400px',"width": "42%"}),

    html.Div([
        dash_table.DataTable(

            id='table1',

            tooltip={i: {'value': i, 'use_with': 'both'  # both refers to header & data cell
                         } for i in df.columns},
            # tooltip_header={i: i for i in df.columns},
            # style_cell={'textAlign': 'Center',
            #            'blackSpace': 'normal','height': 'auto'},
            # fixed_rows={'headers': True},
            # style_as_list_view=True,
            style_cell={
                'blackSpace': 'normal','minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'height': 'auto', 'text-align': 'left','textOverflow': 'ellipsis',
            },
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],

            page_current=0,
            page_size=25,
            page_action='native',
            sort_action='native',
            filter_action='native',
            column_selectable="single",
            row_deletable=True,
            sort_mode='multi',
            #export_format="csv",
            style_filter={'backgroundColor': 'white', 'color': 'white'},
            style_table={'maxHeight': '350px', 'overflowX': 'scroll', 'minWidth': '100%','width': '100%'},
            style_header={'backgroundColor': 'rgb(30, 30, 30)', 'color': 'white'},
            tooltip_delay=0,
            tooltip_duration=None,
            css=[{"selector": ".column-header", "rule": 'display: "none"','color': '#C0C0C0'}]),],
            className='create_container7 eight column',style={'height': '400px',"width": "42%"}),


        ],className="row flex-display"),
    html.Br(),
    html.Br(),
    html.Div([
            html.Div([html.Button(id="save-button", n_clicks=0, children="Save Report",style={'background': 'green','color': '#ffffff'}),
              dbc.Tooltip("Click For Save Data",style={'text-align': 'center', 'fontWeight': 'bold',
                                                                   'background': '#000000','color': '#ffffff', 'fontSize': 8},
                          target="save-button"),
              html.Div(id="output-3",style={'background': 'green','color': '#ffffff'})], className='create_container8 one cloumns'),

    html.Div([html.Button(id="save-button1", n_clicks=0, children="Save Report",style={'background': 'green','color': '#ffffff'}),
              dbc.Tooltip("Click For Save Data",style={'text-align': 'center', 'fontWeight': 'bold', 'background': '#000000','color': '#ffffff', 'fontSize': 8},
                          target="save-button1"),
              html.Div(id="output-4",style={'background': 'green','color': '#ffffff'})], className='create_container9 one cloumns'),

    ],className="row flex-display"),




],),
    
    html.Div(id='page-1-content'),
    html.Br(),
    html.Div([
       html.Div([
                    dcc.Link(html.A('Click here to know more about which products are profitable',
                           style={'color': '#ffffff', 'text-decoration': 'none'},),
                           href='/page-2'), ], className="card_inner"),
            ], className="create_container4 four columns",
                style={'textAlign': 'center', 'margin-left': '32%', 'background': '#008b8b'}),

#     html.Div([dcc.Link(html.A('Click here to know more about which products are profitable'
#                               ,style={'color': '#ffffff', 'text-decoration': 'none'}), href='/page-2'),
#                               ], className="create_container4 four columns",
#                                style={'textAlign': 'center', 'margin-left': '100px', 'background': '#008b8b'}),
    html.Br(),
    dcc.Link('', href='/'),
    
],id="mainContainer",
    style={
        "display": "flex",
        "flex-direction": "column"
})

 

@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)


page_2_layout = html.Div([
html.Div([
        html.Div([

        html.Div([
        html.H1('Product Analysis',
                                              className="card_inner",style={'font-family': 'Arial',
                            'font-size': '40px','color': '#000000', 'fontWeight': 'bold','textAlign': 'center'}),],id='title1'),
        html.Br(),
        html.Div([html.P('Analysis performance of products on the basis of Revenue and Recharge Count Select different conditions such as Top 10 products to focus or Bottom 10 products which can be removed in subsequent months. You can explore products contributing to 80% revenue and much more....',
                                              className="card_inner",style={'font-family': 'Arial',
                            'font-size': '15px','color': '#000000', 'fontWeight': 'bold','textAlign': 'center'})],),



           html.Br(),
            html.Div([
            html.Label('Customer Base',className='p',style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold','textAlign': 'center'}),

            html.Label('Date Range ',
                            style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold','textAlign': 'center'},className='p'),


            html.Label('Product Type',className='p6',style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold','textAlign': 'center'}),

            html.Label('Analyze Products Based on',
                            style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold','textAlign': 'center'},className='p6'),],className='items'),

#            html.Label('Select Granularity on which the data is aggregated',className='p1',
#                                              style={'font-family': 'Helvetica','justify':"center",
#                            'color': 'black','fontWeight': 'bold'}),],className='items'),

    html.Div([
    html.Div([
    html.Div([
            dcc.Dropdown(
                id='demo_dropdown',
                options=[#{'label': i, 'value': i} for i in df['CG/TG'].unique()

                    {'label': 'Full Base', 'value': 'Full Base'},
                    {'label': 'CG', 'value': 'CG'},
                    {'label': 'TG', 'value': 'TG'}
                ],
                value=[],
                multi=True,
                ),],),

            html.Div([
                dcc.DatePickerRange(
                                id='date_picker_sales2',
                                #start_date =date(2021, 4, 1) ,
                                #end_date = date.today(),
                                #min_date_allowed = min_dt,
                                #max_date_allowed = max_dt,
                                start_date_placeholder_text = 'Start date',
                                display_format='YYYY-MM-DD',
                                first_day_of_week = 1,
                                end_date_placeholder_text = 'End date',
                                style = {'font-size' : '14px','font-family': 'Helvetica','width':'105%',
                                         'border-radius': 'inherit'}),
                        ], style = {'margin-top' : '0px','height': "14px"},
                        ),


    html.Div([
            dcc.Dropdown(
                id='demo_dropdown10',
                options=[
                    {'label': 'All', 'value': 'All'},
                    {'label': 'Data', 'value': 'Data'},
                    {'label': 'Voice', 'value': 'Voice'},
                    {'label': 'Combo', 'value': 'Combo'}
                ],
                value=[],
                multi=True,
                ),],),
        html.Div([
                        dcc.Dropdown(
                            id='demo_dropdown11',
                            options=[
                                {'label': 'Top 10 By Revenue', 'value': 'T10R'},
                                {'label': 'Top 10 By Count', 'value': 'T10C'},
                                {'label': 'Bottom 10 By Revenue', 'value': 'B10R'},
                                {'label': 'Bottom 10 By Count', 'value': 'B10C'},
                                {'label': 'Top 80% of Total Revenue', 'value': '80TR'},
                                {'label': 'Top 80% of Total Count', 'value': '80TC'},
                                {'label': 'Bottom 20% of Total Revenue ', 'value': '20TR'},
                                {'label': 'Bottom 20% of Total Count', 'value': '20TC'}
                            ],
                            value=[],
                            #multi=True,
                    ),],),


    ],className='items12'),


        ],className="row flex-display"),
    html.Br(),
    
    html.Div([
        html.Div([html.Label('REVENUE',style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold','textAlign': 'center'}),


                html.Div(dcc.Graph(id='bar-chart6',config={"toImageButtonOptions": {"width": None, "height": None}}),style={'overflow-x':'auto'}),],
                  className='create_container11 nine column',style={'height': '500px',"width": "46%",'margin-left':'2%'}),

        html.Div([html.Label('COUNT',style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold','textAlign': 'center'}),

                html.Div(dcc.Graph(id='bar-chart7',config={"toImageButtonOptions": {"width": None, "height": None}}),style={'overflow-x':'auto'}),],
                  className='create_container11 nine column',style={'height': '500px',"width": "46%",'margin-left':'4%'}),

        ],className="row flex-display"),


],),
       html.Br(),
        html.Div([html.Button(id="save-button1", n_clicks=0, children="Save Report",style={'background': 'green','color': '#ffffff'}),
              dbc.Tooltip("Click For Save Data",style={'text-align': 'center', 'fontWeight': 'bold',
                           'background': '#000000','color': '#ffffff', 'fontSize': 8},target="save-button1"),
              html.Div(id="output-1",style={'background': 'green','color': '#ffffff'})], className='create_container10 one cloumns'),
###############################################################
        html.Br(),
        html.Div([
        html.H1('Product Journey',
                                              className="card_inner",style={'font-family': 'Arial',
                            'font-size': '40px','color': '#000000', 'fontWeight': 'bold','textAlign': 'center'}),],id='title2'),
        html.Br(),
        html.Div([html.P('Analyze the products journey of selected products and compare them on the basis of revenue and count on different customer base',
                                              className="card_inner",style={'font-family': 'Arial',
                            'font-size': '15px','color': '#000000', 'fontWeight': 'bold','textAlign': 'center'})],),

           html.Br(),
            html.Div([
            html.Label('Product Type',className='p',style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold','textAlign': 'center'}),

            html.Label('Product Validity',className='p6',style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold','textAlign': 'center'}),

            html.Label('Select The Products',
                            style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold','textAlign': 'center'},className='p7'),]
                ,className='itemss'),
    html.Table(id='my-table'),
        html.Div([
    html.Div([
    html.Div([
            dcc.Dropdown(
                id='demo_dropdown15',
                options=[

                    {'label': 'All', 'value': 'All'},
                    {'label': 'Data', 'value': 'Data'},
                    {'label': 'Voice', 'value': 'Voice'},
                    {'label': 'Combo', 'value': 'Combo'}
                ],
                value=[],
                multi=True,
                ),],),



    html.Div([
            dcc.Dropdown(
                id='demo_dropdown16',
                options=[
                    {'label': 'All', 'value': 'All'},
                    {'label': 'Daily', 'value': 'Daily'},
                    {'label': 'Weekly', 'value': 'Weekly'},
                    {'label': 'Monthly', 'value': 'Monthly'}
                ],
                value=[],
                multi=True,
                ),],),

                html.Details([
                html.Summary('Select Products...'),
                html.Br(),
                dbc.Col([
                    dcc.Checklist(id='demo_dropdown17',
                        options=[
#                             {'label': 'New York City', 'value': 'NYC'},
#                             {'label': 'Montréal', 'value': 'MTL'},
#                             {'label': 'San Francisco', 'value': 'SF'}
                            ],
                        value=[],
                        labelStyle = {'display': 'block'},
                        style={'width': '250px',
                               'height': '90px', "overflow-x":"scroll"}
                        )
                    ])
                ]),


#         html.Div([
#                         dcc.Dropdown(
#                             id='demo_dropdown17',
#                             options=[],
#                             value=[],
#                             #{'label': i, 'value': i} for i in df['PRODUCT_ID'].unique()

#                     ),],),


    ],className='itemss'),

    html.Br(),

    html.Div([
        html.Div([html.Label('',style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold','textAlign': 'center'}),
                  dcc.RadioItems(id='radio_items8',
                                 options=[
                                     {'label': 'Full Base', 'value': 'A'},
                                     {'label': 'CG', 'value': 'B'},
                                     {'label': 'TG', 'value': 'C'},

                                 ],
                                 value="A",
                                 labelStyle={'display': 'inline-block'},
                                 style={'text-align': 'center', 'color': '#000000','fontWeight': 'bold'}
                                 ),



                dcc.Graph(id='bar-chart8',style={'height': '650',"width": "100%"}),],
                 className='create_container11 nine column',style={'height': '500px',"width": "45%"}),

        html.Div([html.Label('',style={'font-family': 'Helvetica','justify':"center",
                            'color': '#000000','fontWeight': 'bold','textAlign': 'center'}),

                  dcc.RadioItems(id='radio_items9',
                                 options=[
                                     {'label': 'Full Base', 'value': 'A'},
                                     {'label': 'CG', 'value': 'B'},
                                     {'label': 'TG', 'value': 'C'},

                                 ],
                                 value="A",
                                 labelStyle={'display': 'inline-block'},
                                 style={'text-align': 'center', 'color': '#000000','fontWeight': 'bold'}
                                 ),

                dcc.Graph(id='bar-chart9',style={'height': '650',"width": "100%"}),],
                 className='create_container12 nine column',style={'height': '500px',"width": "45%"}),

        ],className="row flex-display"),
    html.Div([
        dash_table.DataTable(

            id='table2',

            tooltip={i: {'value': i, 'use_with': 'both'  # both refers to header & data cell
                         } for i in df.columns},
            # tooltip_header={i: i for i in df.columns},
            # style_cell={'textAlign': 'Center',
            #            'blackSpace': 'normal','height': 'auto'},
            # fixed_rows={'headers': True},
            # style_as_list_view=True,
            style_cell={
                'blackSpace': 'normal','minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'height': 'auto', 'text-align': 'left','textOverflow': 'ellipsis',
            },
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],

            page_current=0,
            page_size=25,
            page_action='native',
            sort_action='native',
            filter_action='native',
            column_selectable="single",
            sort_mode='multi',
            # export_format="csv",
            style_filter={'backgroundColor': 'white', 'color': 'white'},
            style_table={'maxHeight': '350px', 'overflowX': 'scroll', 'minWidth': '100%','width': '100%'},
            style_header={'backgroundColor': 'rgb(30, 30, 30)', 'color': 'white'},
            tooltip_delay=0,
            tooltip_duration=None,
            css=[{"selector": ".column-header", "rule": 'display: "none"',"box-shadow":"4px 4px 4px 4px lightgrey"}]),],
            className='create_container6 eight column',style={'height': '400px',"width": "98%"}),

        ]),
    html.Div(id='page-2-content'),
    html.Br(),

    html.Div([
       html.Div([
                    dcc.Link(html.A('Click here to analyze and compare the trends of TG/CG/Full base and save your report',
                           style={'color': '#ffffff', 'text-decoration': 'none'},),
                           href='/page-1'), ], className="card_inner"),
            ], className="create_container4 four columns",
                style={'textAlign': 'center', 'margin-left': '32%', 'background': '#808080'}),
    
#     html.Div([dcc.Link(html.A('Click here to analyze and compare the trends of TG/CG/Full base and save your report',
#                               style={'color': '#ffffff', 'text-decoration': 'none'}), href='/page-1'),
#                               ], className="create_container4 four columns",
#                                style={'textAlign': 'center', 'margin-left': '100px', 'background': '#808080'}),

#     dcc.Link('Go To Analyze and Compare Page', href='/page-1'),
    html.Br(),
    dcc.Link('', href='/')

],id="mainContainer",
    style={
        "display": "flex",
        "flex-direction": "column"
    })

])

@app.callback(dash.dependencies.Output('page-2-content', 'children'),
              [dash.dependencies.Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)


# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here
    
    
@app.callback(
    Output("pie-chart1", "figure"),
    [Input('none', 'children'),]
)



def activegraph(none):
    df=load_data()
    #print(df)
    #num_days = monthrange(2019, 2)[1]
    global chart,nk
    import numpy as np
    df['Active Customer']=1
    
    df['Date']=pd.to_datetime(df['TRX_DATE'],errors = 'coerce')
    most_end_date = df['Date'].max()
    lastdate=pd.to_datetime(most_end_date)
    lastday=pd.Timedelta(days=30)
    lastbegdate=lastdate-lastday
    df2=df[(df["Date"] >=pd.to_datetime(lastbegdate))]
    df2=df2.drop_duplicates(subset='CONSUMER_ID', keep="last")
    #print(most_end_date)
    #print(lastbegdate)
    #df2.to_csv("active.csv")
    df2['WeekNum'] = df2['Date'].dt.strftime('%W')
    pv = pd.pivot_table(df2, values=['Active Customer'],index=['WeekNum','Date','CG/TG'],aggfunc=np.sum)
    df4=pv.reset_index()
    df4["Week"]=str(' Week')
    df4["Week_Trend"] = df4["WeekNum"].astype(str) + df4["Week"]
    #print(df4)
    df5 = df4.groupby(['WeekNum','Week_Trend','CG/TG'])['Date'].agg(['min', 'max','count']).reset_index()
    #print(df5)
    df6 = df4.groupby(['WeekNum','CG/TG'])['Active Customer'].agg(['sum']).reset_index()
    #print(df6)
    df7=pd.merge(df5, df6, left_index=True, right_index=True)
    df7=df7.drop(['WeekNum_y','CG/TG_y','WeekNum_x'],axis=1)
    df7['Date_Range']=df7['min'].astype(str)+"-"+df7['max'].astype(str)
    df7["Week_Day_Count"] = df7["Week_Trend"].astype(str)

    df7["Week_Day_Count1"] = df7["Week_Trend"].astype(str) +" "+"("+"contains"+ df7["count"].astype(str)+" "+str("Days")+")"
    print(df7)
    cg=df7[(df7['CG/TG_x']=='CG')]
    tg=df7[(df7['CG/TG_x']=='TG')]
    print(cg)
    print(tg)
    new_customdata = cg.iloc[:,8:9]
    new_customdata1 = tg.iloc[:,8:9]
    print(new_customdata)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=cg['Week_Day_Count'],
        y=cg['sum'],
        text = cg['Date_Range'],textposition="none",
        name='CG',
        marker_color='indianred',
        customdata=new_customdata,
        hovertemplate='Date B/W:%{text}<br>Count:%{y}<br>Description:%{customdata[0]}<extra></extra>'
    ))
    fig.add_trace(go.Bar(
        x=tg['Week_Day_Count'],
        y=tg['sum'],text = tg['Date_Range'],textposition="none",
        name='TG',
        marker_color='lightsalmon',
        customdata=new_customdata1,
        hovertemplate='Date B/W:%{text}<br>Count:%{y}<br>Description:%{customdata[0]}<extra></extra>'

        ))

    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    fig.update_layout(barmode='group', xaxis_tickangle=-45,margin=dict(t=30, b=0, l=0, r=0),
                      yaxis={'categoryorder': 'total ascending',"title":'<b>Active Customer</b>'},
                      xaxis={"title":'<b>Week Of Last Month</b>'},plot_bgcolor='#FFFFFF',
                     legend=dict(yanchor="bottom",orientation='h',y=-0.90,xanchor="center",x=0.4))

    chart=fig
    return chart

@app.callback(
    Output("pie-chart2", "figure"),
    [Input('none1', 'children'),]
)



def activegraph1(none1):
    df=load_data()
    #print(df)
    #num_days = monthrange(2019, 2)[1]
    global chart1
    import numpy as np
    df['Active Customer']=1
    df['Date']=pd.to_datetime(df['TRX_DATE'],errors = 'coerce')
    most_end_date = df['Date'].max()
    lastdate=pd.to_datetime(most_end_date)
    lastday=pd.Timedelta(days=30)
    lastbegdate=lastdate-lastday
    df2=df[(df["Date"] >=pd.to_datetime(lastbegdate))]
    print(most_end_date)
    print(lastbegdate)
    #df2.to_csv("active.csv")
    df2['WeekNum'] = df2['Date'].dt.strftime('%W')
    pv = pd.pivot_table(df2, values=['Active Customer'],index=['WeekNum','Date','CG/TG'],aggfunc=np.sum)
    df4=pv.reset_index()
    df4["Week"]=str(' Week')
    df4["Week_Trend"] = df4["WeekNum"].astype(str) + df4["Week"]
    #print(df4)
    df5 = df4.groupby(['WeekNum','Week_Trend','CG/TG'])['Date'].agg(['min', 'max','count']).reset_index()
    #print(df5)
    df6 = df4.groupby(['WeekNum','CG/TG'])['Active Customer'].agg(['sum']).reset_index()
    #print(df6)
    df7=pd.merge(df5, df6, left_index=True, right_index=True)
    df7=df7.drop(['WeekNum_y','CG/TG_y','WeekNum_x'],axis=1)
    df7['Date_Range']=df7['min'].astype(str)+"-"+df7['max'].astype(str)
    df7["Week_Day_Count"] = df7["Week_Trend"].astype(str)

    df7["Week_Day_Count1"] = df7["Week_Trend"].astype(str) +" "+"("+"contains"+ df7["count"].astype(str)+" "+str("Days")+")"

    
    print(df7)
    cg=df7[(df7['CG/TG_x']=='CG')]
    tg=df7[(df7['CG/TG_x']=='TG')]
    print(cg)
    print(tg)
    new_customdata = cg.iloc[:,8:9]
    new_customdata1 = tg.iloc[:,8:9]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=cg['Week_Day_Count'],
        y=cg['sum'],text = cg['Date_Range'],textposition="none",
        name='CG',
        marker_color='#306754',
        customdata=new_customdata,
        hovertemplate='Date B/W:%{text}<br>Count:%{y}<br>Description:%{customdata[0]}<extra></extra>'
    
    ))
    fig.add_trace(go.Bar(
        x=tg['Week_Day_Count'],
        y=tg['sum'],text = tg['Date_Range'],textposition="none",
        name='TG',
        marker_color='#50C878',
        customdata=new_customdata1,
        hovertemplate='Date B/W:%{text}<br>Count:%{y}<br>Description:%{customdata[0]}<extra></extra>'

    ))

    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    fig.update_layout(barmode='group', xaxis_tickangle=-45,margin=dict(t=30, b=0, l=0, r=0),
                      yaxis={'categoryorder': 'total ascending',"title":'<b>Count</b>'},
                      xaxis={"title":'<b>Week Of Last Month</b>'},plot_bgcolor='#FFFFFF',
                     legend=dict(yanchor="bottom",orientation='h',y=-0.90,xanchor="center",x=0.4))

    chart=fig
    return chart

@app.callback(
    Output("pie-chart3", "figure"),
    [Input('none2', 'children'),]
)



def activegraph3(none2):
    df=load_data()
    #print(df)
    #num_days = monthrange(2019, 2)[1]
    global chart1
    import numpy as np
    #df=df.drop_duplicates(subset='CONSUMER_ID', keep="last")
    df['Date']=pd.to_datetime(df['TRX_DATE'],errors = 'coerce')
    most_end_date = df['Date'].max()
    lastdate=pd.to_datetime(most_end_date)
    lastday=pd.Timedelta(days=30)
    lastbegdate=lastdate-lastday
    df2=df[(df["Date"] >=pd.to_datetime(lastbegdate))]
    print(most_end_date)
    print(lastbegdate)
    print(df2)
    df2['WeekNum'] = df2['Date'].dt.strftime('%W')
    pv = pd.pivot_table(df2, values=['PRICE'],index=['WeekNum','Date','CG/TG'],aggfunc=np.sum)
    df4=pv.reset_index()
    df4["Week"]=str(' Week')
    df4["Week_Trend"] = df4["WeekNum"].astype(str) + df4["Week"]
    #print(df4)
    df5 = df4.groupby(['WeekNum','Week_Trend','CG/TG'])['Date'].agg(['min', 'max','count']).reset_index()
    #print(df5)
    df6 = df4.groupby(['WeekNum','CG/TG'])['PRICE'].agg(['sum']).reset_index()
    #print(df6)
    df7=pd.merge(df5, df6, left_index=True, right_index=True)
    df7=df7.drop(['WeekNum_y','CG/TG_y','WeekNum_x'],axis=1)
    df7['Date_Range']=df7['min'].astype(str)+"-"+df7['max'].astype(str)
    df7["Week_Day_Count"] = df7["Week_Trend"].astype(str)

    df7["Week_Day_Count1"] = df7["Week_Trend"].astype(str) +" "+"("+"contains"+ df7["count"].astype(str)+" "+str("Days")+")"

    print(df7)
    cg=df7[(df7['CG/TG_x']=='CG')]
    tg=df7[(df7['CG/TG_x']=='TG')]
    print(cg)
    print(tg)
    new_customdata = cg.iloc[:,8:9]
    new_customdata1 = tg.iloc[:,8:9]

    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=cg['Week_Day_Count'],
        y=cg['sum'],text = cg['Date_Range'],textposition="none",
        name='CG',
        marker_color='#800000',
        customdata=new_customdata,
        hovertemplate='Date B/W:%{text}<br>Count:%{y}<br>Description:%{customdata[0]}<extra></extra>'

    ))
    fig.add_trace(go.Bar(
        x=tg['Week_Day_Count'],
        y=tg['sum'],text = tg['Date_Range'],textposition="none",
        name='TG',
        marker_color='#DC381F',
        customdata=new_customdata1,
        hovertemplate='Date B/W:%{text}<br>Revenue:%{y}<br>Description:%{customdata[0]}<extra></extra>'

    ))

    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    fig.update_layout(barmode='group', xaxis_tickangle=-45,margin=dict(t=30, b=0, l=0, r=0),
                      yaxis={'categoryorder': 'total ascending',"title":'<b>Revenue</b>'},
                      xaxis={"title":'<b>Week Of Last Month</b>'},plot_bgcolor='#FFFFFF',
                     legend=dict(yanchor="bottom",orientation='h',y=-0.90,xanchor="center",x=0.4))

    chart=fig
    return chart

@app.callback(Output("output-4", "children"),
              [Input("save-button1", "n_clicks"),
               ],
              [State("table1", "data")],)

def selected_data_to_csv1(nclicks, table1):
    if nclicks == 0:
        raise PreventUpdate
    else:
        # df=pd.DataFrame(table1)
        # pd.DataFrame(table1).to_csv('C://Users//ch-e05138//Desktop//New folder//gaurav.csv',index=False)
        save_path = ''
        file_name =  "Compare_Trend.csv"
        print(file_name)
        completeName = os.path.join(save_path, file_name)
        print(completeName)
        pd.DataFrame(table1).to_csv(completeName, index=False)

        # df.to_csv(completeName,index=False)
        # print(completeName)
        # file1 = open(completeName, "w")
        # file1.write("file")
        # file1.close()
        # send_data_frame(df.to_csv, value+".csv", index=False)
        # return completeName
        # return send_data_frame(df.to_csv, value+".csv", index=False)

        return "Data Saved"

@app.callback(Output('bar-chart5', 'figure'),
              Output('table1', 'data'),
              Output('table1', 'columns'),
              #Output("date_picker_sales1","start_date"),
               Input('demo_dropdown2','value'),
               Input("date_picker_sales1","start_date"),
               Input("date_picker_sales1","end_date"),
               Input('demo_dropdown5','value'),
               Input('demo_dropdown9','value'),
               Input('demo_dropdown8','value'),
              Input('radio_items5','value'),
              Input('radio_items6','value'),
              )


def display_graphs1(demo_dropdown2_value,date_picker_sales1_start_date, date_picker_sales1_end_date,demo_dropdown5_value, demo_dropdown9_value,demo_dropdown8_value,radio_items5_value,radio_items6_value):
    
    
    #df = pd.read_csv(r'Dashboard_Input_Sample_0.1Mn.csv')
    #df = pd.read_csv(r'Dashboard_Input_Sample_10k.csv')
    #df = pd.read_csv(r'Dashboard_Input_Sample_50k.csv')
    #df = pd.read_csv(r'Dashboard_Input_Sample_0.5Mn.csv')
    #print(demo_dropdown2_value)
    df =load_data()
    #print(df)
    global chart2,df11,pv,df12,df13,df14,df15,df16,df_weekday1,filtered_df_month1
    if demo_dropdown2_value == []:
        #print(demo_dropdown2_value)
        
        filtered_df_month1 = df
        start=filtered_df_month1['TRX_DATE'].min()
        #df11=pd.pivot_table(data=filtered_df_month1, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        #print(filtered_df_month1)
        chart2 = {'data': []}

    elif demo_dropdown2_value == ['Full Base']:
        print(demo_dropdown2_value)
        b=[]
        for i in demo_dropdown2_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        filtered_df_month1.to_csv("/home/jupyter/fullbase.csv")
        #filtered_df_month1 = filtered_df_month1[filtered_df_month1['Full_Base'] == ]
        #filtered_df_month1 = df[(df['CG/TG'].isin(a))]    
        #df13=pd.pivot_table(data=filtered_df_month1, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()

    elif demo_dropdown2_value == ['Full Base','CG']:
        print(demo_dropdown2_value)
        b=[]
        for i in demo_dropdown2_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))] 
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown2_value == ['Full Base','TG']:
        print(demo_dropdown2_value)
        b=[]
        for i in demo_dropdown2_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        #filtered_df_month1 = filtered_df_month1[filtered_df_month1['Full_Base'] == ]
        #filtered_df_month1 = df[(df['CG/TG'].isin(a))]    
    elif demo_dropdown2_value == ['TG','Full Base']:
        print(demo_dropdown2_value)
        b=[]
        for i in demo_dropdown2_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        
    elif demo_dropdown2_value == ['Full Base','CG','TG']:
        print(demo_dropdown2_value)
        b=[]
        for i in demo_dropdown2_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        
    elif demo_dropdown2_value == ['Full Base','TG','CG']:
        print(demo_dropdown2_value)
        b=[]
        for i in demo_dropdown2_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        
    elif demo_dropdown2_value == ['CG','TG','Full Base']:
        print(demo_dropdown2_value)
        b=[]
        for i in demo_dropdown2_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        print(filtered_df_month1)
        
    elif demo_dropdown2_value == ['TG','CG','Full Base']:
        print(demo_dropdown2_value)
        b=[]
        for i in demo_dropdown2_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown2_value == ['CG','Full Base','TG']:
        print(demo_dropdown2_value)
        b=[]
        for i in demo_dropdown2_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        
    elif demo_dropdown2_value == ['TG','Full Base','CG']:
        print(demo_dropdown2_value)
        b=[]
        for i in demo_dropdown2_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        
    elif demo_dropdown2_value == ['TG','Full Base']:
        print(demo_dropdown2_value)
        b=[]
        for i in demo_dropdown2_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

        
    elif demo_dropdown2_value == ['CG','Full Base']:
        print(demo_dropdown2_value)
        b=[]
        for i in demo_dropdown2_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown2_value == ['CG','TG']:
        a=[]
        for i in demo_dropdown2_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month1 = df[(df['CG/TG'].isin(a))]  
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1 )
        #filtered_df_month1 = df[df['CG/TG'] == demo_dropdown2_value]
            #print(filtered_df_month1)
            #df1 = df.groupby('CG/TG', as_index=False)['Voice_Benefit'].agg({'Sum_value': 'sum'})

    elif demo_dropdown2_value == ['CG']:
        a=[]
        for i in demo_dropdown2_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month1 = df[(df['CG/TG'].isin(a))]  
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        print(start)
    elif demo_dropdown2_value == ['TG']:
        a=[]
        for i in demo_dropdown2_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month1 = df[(df['CG/TG'].isin(a))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)    
###################################################        
    if demo_dropdown5_value == []:
        #print(demo_dropdown2_value)
        filtered_df_month1 = filtered_df_month1
        #df11=pd.pivot_table(data=filtered_df_month1, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        print(filtered_df_month1)
        chart2 = {'data': []}

    elif demo_dropdown5_value == ['All']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
#        print(b)
#        b[0]="Full Base"
#        print(b)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type_ALL'].isin(b))]    
        print(filtered_df_month1)
    
    elif demo_dropdown5_value == ['Data']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        print(start)
        
    elif demo_dropdown5_value == ['Voice']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        filtered_df_month1.to_csv("voice.csv")
    elif demo_dropdown5_value == ['Combo']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown5_value == ['Voice','Combo']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown5_value == ['Voice','Data']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        
    elif demo_dropdown5_value == ['Data','Voice']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown5_value == ['Combo','Voice']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown5_value == ['Combo','Data']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown5_value == ['Data','Combo']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown5_value == ['Data','Voice','Combo']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        
    elif demo_dropdown5_value == ['Data','Voice','Combo']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown5_value == ['Voice','Data','Combo']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown5_value == ['Voice','Combo','Data']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown5_value == ['Combo','Voice','Data']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))] 
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown5_value == ['Combo','Data','Voice']:
        print(demo_dropdown5_value)
        b=[]
        for i in demo_dropdown5_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        print(filtered_df_month1)
    if demo_dropdown9_value == []:
        #print(demo_dropdown2_value)
        filtered_df_month1 = filtered_df_month1
        #df11=pd.pivot_table(data=filtered_df_month1, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        print(filtered_df_month1)
        chart2 = {'data': []}

    elif demo_dropdown9_value == ['All']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
#        print(b)
#        b[0]="Full Base"
#        print(b)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity_ALL'].isin(b))]    
        print(filtered_df_month1)
    
    elif demo_dropdown9_value == ['Daily']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        print(start)
        
    elif demo_dropdown9_value == ['Weekly']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown9_value == ['Monthly']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown9_value == ['Daily','Weekly']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown9_value == ['Daily','Monthly']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        
    elif demo_dropdown9_value == ['Weekly','Daily']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown9_value == ['Weekly','Monthly']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown9_value == ['Monthly','Daily']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown9_value == ['Monthly','Weekly']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown9_value == ['Daily','Weekly','Monthly']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        
    elif demo_dropdown9_value == ['Daily','Monthly','Weekly']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown9_value == ['Weekly','Daily','Monthly']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown9_value == ['Weekly','Monthly','Daily']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown9_value == ['Monthly','Weekly','Daily']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))] 
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown9_value == ['Monthly','Daily','Weekly']:
        print(demo_dropdown9_value)
        b=[]
        for i in demo_dropdown9_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Validity'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        
    if date_picker_sales1_start_date == None and date_picker_sales1_end_date == None:
        #print(demo_dropdown2_value)
        filtered_df_month1 = filtered_df_month1
        #df11=pd.pivot_table(data=filtered_df_month1, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        print(filtered_df_month1)
        chart2 = {'data': []}
    elif date_picker_sales1_start_date != None and date_picker_sales1_end_date != None:
        
        print(date_picker_sales1_start_date)
        print(date_picker_sales1_end_date)
        global pv,chart,df13
        #filtered_df_month1=filtered_df_month1[(filtered_df_month1['Date']>date_picker_sales1_start_date)&(filtered_df_month1['Date']<date_picker_sales1_end_date)]
        print(filtered_df_month1)
        filtered_df_month1['Date']=pd.to_datetime(filtered_df_month1['TRX_DATE'],errors = 'coerce')
        filtered_df_month1['Month']=filtered_df_month1['Date'].dt.month
        filtered_df_month1['Day']=filtered_df_month1['Date'].dt.day
        #filtered_df_month1['WeekNum'] = filtered_df_month1['Date'].dt.week
        filtered_df_month1['WeekNum'] = filtered_df_month1['Date'].dt.strftime('%W')
        filtered_df_month1['Name of Day']=filtered_df_month1['Date'].dt.day_name()
        #filtered_df_month1['WeekNum'] = filtered_df_month1['WeekNum'].replace([53], 1)
        filtered_df_month1['Month_Name']=filtered_df_month1['Month'].apply(lambda x:calendar.month_abbr[x])
        filtered_df_month1["Week"]=str(' Week')
        filtered_df_month1["Week_Trend"] = filtered_df_month1["WeekNum"].astype(str) + filtered_df_month1["Week"]
        filtered_df_month1["Day_Trend"] = filtered_df_month1["Day"].astype(str) + filtered_df_month1["Month_Name"]
        
        date_entry=date_picker_sales1_start_date
        year,month,day=map(int,date_entry.split('-'))
        start_date=datetime(year,month,day)

        date_entry1=date_picker_sales1_end_date
        year,month,day=map(int,date_entry1.split('-'))
        end_date=datetime(year,month,day)

        date33=end_date
        date11=start_date

        print(date11)
        print(date33)
        mdate1=date11
        rdate1=date33
        delta=(rdate1-mdate1).days
        print(delta)
        filtered_df_month1=filtered_df_month1[(filtered_df_month1['Date']>=date11)&(filtered_df_month1['Date']<=date33)]
        print(filtered_df_month1)
    if demo_dropdown8_value == "":
        #global df13
        #df13 = df11
        #df11=pd.pivot_table(data=filtered_df_month1, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        print(df13)
        chart2 = {'data': []}
    if demo_dropdown8_value == 'TRC':
        if radio_items6_value == "B":
            print(filtered_df_month1)
            global df11,pv
            #if delta>=30:
            #pv=pd.pivot_table(filtered_df_month1,values=['Total Recharge Count'],index=['Month_Name'],aggfunc=np.sum)
            #df11=pv.reset_index()
            #print(df11)
            #df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['Total Recharge Count'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Total Recharge Count':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            print(new_customdata)
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'],
                                  textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Total Recharge Count'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text',
                               hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Recharge Count</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)

            #chart2=px.scatter(df12, x='Week_Day_Count', y='Total Recharge Count',trendline="lowess")
            #chart2=px.line(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)
        
                                                               
            if radio_items5_value == "week":
                pv = pd.pivot_table(filtered_df_month1, values=['Total Recharge Count'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Total Recharge Count':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

#                 df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Total Recharge Count'],groupnorm='percent',customdata=new_customdata,
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',
                                      hoverinfo='text'
                                      ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},autosize=True,
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.scatter(df12, x='Week_Day_Count', y='Total Recharge Count',trendline="lowess")
                #chart2=px.line(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['Total Recharge Count'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                print(df15)
                new_customdata = df15.iloc[:,0:1]
                print(new_customdata)
                #chart2=px.scatter(df15, x='Date', y='Total Recharge Count',trendline="lowess")
                data = go.Scatter(x=df15['Date'], y=df15['Total Recharge Count'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Total Recharge Count'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                      ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Daily Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                
                #chart2=px.line(df15, x='Date', y='Total Recharge Count')
            if radio_items5_value == "month":
                
                pv = pd.pivot_table(filtered_df_month1, values=['Total Recharge Count'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Total Recharge Count')
                print(df7)    
                new_customdata = df7.iloc[:,0:1]
                data = go.Scatter(x=df7['Month_Name'], y=df7['Total Recharge Count'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Total Recharge Count'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
                #chart2=px.line(df7, x='Month_Name', y='Total Recharge Count')
            
            if radio_items5_value == "dayname":
                pv = pd.pivot_table(filtered_df_month1, values=['Total Recharge Count'],index=['Name of Day'],aggfunc=np.sum)
                df16=pv.reset_index()
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                df_weekday1 = df16.groupby(['Name of Day']).sum().reindex(cats)
                df16=df_weekday1.reset_index()
                df16            
                print(df16)
                new_customdata = df16.iloc[:,0:1]
                data = go.Scatter(x=df16['Name of Day'], y=df16['Total Recharge Count'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Total Recharge Count'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day Trend</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
                #chart2=px.line(df16, x='Name of Day', y='Total Recharge Count')

        if radio_items6_value == "A":

            #global df11,pv
            #if delta>=30:
            #pv=pd.pivot_table(filtered_df_month1,values=['Total Recharge Count'],index=['Month_Name'],aggfunc=np.sum)
            #df11=pv.reset_index()
            #print(df11)
            #df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['Total Recharge Count'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Total Recharge Count':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'],
                                  textposition='auto',marker=dict(color='#800000'),
                                  text=df12['Total Recharge Count'],
                                  texttemplate= '%{text:,.3s}',customdata=new_customdata,
                                  hoverinfo='text'
                                  ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Recharge Count</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)
        
                                                               
            if radio_items5_value == "week":
                pv = pd.pivot_table(filtered_df_month1, values=['Total Recharge Count'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Total Recharge Count':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df12['Total Recharge Count'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['Total Recharge Count'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                print(df15)
                new_customdata = df15.iloc[:,0:1]
                data = go.Bar(x=df15['Date'], y=df15['Total Recharge Count'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df15['Total Recharge Count'],customdata=new_customdata,
                              texttemplate='%{text:,.2s}',
                              hoverinfo='text'
                              ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df15, x='Date', y='Total Recharge Count')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "month":
               
                pv = pd.pivot_table(filtered_df_month1, values=['Total Recharge Count'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Total Recharge Count')
                print(df7)    
                new_customdata = df7.iloc[:,0:1]
                data = go.Bar(x=df7['Month_Name'], y=df7['Total Recharge Count'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df7['Total Recharge Count'],customdata=new_customdata,
                              texttemplate='%{text:,.3s}',
                              hoverinfo='text'
                              ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "dayname":
                pv = pd.pivot_table(filtered_df_month1, values=['Total Recharge Count'],index=['Name of Day'],aggfunc=np.sum)
                df16=pv.reset_index()
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                df_weekday1 = df16.groupby(['Name of Day']).sum().reindex(cats)
                df16=df_weekday1.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Bar(x=df16['Name of Day'], y=df16['Total Recharge Count'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df16['Total Recharge Count'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df16, x='Name of Day', y='Total Recharge Count')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
                
    if demo_dropdown8_value == 'TR':
        if radio_items6_value == "B":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month1,values=['PRICE'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['PRICE'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'PRICE':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['PRICE'],
                                  textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['PRICE'],groupnorm='percent',
                                  texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                                  ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)

            #chart2=px.line(df12, x='Week_Day_Count', y='PRICE')
            #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['PRICE'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "week":
                
                pv=pd.pivot_table(filtered_df_month1,values=['PRICE'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month1, values=['PRICE'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'PRICE':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['PRICE'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['PRICE'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                      ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
                #chart2=px.line(df12, x='Week_Day_Count', y='PRICE')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['PRICE'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['PRICE'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                print(df15)
                new_customdata = df15.iloc[:,0:1]
                data = go.Scatter(x=df15['Date'], y=df15['PRICE'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['PRICE'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.line(df15, x='Date', y='PRICE')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "month":
                pv = pd.pivot_table(filtered_df_month1, values=['PRICE'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='PRICE')            
                print(df7)
                new_customdata = df7.iloc[:,0:1]
                data = go.Scatter(x=df7['Month_Name'], y=df7['PRICE'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['PRICE'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.line(df7, x='Month_Name', y='PRICE')
                #chart2=px.scatter(df7, x='Month_Name', y='PRICE',trendline="lowess")
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "dayname":
                pv = pd.pivot_table(filtered_df_month1, values=['PRICE'],index=['Name of Day'],aggfunc=np.sum)
                df16=pv.reset_index()

                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                df_weekday1 = df16.groupby(['Name of Day']).sum().reindex(cats)
                df16=pv.reset_index()
                print(df16)  
                new_customdata = df16.iloc[:,0:1]
                data = go.Scatter(x=df16['Name of Day'], y=df16['PRICE'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['PRICE'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
        if radio_items6_value == "A":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month1,values=['PRICE'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['PRICE'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)
            df12=df14.groupby('Week_Trend').agg({'PRICE':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['PRICE'],
                                  textposition='auto',marker=dict(color='#800000'),
                                  text=df12['PRICE'],
                                  texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                  hoverinfo='text'
                                  ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))
            chart2 = go.Figure(data=data, layout=layout)
            #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['PRICE'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)


            if radio_items5_value == "week":
                pv=pd.pivot_table(filtered_df_month1,values=['PRICE'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month1, values=['PRICE'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)
                df12=df14.groupby('Week_Trend').agg({'PRICE':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['PRICE'],
                                      textposition='auto',marker=dict(color='#800000'),
                                      text=df12['PRICE'],
                                      texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                      hoverinfo='text'
                                      ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))
                chart2 = go.Figure(data=data, layout=layout)

                #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['PRICE'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['PRICE'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                print(df15)    
                new_customdata = df15.iloc[:,0:1]
                data = go.Bar(x=df15['Date'], y=df15['PRICE'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df15['PRICE'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.bar(df15, x='Date', y='PRICE')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "month":
                pv = pd.pivot_table(filtered_df_month1, values=['PRICE'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='PRICE')            
                print(df7)    
                new_customdata = df7.iloc[:,0:1]
                data = go.Bar(x=df7['Month_Name'], y=df7['PRICE'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df7['PRICE'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df7, x='Month_Name', y='PRICE')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "dayname":
                
                pv = pd.pivot_table(filtered_df_month1, values=['PRICE'],index=['Name of Day'],aggfunc=np.sum)
                df16=pv.reset_index()
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                df_weekday1 = df16.groupby(['Name of Day']).sum().reindex(cats)
                df16=df_weekday1.reset_index()
                print(df16)
                new_customdata = df16.iloc[:,0:1]
                data = go.Bar(x=df16['Name of Day'], y=df16['PRICE'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df16['PRICE'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df16, x='Name of Day', y='PRICE')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

    if demo_dropdown8_value == 'TDB':
        if radio_items6_value == "B":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month1,values=['Data_Benefit'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['Data_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Data_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Benefit'],
                                  textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Data_Benefit'],groupnorm='percent',
                                  texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                                  ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)
            
            #chart2=px.line(df12, x='Week_Day_Count', y='Data_Benefit')
            #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Benefit'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)


            if radio_items5_value == "week":
                pv=pd.pivot_table(filtered_df_month1,values=['Data_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Data_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]

                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Data_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                      ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
                #chart2=px.line(df12, x='Week_Day_Count', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Benefit'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Benefit'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                print(df15)   
                new_customdata = df15.iloc[:,0:1]
                data = go.Scatter(x=df15['Date'], y=df15['Data_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Data_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
                #chart2=px.line(df15, x='Date', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "month":
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Data_Benefit')            
                print(df7)    
                new_customdata = df7.iloc[:,0:1]
                data = go.Scatter(x=df7['Month_Name'], y=df7['Data_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Data_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
                #chart2=px.scatter(df7, x='Month_Name', y='Data_Benefit',trendline="lowess")
                #chart2=px.line(df7, x='Month_Name', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Benefit'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                print(df16)
                new_customdata = df16.iloc[:,0:1]
                data = go.Scatter(x=df16['Name of Day'], y=df16['Data_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Data_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.scatter(df16, x='Name of Day', y='Data_Benefit',trendline="lowess")
                #chart2=px.line(df16, x='Name of Day', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
        if radio_items6_value == "A":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month1,values=['Data_Benefit'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['Data_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Data_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Benefit'],
                                  textposition='auto',marker=dict(color='#800000'),
                                  text=df12['Data_Benefit'],
                                  texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                  hoverinfo='text'
                          ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))
            chart2 = go.Figure(data=data, layout=layout)
            #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Benefit'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)


            if radio_items5_value == "week":
                pv=pd.pivot_table(filtered_df_month1,values=['Data_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Data_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Benefit'],
                                      textposition='auto',marker=dict(color='#800000'),
                                      text=df12['Data_Benefit'],
                                      texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                      hoverinfo='text'
                              ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))
                chart2 = go.Figure(data=data, layout=layout)
                #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Benefit'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Benefit'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                print(df15)
                new_customdata = df15.iloc[:,0:1]
                data = go.Bar(x=df15['Date'], y=df15['Data_Benefit'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df15['Data_Benefit'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df15, x='Date', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "month":
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Data_Benefit') 
                new_customdata = df7.iloc[:,0:1]
                print(df7)
                data = go.Bar(x=df7['Month_Name'], y=df7['Data_Benefit'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df7['Data_Benefit'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.bar(df7, x='Month_Name', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Benefit'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Bar(x=df16['Name of Day'], y=df16['Data_Benefit'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df16['Data_Benefit'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df16, x='Name of Day', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)


    if demo_dropdown8_value == 'TVB':
        if radio_items6_value == "B":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month1,values=['Voice_Benefit'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['Voice_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Voice_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            #chart2=px.line(df12, x='Week_Day_Count', y='Voice_Benefit')
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Voice_Benefit'],
                                  textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Voice_Benefit'],groupnorm='percent',
                                  texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                              ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)


            if radio_items5_value == "week":
                pv=pd.pivot_table(filtered_df_month1,values=['Voice_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Voice_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                #chart2=px.line(df12, x='Week_Day_Count', y='Voice_Benefit')
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Voice_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Voice_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Benefit'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)    
                data = go.Scatter(x=df15['Date'], y=df15['Voice_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Voice_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "month":
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Voice_Benefit')  
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                data = go.Scatter(x=df7['Month_Name'], y=df7['Voice_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Voice_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.scatter(df7, x='Month_Name', y='Voice_Benefit',trendline="lowess")
                #chart2=px.line(df7, x='Month_Name', y='Voice_Benefit')
            if radio_items5_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Benefit'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Scatter(x=df16['Name of Day'], y=df16['Voice_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Voice_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Weekday Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
                #chart2=px.line(df16, x='Name of Day', y='Voice_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
        if radio_items6_value == "A":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month1,values=['Voice_Benefit'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['Voice_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Voice_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Voice_Benefit'],
                                  textposition='auto',marker=dict(color='#800000'),
                                  text=df12['Voice_Benefit'],
                                  texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                  hoverinfo='text'
                          ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))
            chart2 = go.Figure(data=data, layout=layout)
            #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Voice_Benefit'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)


            if radio_items5_value == "week":
                pv=pd.pivot_table(filtered_df_month1,values=['Voice_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Voice_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Voice_Benefit'],
                                      textposition='auto',marker=dict(color='#800000'),
                                      text=df12['Voice_Benefit'],
                                      texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                      hoverinfo='text'
                              ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))
                chart2 = go.Figure(data=data, layout=layout)
                #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Voice_Benefit'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Benefit'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)    
                data = go.Bar(x=df15['Date'], y=df15['Voice_Benefit'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df15['Voice_Benefit'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.bar(df15, x='Date', y='Voice_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "month":
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Voice_Benefit')
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                data = go.Bar(x=df7['Month_Name'], y=df7['Voice_Benefit'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df7['Voice_Benefit'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df7, x='Month_Name', y='Voice_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Benefit'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Bar(x=df16['Name of Day'], y=df16['Voice_Benefit'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df16['Voice_Benefit'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df16, x='Name of Day', y='Voice_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
                

    if demo_dropdown8_value == 'TDP':
        if radio_items6_value == "B":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month1,values=['Data_Price'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['Data_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Data_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Price'],
                                  textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Data_Price'],groupnorm='percent',
                                  texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                              ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)

            #chart2=px.line(df12, x='Week_Day_Count', y='Data_Price')
            ##chart2=px.scatter(df12, x='Week_Day_Count', y='Data_Price',trendline="lowess")
            #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Price'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)


            if radio_items5_value == "week":
                pv=pd.pivot_table(filtered_df_month1,values=['Data_Price'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Data_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Price'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Data_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.line(df12, x='Week_Day_Count', y='Data_Price')
                #chart2=px.scatter(df12, x='Week_Day_Count', y='Data_Price',trendline="lowess")
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Price'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Price'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)   
                data = go.Scatter(x=df15['Date'], y=df15['Data_Price'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Data_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "month":
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Price'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Data_Price')  
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                data = go.Scatter(x=df7['Month_Name'], y=df7['Data_Price'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Data_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.line(df7, x='Month_Name', y='Data_Price')
            if radio_items5_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Price'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                #chart2=px.line(df16, x='Name of Day', y='Data_Price')
                data = go.Scatter(x=df16['Name of Day'], y=df16['Data_Price'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Data_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

        if radio_items6_value == "A":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month1,values=['Data_Price'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['Data_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Data_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Price'],
                                  textposition='auto',marker=dict(color='#800000'),
                                  text=df12['Data_Price'],
                                  texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                  hoverinfo='text'
                          ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week Trend</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))
            chart2 = go.Figure(data=data, layout=layout)
            #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Price'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)


            if radio_items5_value == "week":
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Data_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Price'],
                                      textposition='auto',marker=dict(color='#800000'),
                                      text=df12['Data_Price'],
                                      texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                      hoverinfo='text'
                              ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Trend</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))
                chart2 = go.Figure(data=data, layout=layout)
                #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Price'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Price'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)
                data = go.Bar(x=df15['Date'], y=df15['Data_Price'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df15['Data_Price'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #df7=df15.groupby('Week_Trend').agg({'Total Recharge Count':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                #print(df12)
                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                #print(df12)

                #chart2=px.bar(df15, x='Date', y='Data_Price')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "month":
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Price'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Data_Price') 
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                #chart2=px.bar(df7, x='Month_Name', y='Data_Price')
                data = go.Bar(x=df7['Month_Name'], y=df7['Data_Price'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df7['Data_Price'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month1, values=['Data_Price'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Bar(x=df16['Name of Day'], y=df16['Data_Price'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df16['Data_Price'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df16, x='Name of Day', y='Data_Price')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
                

    if demo_dropdown8_value == 'TVP':
        if radio_items6_value == "B":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month1,values=['Voice_Price'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['Voice_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Voice_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Voice_Price'],
                                  textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Voice_Price'],groupnorm='percent',
                                  texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                              ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)
            
            if radio_items5_value == "week":
                pv=pd.pivot_table(filtered_df_month1,values=['Voice_Price'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Voice_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Voice_Price'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Voice_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))
                chart2 = go.Figure(data=data, layout=layout)    
            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Price'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)    
                data = go.Scatter(x=df15['Date'], y=df15['Voice_Price'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Voice_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
    
            if radio_items5_value == "month":
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Price'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Voice_Price')
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                #chart2=px.line(df7, x='Month_Name', y='Voice_Price')
                data = go.Scatter(x=df7['Month_Name'], y=df7['Voice_Price'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Voice_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Price'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Scatter(x=df16['Name of Day'], y=df16['Voice_Price'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Voice_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

        if radio_items6_value == "A":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month1,values=['Voice_Price'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['Voice_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Voice_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Voice_Price'],
                                  textposition='auto',marker=dict(color='#800000'),
                                  text=df12['Voice_Price'],
                                  texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                  hoverinfo='text'
                          ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "week":
                pv=pd.pivot_table(filtered_df_month1,values=['Voice_Price'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Voice_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Voice_Price'],
                                      textposition='auto',marker=dict(color='#800000'),
                                      text=df12['Voice_Price'],
                                      texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                      hoverinfo='text'
                              ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Price'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)    
                data = go.Bar(x=df15['Date'], y=df15['Voice_Price'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df15['Voice_Price'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df15, x='Date', y='Voice_Price')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "month":
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Price'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Voice_Price')
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                data = go.Bar(x=df7['Month_Name'], y=df7['Voice_Price'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df7['Voice_Price'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df7, x='Month_Name', y='Voice_Price')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month1, values=['Voice_Price'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Bar(x=df16['Name of Day'], y=df16['Voice_Price'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df16['Voice_Price'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


    if demo_dropdown8_value == 'TCP':
        if radio_items6_value == "B":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month1,values=['Combo_Price'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['Combo_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Combo_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
            new_customdata = df12.iloc[:,4:5]
            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Combo_Price'],
                                  textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Combo_Price'],groupnorm='percent',
                                  texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                              ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)


            if radio_items5_value == "week":
                pv=pd.pivot_table(filtered_df_month1,values=['Combo_Price'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month1, values=['Combo_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Combo_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
                new_customdata = df12.iloc[:,4:5]
                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Combo_Price'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Combo_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['Combo_Price'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)  
                data = go.Scatter(x=df15['Date'], y=df15['Combo_Price'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Combo_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
            if radio_items5_value == "month":
                pv = pd.pivot_table(filtered_df_month1, values=['Combo_Price'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Combo_Price')
                new_customdata = df7.iloc[:,0:1]
                print(df7)   
                data = go.Scatter(x=df7['Month_Name'], y=df7['Combo_Price'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Combo_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month1, values=['Combo_Price'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)   
                data = go.Scatter(x=df16['Name of Day'], y=df16['Combo_Price'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Combo_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

        if radio_items6_value == "A":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month1,values=['Combo_Price'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month1, values=['Combo_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Combo_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
            new_customdata = df12.iloc[:,4:5]
            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Combo_Price'],
                                  textposition='auto',marker=dict(color='#800000'),
                                  text=df12['Combo_Price'],
                                  texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                  hoverinfo='text'
                          ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)


            if radio_items5_value == "week":
                pv=pd.pivot_table(filtered_df_month1,values=['Combo_Price'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month1, values=['Combo_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Combo_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
                new_customdata = df12.iloc[:,4:5]
                print(df12)
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Combo_Price'],
                                      textposition='auto',marker=dict(color='#800000'),
                                      text=df12['Combo_Price'],
                                      texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                      hoverinfo='text'
                              ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


            if radio_items5_value == "day":
                pv = pd.pivot_table(filtered_df_month1, values=['Combo_Price'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)    
                data = go.Bar(x=df15['Date'], y=df15['Combo_Price'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df15['Combo_Price'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "month":
                pv = pd.pivot_table(filtered_df_month1, values=['Combo_Price'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Combo_Price')
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                data = go.Bar(x=df7['Month_Name'], y=df7['Combo_Price'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df7['Combo_Price'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

            if radio_items5_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month1, values=['Combo_Price'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Bar(x=df16['Name of Day'], y=df16['Combo_Price'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df16['Combo_Price'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df16, x='Name of Day', y='Combo_Price')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)


    if demo_dropdown8_value == 'Active':
        if radio_items6_value == "B":
            
            #if delta>=30:
            filtered_df_month1=filtered_df_month1.drop_duplicates(subset='CONSUMER_ID', keep="last")
            filtered_df_month1['Active Customer']=1
            print(filtered_df_month1)
            pv = pd.pivot_table(filtered_df_month1, values=['Active Customer'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            df12=df14.groupby('Week_Trend').agg({'Active Customer':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
            new_customdata = df12.iloc[:,4:5]        
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Active Customer'],
                                  textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Active Customer'],groupnorm='percent',
                                  texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                              ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Active Customer Count</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)
            
            #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Active Customer']),])
            #chart2=px.line(df12, x='Week_Day_Count', y='Active Customer')
            #chart2=px.scatter(df12, x='Week_Day_Count', y='Active Customer',trendline="lowess")

            if radio_items5_value == "week":
                filtered_df_month1=filtered_df_month1.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month1['Active Customer']=1
                print(filtered_df_month1)
                pv = pd.pivot_table(filtered_df_month1, values=['Active Customer'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                df12=df14.groupby('Week_Trend').agg({'Active Customer':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
                new_customdata = df12.iloc[:,4:5]        
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Active Customer'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Active Customer'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.scatter(df12, x='Week_Day_Count', y='Active Customer',trendline="lowess")    
                #chart2=px.line(df12, x='Week_Day_Count', y='Active Customer')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Active Customer']),])

            if radio_items5_value == "day":
                filtered_df_month1=filtered_df_month1.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month1['Active Customer']=1

                pv = pd.pivot_table(filtered_df_month1, values=['Active Customer'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                data = go.Scatter(x=df15['Date'], y=df15['Active Customer'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Active Customer'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.scatter(df15, x='Date', y='Active Customer',trendline="lowess")
                #chart2=px.line(df15, x='Date', y='Active Customer')

            if radio_items5_value == "month":
                filtered_df_month1=filtered_df_month1.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month1['Active Customer']=1

                pv = pd.pivot_table(filtered_df_month1, values=['Active Customer'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Active Customer')
                new_customdata = df7.iloc[:,0:1]
                data = go.Scatter(x=df7['Month_Name'], y=df7['Active Customer'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Active Customer'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.scatter(df7, x='Month_Name', y='Active Customer',trendline="lowess")
                #chart2=px.line(df7, x='Month_Name', y='Active Customer')

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "dayname":
                filtered_df_month1=filtered_df_month1.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month1['Active Customer']=1

                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month1, values=['Active Customer'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                #chart2=px.scatter(df16, x='Name of Day', y='Active Customer',trendline="lowess")
                #chart2=px.line(df16, x='Name of Day', y='Active Customer')
                data = go.Scatter(x=df16['Name of Day'], y=df16['Active Customer'],
                                      textposition='bottom left',marker=dict(color='#800000', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Active Customer'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

        if radio_items6_value == "A":
            
            #if delta>=30:
            filtered_df_month1=filtered_df_month1.drop_duplicates(subset='CONSUMER_ID', keep="last")
            filtered_df_month1['Active Customer']=1
            print(filtered_df_month1)
            pv = pd.pivot_table(filtered_df_month1, values=['Active Customer'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            df12=df14.groupby('Week_Trend').agg({'Active Customer':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
            new_customdata = df12.iloc[:,4:5]
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Active Customer'],
                                  textposition='auto',marker=dict(color='#800000'),
                                  text=df12['Active Customer'],
                                  texttemplate= '%{text:,.3s}',customdata=new_customdata,
                                  hoverinfo='text'
                          ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Active Customer Count</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)
            #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Active Customer']),])


            if radio_items5_value == "week":
                filtered_df_month1=filtered_df_month1.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month1['Active Customer']=1
                print(filtered_df_month1)
                pv = pd.pivot_table(filtered_df_month1, values=['Active Customer'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                df12=df14.groupby('Week_Trend').agg({'Active Customer':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Active Customer'],
                                      textposition='auto',marker=dict(color='#800000'),
                                      text=df12['Active Customer'],
                                      texttemplate= '%{text:,.3s}',customdata=new_customdata,
                                      hoverinfo='text'
                              ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0',plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                    #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Active Customer']),])

            if radio_items5_value == "day":
                filtered_df_month1=filtered_df_month1.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month1['Active Customer']=1

                pv = pd.pivot_table(filtered_df_month1, values=['Active Customer'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                data = go.Bar(x=df15['Date'], y=df15['Active Customer'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df15['Active Customer'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.bar(df15, x='Date', y='Active Customer')

            if radio_items5_value == "month":
                filtered_df_month1=filtered_df_month1.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month1['Active Customer']=1

                pv = pd.pivot_table(filtered_df_month1, values=['Active Customer'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Active Customer')
                new_customdata = df7.iloc[:,0:1]

                data = go.Bar(x=df7['Month_Name'], y=df7['Active Customer'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df7['Active Customer'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df7, x='Month_Name', y='Active Customer')

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items5_value == "dayname":
                filtered_df_month1=filtered_df_month1.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month1['Active Customer']=1

                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month1, values=['Active Customer'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                data = go.Bar(x=df16['Name of Day'], y=df16['Active Customer'],
                              textposition='auto', marker=dict(color='#800000'),
                              text=df16['Active Customer'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#C0C0C0', plot_bgcolor='#C0C0C0',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df16, x='Name of Day', y='Active Customer')
    
    df1 = filtered_df_month1
    #df1=df1.drop(df1[['Date','Month','Day','WeekNum','Name of Day','Month_Name','Week','Week_Trend','Day_Trend']],axis=1)
    # tooltip_data= [{i: {'value': i,'use_with': 'both'} for i in df.columns}]
    col = [{"name": i, "id": i, "hideable": "last"} for i in df.columns]
    df1 = df1.to_dict('records')
            
    return chart2,df1, col                                                           
@app.callback(Output("output-3", "children"),
              [Input("save-button", "n_clicks"),
               ],
              [State("table", "data")],)

def selected_data_to_csv(nclicks, table):
    if nclicks == 0:
        raise PreventUpdate
    else:
        # df=pd.DataFrame(table1)
        # pd.DataFrame(table1).to_csv('C://Users//ch-e05138//Desktop//New folder//gaurav.csv',index=False)
        save_path = 'C:/Users/ch-e05138/Desktop/New folder/'
        file_name =  "Analyze_Trend.csv"
        print(file_name)
        completeName = os.path.join(save_path, file_name)
        print(completeName)
        pd.DataFrame(table).to_csv(completeName, index=False)

        # df.to_csv(completeName,index=False)
        # print(completeName)
        # file1 = open(completeName, "w")
        # file1.write("file")
        # file1.close()
        # send_data_frame(df.to_csv, value+".csv", index=False)
        # return completeName
        # return send_data_frame(df.to_csv, value+".csv", index=False)

        return "Data Saved"

@app.callback(Output('bar-chart4', 'figure'),
              Output('table', 'data'),
              Output('table', 'columns'),
              #Output("date_picker_sales","start_date"),
               Input('demo_dropdown','value'),
               Input("date_picker_sales","start_date"),
               Input("date_picker_sales","end_date"),
               Input('demo_dropdown4','value'),
               Input('demo_dropdown6','value'),
               Input('demo_dropdown7','value'),
              Input('radio_items3','value'),
              Input('radio_items4','value'),
              )


def display_graphs(demo_dropdown_value,date_picker_sales_start_date, date_picker_sales_end_date,demo_dropdown4_value, demo_dropdown6_value,demo_dropdown7_value,radio_items3_value,radio_items4_value):
    
    
    #df = pd.read_csv(r'Dashboard_Input_Sample_0.1Mn.csv')
    #df = pd.read_csv(r'Dashboard_Input_Sample_10k.csv')
    #df = pd.read_csv(r'Dashboard_Input_Sample_50k.csv')
    #df = pd.read_csv(r'Dashboard_Input_Sample_0.5Mn.csv')
    #print(demo_dropdown_value)
    df =load_data()
    #print(df)
    global chart2,df2,pv,df4,df3,df5,df6,df8,df_weekday
    if demo_dropdown_value == []:
        #print(demo_dropdown_value)
        
        filtered_df_month = df
        start=filtered_df_month['TRX_DATE'].min()
        #df2=pd.pivot_table(data=filtered_df_month, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        #print(filtered_df_month)
        chart1 = {'data': []}

    elif demo_dropdown_value == ['Full Base']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        #filtered_df_month = filtered_df_month[filtered_df_month['Full_Base'] == ]
        #filtered_df_month = df[(df['CG/TG'].isin(a))]    
        #df3=pd.pivot_table(data=filtered_df_month, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()

    elif demo_dropdown_value == ['Full Base','CG']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month = df[(df['Full_Base'].isin(b))] 
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown_value == ['Full Base','TG']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        #filtered_df_month = filtered_df_month[filtered_df_month['Full_Base'] == ]
        #filtered_df_month = df[(df['CG/TG'].isin(a))]    
        
    elif demo_dropdown_value == ['TG','Full Base']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        
    elif demo_dropdown_value == ['CG','Full Base']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
  

    elif demo_dropdown_value == ['Full Base','CG','TG']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        
    elif demo_dropdown_value == ['Full Base','TG','CG']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        
    elif demo_dropdown_value == ['CG','TG','Full Base']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        
    elif demo_dropdown_value == ['TG','CG','Full Base']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        
    elif demo_dropdown_value == ['CG','Full Base','TG']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        
    elif demo_dropdown_value == ['TG','Full Base','CG']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        
        
    elif demo_dropdown_value == ['CG','TG']:
        a=[]
        for i in demo_dropdown_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month = df[(df['CG/TG'].isin(a))]  
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month )
        #filtered_df_month = df[df['CG/TG'] == demo_dropdown_value]
            #print(filtered_df_month)
            #df1 = df.groupby('CG/TG', as_index=False)['Voice_Benefit'].agg({'Sum_value': 'sum'})

    elif demo_dropdown_value == ['CG']:
        a=[]
        for i in demo_dropdown_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month = df[(df['CG/TG'].isin(a))]  
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        print(start)
    elif demo_dropdown_value == ['TG']:
        a=[]
        for i in demo_dropdown_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month = df[(df['CG/TG'].isin(a))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)    
###################################################        
    if demo_dropdown4_value == []:
        #print(demo_dropdown_value)
        filtered_df_month = filtered_df_month
        #df2=pd.pivot_table(data=filtered_df_month, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        print(filtered_df_month)
        chart1 = {'data': []}

    elif demo_dropdown4_value == ['All']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
#        print(b)
#        b[0]="Full Base"
#        print(b)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type_ALL'].isin(b))]    
        print(filtered_df_month)
    
    elif demo_dropdown4_value == ['Data']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        print(start)
        
    elif demo_dropdown4_value == ['Voice']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown4_value == ['Combo']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown4_value == ['Voice','Combo']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown4_value == ['Voice','Data']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        
    elif demo_dropdown4_value == ['Data','Voice']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown4_value == ['Combo','Voice']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown4_value == ['Combo','Data']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown4_value == ['Data','Combo']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown4_value == ['Data','Voice','Combo']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        
    elif demo_dropdown4_value == ['Data','Voice','Combo']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown4_value == ['Voice','Data','Combo']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown4_value == ['Voice','Combo','Data']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown4_value == ['Combo','Voice','Data']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))] 
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown4_value == ['Combo','Data','Voice']:
        print(demo_dropdown4_value)
        b=[]
        for i in demo_dropdown4_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Type'].isin(b))]
        print(filtered_df_month)
    if demo_dropdown6_value == []:
        #print(demo_dropdown_value)
        filtered_df_month = filtered_df_month
        #df2=pd.pivot_table(data=filtered_df_month, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        print(filtered_df_month)
        chart1 = {'data': []}

    elif demo_dropdown6_value == ['All']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
#        print(b)
#        b[0]="Full Base"
#        print(b)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity_ALL'].isin(b))]    
        print(filtered_df_month)
    
    elif demo_dropdown6_value == ['Daily']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        print(start)
        
    elif demo_dropdown6_value == ['Weekly']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown6_value == ['Monthly']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown6_value == ['Daily','Weekly']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown6_value == ['Daily','Monthly']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        
    elif demo_dropdown6_value == ['Weekly','Daily']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown6_value == ['Weekly','Monthly']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown6_value == ['Monthly','Daily']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown6_value == ['Monthly','Weekly']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown6_value == ['Daily','Weekly','Monthly']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        
    elif demo_dropdown6_value == ['Daily','Monthly','Weekly']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown6_value == ['Weekly','Daily','Monthly']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown6_value == ['Weekly','Monthly','Daily']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown6_value == ['Monthly','Weekly','Daily']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))] 
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)

    elif demo_dropdown6_value == ['Monthly','Daily','Weekly']:
        print(demo_dropdown6_value)
        b=[]
        for i in demo_dropdown6_value:
            b.append(i)
        filtered_df_month = filtered_df_month[(filtered_df_month['Validity'].isin(b))]
        start=filtered_df_month['TRX_DATE'].min()
        print(filtered_df_month)
        
    if date_picker_sales_start_date == None and date_picker_sales_end_date == None:
        #print(demo_dropdown_value)
        filtered_df_month = filtered_df_month
        #df2=pd.pivot_table(data=filtered_df_month, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        print(filtered_df_month)
        chart1 = {'data': []}
    elif date_picker_sales_start_date != None and date_picker_sales_end_date != None:
        
        print(date_picker_sales_start_date)
        print(date_picker_sales_end_date)
        global pv,chart,df3
        #filtered_df_month=filtered_df_month[(filtered_df_month['Date']>date_picker_sales_start_date)&(filtered_df_month['Date']<date_picker_sales_end_date)]
        print(filtered_df_month)
        filtered_df_month['Date']=pd.to_datetime(filtered_df_month['TRX_DATE'],errors = 'coerce')
        filtered_df_month['Month']=filtered_df_month['Date'].dt.month
        filtered_df_month['Day']=filtered_df_month['Date'].dt.day
        #filtered_df_month['WeekNum'] = filtered_df_month['Date'].dt.week
        filtered_df_month['WeekNum'] = filtered_df_month['Date'].dt.strftime('%W')
        filtered_df_month['Name of Day']=filtered_df_month['Date'].dt.day_name()
        #filtered_df_month['WeekNum'] = filtered_df_month['WeekNum'].replace([53], 1)
        filtered_df_month['Month_Name']=filtered_df_month['Month'].apply(lambda x:calendar.month_abbr[x])
        filtered_df_month["Week"]=str(' Week')
        filtered_df_month["Week_Trend"] = filtered_df_month["WeekNum"].astype(str) + filtered_df_month["Week"]
        filtered_df_month["Day_Trend"] = filtered_df_month["Day"].astype(str) + filtered_df_month["Month_Name"]
        
        date_entry=date_picker_sales_start_date
        year,month,day=map(int,date_entry.split('-'))
        start_date=datetime(year,month,day)

        date_entry1=date_picker_sales_end_date
        year,month,day=map(int,date_entry1.split('-'))
        end_date=datetime(year,month,day)

        date33=end_date
        date11=start_date

        print(date11)
        print(date33)
        mdate1=date11
        rdate1=date33
        delta=(rdate1-mdate1).days
        print(delta)
        filtered_df_month=filtered_df_month[(filtered_df_month['Date']>=date11)&(filtered_df_month['Date']<=date33)]
        print(filtered_df_month)
    if demo_dropdown7_value == "":
        #global df3
        #df3 = df2
        #df2=pd.pivot_table(data=filtered_df_month, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        print(df3)
        chart1 = {'data': []}
    if demo_dropdown7_value == 'TRC':
        if radio_items4_value == "B":
            print(filtered_df_month)
            global df11,pv
            #if delta>=30:
            #pv=pd.pivot_table(filtered_df_month,values=['Total Recharge Count'],index=['Month_Name'],aggfunc=np.sum)
            #df11=pv.reset_index()
            #print(df11)
            #df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['Total Recharge Count'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Total Recharge Count':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            print(new_customdata)
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'],
                                  textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Total Recharge Count'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text',
                               hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Recharge Count</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)

            #chart2=px.scatter(df12, x='Week_Day_Count', y='Total Recharge Count',trendline="lowess")
            #chart2=px.line(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)
        
                                                               
            if radio_items3_value == "week":
                pv = pd.pivot_table(filtered_df_month, values=['Total Recharge Count'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Total Recharge Count':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

#                 df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Total Recharge Count'],groupnorm='percent',customdata=new_customdata,
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',
                                      hoverinfo='text'
                                      ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},autosize=True,
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.scatter(df12, x='Week_Day_Count', y='Total Recharge Count',trendline="lowess")
                #chart2=px.line(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['Total Recharge Count'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                print(df15)
                new_customdata = df15.iloc[:,0:1]
                print(new_customdata)
                #chart2=px.scatter(df15, x='Date', y='Total Recharge Count',trendline="lowess")
                data = go.Scatter(x=df15['Date'], y=df15['Total Recharge Count'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Total Recharge Count'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                      ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Daily Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                
                #chart2=px.line(df15, x='Date', y='Total Recharge Count')
            if radio_items3_value == "month":
                
                pv = pd.pivot_table(filtered_df_month, values=['Total Recharge Count'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Total Recharge Count')
                print(df7)    
                new_customdata = df7.iloc[:,0:1]
                data = go.Scatter(x=df7['Month_Name'], y=df7['Total Recharge Count'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Total Recharge Count'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
                #chart2=px.line(df7, x='Month_Name', y='Total Recharge Count')
            
            if radio_items3_value == "dayname":
                pv = pd.pivot_table(filtered_df_month, values=['Total Recharge Count'],index=['Name of Day'],aggfunc=np.sum)
                df16=pv.reset_index()
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                df_weekday1 = df16.groupby(['Name of Day']).sum().reindex(cats)
                df16=df_weekday1.reset_index()
                df16            
                print(df16)
                new_customdata = df16.iloc[:,0:1]
                data = go.Scatter(x=df16['Name of Day'], y=df16['Total Recharge Count'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Total Recharge Count'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day Trend</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
                #chart2=px.line(df16, x='Name of Day', y='Total Recharge Count')

        if radio_items4_value == "A":

            #global df11,pv
            #if delta>=30:
            #pv=pd.pivot_table(filtered_df_month,values=['Total Recharge Count'],index=['Month_Name'],aggfunc=np.sum)
            #df11=pv.reset_index()
            #print(df11)
            #df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['Total Recharge Count'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Total Recharge Count':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'],
                                  textposition='auto',marker=dict(color='#800080'),
                                  text=df12['Total Recharge Count'],
                                  texttemplate= '%{text:,.3s}',customdata=new_customdata,
                                  hoverinfo='text'
                                  ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Recharge Count</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)
        
                                                               
            if radio_items3_value == "week":
                pv = pd.pivot_table(filtered_df_month, values=['Total Recharge Count'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Total Recharge Count':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df12['Total Recharge Count'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['Total Recharge Count'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                print(df15)
                new_customdata = df15.iloc[:,0:1]
                data = go.Bar(x=df15['Date'], y=df15['Total Recharge Count'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df15['Total Recharge Count'],customdata=new_customdata,
                              texttemplate='%{text:,.2s}',
                              hoverinfo='text'
                              ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df15, x='Date', y='Total Recharge Count')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "month":
               
                pv = pd.pivot_table(filtered_df_month, values=['Total Recharge Count'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Total Recharge Count')
                print(df7)    
                new_customdata = df7.iloc[:,0:1]
                data = go.Bar(x=df7['Month_Name'], y=df7['Total Recharge Count'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df7['Total Recharge Count'],customdata=new_customdata,
                              texttemplate='%{text:,.3s}',
                              hoverinfo='text'
                              ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "dayname":
                pv = pd.pivot_table(filtered_df_month, values=['Total Recharge Count'],index=['Name of Day'],aggfunc=np.sum)
                df16=pv.reset_index()
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                df_weekday1 = df16.groupby(['Name of Day']).sum().reindex(cats)
                df16=df_weekday1.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Scatter(x=df16['Name of Day'], y=df16['Total Recharge Count'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Total Recharge Count'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day Trend</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Recharge Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df16, x='Name of Day', y='Total Recharge Count')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
                
    if demo_dropdown7_value == 'TR':
        if radio_items4_value == "B":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month,values=['PRICE'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['PRICE'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'PRICE':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['PRICE'],
                                  textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['PRICE'],groupnorm='percent',
                                  texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                                  ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)

            #chart2=px.line(df12, x='Week_Day_Count', y='PRICE')
            #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['PRICE'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "week":
                
                pv=pd.pivot_table(filtered_df_month,values=['PRICE'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month, values=['PRICE'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'PRICE':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['PRICE'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['PRICE'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                      ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
                #chart2=px.line(df12, x='Week_Day_Count', y='PRICE')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['PRICE'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['PRICE'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                print(df15)
                new_customdata = df15.iloc[:,0:1]
                data = go.Scatter(x=df15['Date'], y=df15['PRICE'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['PRICE'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.line(df15, x='Date', y='PRICE')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items3_value == "month":
                pv = pd.pivot_table(filtered_df_month, values=['PRICE'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='PRICE')            
                print(df7)
                new_customdata = df7.iloc[:,0:1]
                data = go.Scatter(x=df7['Month_Name'], y=df7['PRICE'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['PRICE'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.line(df7, x='Month_Name', y='PRICE')
                #chart2=px.scatter(df7, x='Month_Name', y='PRICE',trendline="lowess")
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "dayname":
                pv = pd.pivot_table(filtered_df_month, values=['PRICE'],index=['Name of Day'],aggfunc=np.sum)
                df16=pv.reset_index()

                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                df_weekday1 = df16.groupby(['Name of Day']).sum().reindex(cats)
                df16=pv.reset_index()
                print(df16)  
                new_customdata = df16.iloc[:,0:1]
                data = go.Scatter(x=df16['Name of Day'], y=df16['PRICE'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['PRICE'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
        if radio_items4_value == "A":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month,values=['PRICE'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['PRICE'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)
            df12=df14.groupby('Week_Trend').agg({'PRICE':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['PRICE'],
                                  textposition='auto',marker=dict(color='#800080'),
                                  text=df12['PRICE'],
                                  texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                  hoverinfo='text'
                                  ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))
            chart2 = go.Figure(data=data, layout=layout)
            #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['PRICE'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "week":
                pv=pd.pivot_table(filtered_df_month,values=['PRICE'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month, values=['PRICE'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)
                df12=df14.groupby('Week_Trend').agg({'PRICE':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['PRICE'],
                                      textposition='auto',marker=dict(color='#800080'),
                                      text=df12['PRICE'],
                                      texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                      hoverinfo='text'
                                      ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>',color='black',showline=False,showgrid=False))
                chart2 = go.Figure(data=data, layout=layout)


                #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['PRICE'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['PRICE'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                print(df15)    
                new_customdata = df15.iloc[:,0:1]
                data = go.Bar(x=df15['Date'], y=df15['PRICE'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df15['PRICE'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)



                #chart2=px.bar(df15, x='Date', y='PRICE')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "month":
                pv = pd.pivot_table(filtered_df_month, values=['PRICE'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='PRICE')            
                print(df7)    
                new_customdata = df7.iloc[:,0:1]
                data = go.Bar(x=df7['Month_Name'], y=df7['PRICE'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df7['PRICE'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df7, x='Month_Name', y='PRICE')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "dayname":
                
                pv = pd.pivot_table(filtered_df_month, values=['PRICE'],index=['Name of Day'],aggfunc=np.sum)
                df16=pv.reset_index()
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                df_weekday1 = df16.groupby(['Name of Day']).sum().reindex(cats)
                df16=df_weekday1.reset_index()
                print(df16)
                new_customdata = df16.iloc[:,0:1]
                data = go.Bar(x=df16['Name of Day'], y=df16['PRICE'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df16['PRICE'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Revenue:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Revenue</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df16, x='Name of Day', y='PRICE')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

    if demo_dropdown7_value == 'TDB':
        if radio_items4_value == "B":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month,values=['Data_Benefit'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['Data_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Data_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Benefit'],
                                  textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Data_Benefit'],groupnorm='percent',
                                  texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                                  ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)

            
            #chart2=px.line(df12, x='Week_Day_Count', y='Data_Benefit')
            #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Benefit'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "week":
                pv=pd.pivot_table(filtered_df_month,values=['Data_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month, values=['Data_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Data_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]

                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Data_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                      ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
                #chart2=px.line(df12, x='Week_Day_Count', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Benefit'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['Data_Benefit'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                print(df15)   
                new_customdata = df15.iloc[:,0:1]
                data = go.Scatter(x=df15['Date'], y=df15['Data_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Data_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                
                #chart2=px.line(df15, x='Date', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "month":
                pv = pd.pivot_table(filtered_df_month, values=['Data_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Data_Benefit')            
                print(df7)    
                new_customdata = df7.iloc[:,0:1]
                data = go.Scatter(x=df7['Month_Name'], y=df7['Data_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Data_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                
                #chart2=px.scatter(df7, x='Month_Name', y='Data_Benefit',trendline="lowess")
                #chart2=px.line(df7, x='Month_Name', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month, values=['Data_Benefit'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                print(df16)
                new_customdata = df16.iloc[:,0:1]
                data = go.Scatter(x=df16['Name of Day'], y=df16['Data_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Data_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.scatter(df16, x='Name of Day', y='Data_Benefit',trendline="lowess")
                #chart2=px.line(df16, x='Name of Day', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
        if radio_items4_value == "A":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month,values=['Data_Benefit'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['Data_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Data_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Benefit'],
                                  textposition='auto',marker=dict(color='#800080'),
                                  text=df12['Data_Benefit'],
                                  texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                  hoverinfo='text'
                          ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))
            chart2 = go.Figure(data=data, layout=layout)

            #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Benefit'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "week":
                pv=pd.pivot_table(filtered_df_month,values=['Data_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month, values=['Data_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Data_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Benefit'],
                                      textposition='auto',marker=dict(color='#800080'),
                                      text=df12['Data_Benefit'],
                                      texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                      hoverinfo='text'
                              ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>',color='black',showline=False,showgrid=False))
                chart2 = go.Figure(data=data, layout=layout)
                #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Benefit'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['Data_Benefit'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                print(df15)
                new_customdata = df15.iloc[:,0:1]
                data = go.Bar(x=df15['Date'], y=df15['Data_Benefit'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df15['Data_Benefit'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.bar(df15, x='Date', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "month":
                pv = pd.pivot_table(filtered_df_month, values=['Data_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Data_Benefit') 
                new_customdata = df7.iloc[:,0:1]
                print(df7)
                data = go.Bar(x=df7['Month_Name'], y=df7['Data_Benefit'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df7['Data_Benefit'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)



                #chart2=px.bar(df7, x='Month_Name', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month, values=['Data_Benefit'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Bar(x=df16['Name of Day'], y=df16['Data_Benefit'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df16['Data_Benefit'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Data Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Benefit</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df16, x='Name of Day', y='Data_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)


    if demo_dropdown7_value == 'TVB':
        if radio_items4_value == "B":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month,values=['Voice_Benefit'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['Voice_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Voice_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            #chart2=px.line(df12, x='Week_Day_Count', y='Voice_Benefit')
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Voice_Benefit'],
                                  textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Voice_Benefit'],groupnorm='percent',
                                  texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                              ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "week":
                pv=pd.pivot_table(filtered_df_month,values=['Voice_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Voice_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                #chart2=px.line(df12, x='Week_Day_Count', y='Voice_Benefit')
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Voice_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Voice_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Benefit'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)    
                data = go.Scatter(x=df15['Date'], y=df15['Voice_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Voice_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "month":
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Voice_Benefit')  
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                data = go.Scatter(x=df7['Month_Name'], y=df7['Voice_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Voice_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)



                #chart2=px.scatter(df7, x='Month_Name', y='Voice_Benefit',trendline="lowess")
                #chart2=px.line(df7, x='Month_Name', y='Voice_Benefit')
            if radio_items3_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Benefit'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Scatter(x=df16['Name of Day'], y=df16['Voice_Benefit'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Voice_Benefit'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Weekday Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                
                #chart2=px.line(df16, x='Name of Day', y='Voice_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
        if radio_items4_value == "A":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month,values=['Voice_Benefit'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['Voice_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Voice_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Voice_Benefit'],
                                  textposition='auto',marker=dict(color='#800080'),
                                  text=df12['Voice_Benefit'],
                                  texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                  hoverinfo='text'
                          ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))
            chart2 = go.Figure(data=data, layout=layout)

            #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Voice_Benefit'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "week":
                pv=pd.pivot_table(filtered_df_month,values=['Voice_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Benefit'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Voice_Benefit':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Voice_Benefit'],
                                      textposition='auto',marker=dict(color='#800080'),
                                      text=df12['Voice_Benefit'],
                                      texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                      hoverinfo='text'
                              ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>',color='black',showline=False,showgrid=False))
                chart2 = go.Figure(data=data, layout=layout)
                #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Voice_Benefit'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Benefit'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)    
                data = go.Bar(x=df15['Date'], y=df15['Voice_Benefit'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df15['Voice_Benefit'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.bar(df15, x='Date', y='Voice_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "month":
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Benefit'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Voice_Benefit')
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                data = go.Bar(x=df7['Month_Name'], y=df7['Voice_Benefit'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df7['Voice_Benefit'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.bar(df7, x='Month_Name', y='Voice_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Benefit'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Bar(x=df16['Name of Day'], y=df16['Voice_Benefit'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df16['Voice_Benefit'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Voice Benefit:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Benefit</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.bar(df16, x='Name of Day', y='Voice_Benefit')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
                

    if demo_dropdown7_value == 'TDP':
        if radio_items4_value == "B":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month,values=['Data_Price'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['Data_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Data_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Price'],
                                  textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Data_Price'],groupnorm='percent',
                                  texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                              ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)


            #chart2=px.line(df12, x='Week_Day_Count', y='Data_Price')
            ##chart2=px.scatter(df12, x='Week_Day_Count', y='Data_Price',trendline="lowess")
            #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Price'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "week":
                pv=pd.pivot_table(filtered_df_month,values=['Data_Price'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month, values=['Data_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Data_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Price'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Data_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.line(df12, x='Week_Day_Count', y='Data_Price')
                #chart2=px.scatter(df12, x='Week_Day_Count', y='Data_Price',trendline="lowess")
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Data_Price'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['Data_Price'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)   
                data = go.Scatter(x=df15['Date'], y=df15['Data_Price'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Data_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "month":
                pv = pd.pivot_table(filtered_df_month, values=['Data_Price'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Data_Price')  
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                data = go.Scatter(x=df7['Month_Name'], y=df7['Data_Price'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Data_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.line(df7, x='Month_Name', y='Data_Price')
            if radio_items3_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month, values=['Data_Price'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                #chart2=px.line(df16, x='Name of Day', y='Data_Price')
                data = go.Scatter(x=df16['Name of Day'], y=df16['Data_Price'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Data_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


        if radio_items4_value == "A":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month,values=['Data_Price'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['Data_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Data_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Price'],
                                  textposition='auto',marker=dict(color='#800080'),
                                  text=df12['Data_Price'],
                                  texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                  hoverinfo='text'
                          ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week Trend</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))
            chart2 = go.Figure(data=data, layout=layout)
            #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Price'])])
            #data = go.Data([
            #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

            #layout = go.Layout(
            #    title="Week Trend",
            #    margin=dict(l=20, r=20, t=5, b=20))

            #chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "week":
                pv = pd.pivot_table(filtered_df_month, values=['Data_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Data_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Price'],
                                      textposition='auto',marker=dict(color='#800080'),
                                      text=df12['Data_Price'],
                                      texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                      hoverinfo='text'
                              ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Trend</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>',color='black',showline=False,showgrid=False))
                chart2 = go.Figure(data=data, layout=layout)

                #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Data_Price'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)

            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['Data_Price'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)
                data = go.Bar(x=df15['Date'], y=df15['Data_Price'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df15['Data_Price'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #df7=df15.groupby('Week_Trend').agg({'Total Recharge Count':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                #print(df12)
                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                #print(df12)

                #chart2=px.bar(df15, x='Date', y='Data_Price')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "month":
                pv = pd.pivot_table(filtered_df_month, values=['Data_Price'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Data_Price') 
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                #chart2=px.bar(df7, x='Month_Name', y='Data_Price')
                data = go.Bar(x=df7['Month_Name'], y=df7['Data_Price'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df7['Data_Price'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month, values=['Data_Price'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Bar(x=df16['Name of Day'], y=df16['Data_Price'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df16['Data_Price'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Data Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Data Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.bar(df16, x='Name of Day', y='Data_Price')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
                

    if demo_dropdown7_value == 'TVP':
        if radio_items4_value == "B":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month,values=['Voice_Price'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['Voice_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Voice_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Voice_Price'],
                                  textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Voice_Price'],groupnorm='percent',
                                  texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                              ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)
            
            if radio_items3_value == "week":
                pv=pd.pivot_table(filtered_df_month,values=['Voice_Price'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Voice_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Voice_Price'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Voice_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))
                chart2 = go.Figure(data=data, layout=layout)    
    
            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Price'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)    
                data = go.Scatter(x=df15['Date'], y=df15['Voice_Price'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Voice_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
    
            if radio_items3_value == "month":
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Price'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Voice_Price')
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                #chart2=px.line(df7, x='Month_Name', y='Voice_Price')
                data = go.Scatter(x=df7['Month_Name'], y=df7['Voice_Price'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Voice_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Price'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Scatter(x=df16['Name of Day'], y=df16['Voice_Price'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Voice_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

        if radio_items4_value == "A":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month,values=['Voice_Price'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['Voice_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Voice_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            new_customdata = df12.iloc[:,4:5]
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Voice_Price'],
                                  textposition='auto',marker=dict(color='#800080'),
                                  text=df12['Voice_Price'],
                                  texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                  hoverinfo='text'
                          ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "week":
                pv=pd.pivot_table(filtered_df_month,values=['Voice_Price'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Voice_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"

                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Voice_Price'],
                                      textposition='auto',marker=dict(color='#800080'),
                                      text=df12['Voice_Price'],
                                      texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                      hoverinfo='text'
                              ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Price'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)    
                data = go.Bar(x=df15['Date'], y=df15['Voice_Price'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df15['Voice_Price'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.bar(df15, x='Date', y='Voice_Price')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "month":
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Price'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Voice_Price')
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                data = go.Bar(x=df7['Month_Name'], y=df7['Voice_Price'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df7['Voice_Price'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)



                #chart2=px.bar(df7, x='Month_Name', y='Voice_Price')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month, values=['Voice_Price'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Bar(x=df16['Name of Day'], y=df16['Voice_Price'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df16['Voice_Price'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Voice Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Voice Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)




    if demo_dropdown7_value == 'TCP':
        if radio_items4_value == "B":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month,values=['Combo_Price'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['Combo_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Combo_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
            new_customdata = df12.iloc[:,4:5]
            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Combo_Price'],
                                  textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Combo_Price'],groupnorm='percent',
                                  texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                              ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)



            if radio_items3_value == "week":
                pv=pd.pivot_table(filtered_df_month,values=['Combo_Price'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month, values=['Combo_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Combo_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
                new_customdata = df12.iloc[:,4:5]
                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                print(df12)
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Combo_Price'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Combo_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'

                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['Combo_Price'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)  
                data = go.Scatter(x=df15['Date'], y=df15['Combo_Price'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Combo_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)
                
            if radio_items3_value == "month":
                pv = pd.pivot_table(filtered_df_month, values=['Combo_Price'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Combo_Price')
                new_customdata = df7.iloc[:,0:1]
                print(df7)   
                data = go.Scatter(x=df7['Month_Name'], y=df7['Combo_Price'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Combo_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

            if radio_items3_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month, values=['Combo_Price'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)   
                data = go.Scatter(x=df16['Name of Day'], y=df16['Combo_Price'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Combo_Price'],groupnorm='percent',
                                      texttemplate= '%{text:,.2s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


        if radio_items4_value == "A":
            
            #if delta>=30:
            pv=pd.pivot_table(filtered_df_month,values=['Combo_Price'],index=['Month_Name'],aggfunc=np.sum)
            df11=pv.reset_index()
            print(df11)
            df13=df11
            pv = pd.pivot_table(filtered_df_month, values=['Combo_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            print(df14)    
            df12=df14.groupby('Week_Trend').agg({'Combo_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            print(df12)
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
            new_customdata = df12.iloc[:,4:5]
            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            print(df12)
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Combo_Price'],
                                  textposition='auto',marker=dict(color='#800080'),
                                  text=df12['Combo_Price'],
                                  texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                  hoverinfo='text'
                          ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)



            if radio_items3_value == "week":
                pv=pd.pivot_table(filtered_df_month,values=['Combo_Price'],index=['Month_Name'],aggfunc=np.sum)
                df11=pv.reset_index()
                print(df11)
                df13=df11
                pv = pd.pivot_table(filtered_df_month, values=['Combo_Price'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                print(df14)    
                df12=df14.groupby('Week_Trend').agg({'Combo_Price':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                print(df12)
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
                new_customdata = df12.iloc[:,4:5]
                print(df12)
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Combo_Price'],
                                      textposition='auto',marker=dict(color='#800080'),
                                      text=df12['Combo_Price'],
                                      texttemplate= '%{text:,.2s}',customdata=new_customdata,
                                      hoverinfo='text'
                              ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)



            if radio_items3_value == "day":
                pv = pd.pivot_table(filtered_df_month, values=['Combo_Price'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                print(df15)    
                data = go.Bar(x=df15['Date'], y=df15['Combo_Price'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df15['Combo_Price'],
                              texttemplate='%{text:,.2s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


            if radio_items3_value == "month":
                pv = pd.pivot_table(filtered_df_month, values=['Combo_Price'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Combo_Price')
                new_customdata = df7.iloc[:,0:1]
                print(df7)    
                data = go.Bar(x=df7['Month_Name'], y=df7['Combo_Price'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df7['Combo_Price'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

            if radio_items3_value == "dayname":
                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month, values=['Combo_Price'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                print(df16)    
                data = go.Bar(x=df16['Name of Day'], y=df16['Combo_Price'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df16['Combo_Price'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Combo Price:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Combo Price</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.bar(df16, x='Name of Day', y='Combo_Price')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])])
                #data = go.Data([
                #    go.Scatter(x=df12['Week_Day_Count'], y=df12['Total Recharge Count'])]

                #layout = go.Layout(
                #    title="Week Trend",
                #    margin=dict(l=20, r=20, t=5, b=20))

                #chart2 = go.Figure(data=data, layout=layout)


    if demo_dropdown7_value == 'Active':
        if radio_items4_value == "B":
            
            #if delta>=30:
            filtered_df_month=filtered_df_month.drop_duplicates(subset='CONSUMER_ID', keep="last")
            filtered_df_month['Active Customer']=1
            print(filtered_df_month)
            pv = pd.pivot_table(filtered_df_month, values=['Active Customer'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            df12=df14.groupby('Week_Trend').agg({'Active Customer':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
            new_customdata = df12.iloc[:,4:5]        
            data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Active Customer'],
                                  textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                         line=dict(color='#FFFFFF', width=2)),
                                  text=df12['Active Customer'],groupnorm='percent',
                                  texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                  hoverinfo='text'
                              ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Active Customer Count</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)

            
            #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Active Customer']),])
            #chart2=px.line(df12, x='Week_Day_Count', y='Active Customer')
            #chart2=px.scatter(df12, x='Week_Day_Count', y='Active Customer',trendline="lowess")

            if radio_items3_value == "week":
                filtered_df_month=filtered_df_month.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month['Active Customer']=1
                print(filtered_df_month)
                pv = pd.pivot_table(filtered_df_month, values=['Active Customer'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                df12=df14.groupby('Week_Trend').agg({'Active Customer':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
                new_customdata = df12.iloc[:,4:5]        
                data = go.Scatter(x=df12['Week_Day_Count'], y=df12['Active Customer'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df12['Active Customer'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Toal Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.scatter(df12, x='Week_Day_Count', y='Active Customer',trendline="lowess")    
                #chart2=px.line(df12, x='Week_Day_Count', y='Active Customer')
                #chart2=go.Figure([go.Scatter(x=df12['Week_Day_Count'], y=df12['Active Customer']),])

            if radio_items3_value == "day":
                filtered_df_month=filtered_df_month.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month['Active Customer']=1

                pv = pd.pivot_table(filtered_df_month, values=['Active Customer'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                data = go.Scatter(x=df15['Date'], y=df15['Active Customer'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df15['Active Customer'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.scatter(df15, x='Date', y='Active Customer',trendline="lowess")
                #chart2=px.line(df15, x='Date', y='Active Customer')

            if radio_items3_value == "month":
                filtered_df_month=filtered_df_month.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month['Active Customer']=1

                pv = pd.pivot_table(filtered_df_month, values=['Active Customer'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Active Customer')
                new_customdata = df7.iloc[:,0:1]
                data = go.Scatter(x=df7['Month_Name'], y=df7['Active Customer'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df7['Active Customer'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.scatter(df7, x='Month_Name', y='Active Customer',trendline="lowess")
                #chart2=px.line(df7, x='Month_Name', y='Active Customer')

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "dayname":
                filtered_df_month=filtered_df_month.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month['Active Customer']=1

                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month, values=['Active Customer'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                #chart2=px.scatter(df16, x='Name of Day', y='Active Customer',trendline="lowess")
                #chart2=px.line(df16, x='Name of Day', y='Active Customer')
                data = go.Scatter(x=df16['Name of Day'], y=df16['Active Customer'],
                                      textposition='bottom left',marker=dict(color='#800080', size=10, symbol='circle',
                                                                             line=dict(color='#FFFFFF', width=2)),
                                      text=df16['Active Customer'],groupnorm='percent',
                                      texttemplate= '%{text:,.3s}',mode='markers+lines+text',customdata=new_customdata,
                                      hoverinfo='text'
                                  ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

        if radio_items4_value == "A":
            
            #if delta>=30:
            filtered_df_month=filtered_df_month.drop_duplicates(subset='CONSUMER_ID', keep="last")
            filtered_df_month['Active Customer']=1
            print(filtered_df_month)
            pv = pd.pivot_table(filtered_df_month, values=['Active Customer'],index=['Week_Trend','Date'],aggfunc=np.sum)
            df14=pv.reset_index()
            df12=df14.groupby('Week_Trend').agg({'Active Customer':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
            #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
            df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
            df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
            new_customdata = df12.iloc[:,4:5]
            data = go.Bar(x=df12['Week_Day_Count'], y=df12['Active Customer'],
                                  textposition='auto',marker=dict(color='#800080'),
                                  text=df12['Active Customer'],
                                  texttemplate= '%{text:,.3s}',customdata=new_customdata,
                                  hoverinfo='text'
                          ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                          )

            layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                      'xanchor': 'center','yanchor': 'top'},
                               titlefont={'color': 'black','size': 15},
                               font=dict(family='sans-serif',color='black',size=12),
                               hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                               paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                               xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                               yaxis=dict(title='<b>Total Active Customer Count</b>',color='black',showline=False,showgrid=False))

            chart2 = go.Figure(data=data, layout=layout)

            #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Active Customer']),])


            if radio_items3_value == "week":
                filtered_df_month=filtered_df_month.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month['Active Customer']=1
                print(filtered_df_month)
                pv = pd.pivot_table(filtered_df_month, values=['Active Customer'],index=['Week_Trend','Date'],aggfunc=np.sum)
                df14=pv.reset_index()
                df12=df14.groupby('Week_Trend').agg({'Active Customer':sum, 'Week_Trend':'count'}).rename(columns={'Week_Trend':'count'}).reset_index()
                #df12["Week_Day_Count"] = df12["Week_Trend"].astype(str) +" "+ df12["count"].astype(str)+" "+str("Days")
                df12["Week_Day_Count"] = df12["Week_Trend"].astype(str)
                df12["Week_Day_Count1"] = df12["Week_Trend"].astype(str) +" "+"("+"contains"+ df12["count"].astype(str)+" "+str("Days")+")"
                new_customdata = df12.iloc[:,4:5]
                data = go.Bar(x=df12['Week_Day_Count'], y=df12['Active Customer'],
                                      textposition='auto',marker=dict(color='#800080'),
                                      text=df12['Active Customer'],
                                      texttemplate= '%{text:,.3s}',customdata=new_customdata,
                                      hoverinfo='text'
                              ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Week Trend','y': 0.95,'x': 0.5,
                                          'xanchor': 'center','yanchor': 'top'},
                                   titlefont={'color': 'black','size': 15},
                                   font=dict(family='sans-serif',color='black',size=12),
                                   hovermode='closest',margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF',plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week</b>',color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>',color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                    #chart2=go.Figure([go.Bar(x=df12['Week_Day_Count'], y=df12['Active Customer']),])

            if radio_items3_value == "day":
                filtered_df_month=filtered_df_month.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month['Active Customer']=1

                pv = pd.pivot_table(filtered_df_month, values=['Active Customer'], index=['Date'],aggfunc=np.sum)
                df15=pv.reset_index()
                new_customdata = df15.iloc[:,0:1]
                data = go.Bar(x=df15['Date'], y=df15['Active Customer'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df15['Active Customer'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Daily Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Daily</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)



                #chart2=px.bar(df15, x='Date', y='Active Customer')

            if radio_items3_value == "month":
                filtered_df_month=filtered_df_month.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month['Active Customer']=1

                pv = pd.pivot_table(filtered_df_month, values=['Active Customer'],index=['Month_Name'],aggfunc=np.sum)
                df=pv.reset_index()
                df7=Sort_Dataframeby_MonthandNumeric_cols(df = df, monthcolumn='Month_Name',numericcolumn='Active Customer')
                new_customdata = df7.iloc[:,0:1]

                data = go.Bar(x=df7['Month_Name'], y=df7['Active Customer'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df7['Active Customer'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'Monthly Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Month</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)


                #chart2=px.bar(df7, x='Month_Name', y='Active Customer')

                #chart2 = go.Figure(data=data, layout=layout)
            if radio_items3_value == "dayname":
                filtered_df_month=filtered_df_month.drop_duplicates(subset='CONSUMER_ID', keep="last")
                filtered_df_month['Active Customer']=1

                cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                pv = pd.pivot_table(filtered_df_month, values=['Active Customer'],index=['Name of Day'],aggfunc=np.sum).reindex(cats)
                df16=pv.reset_index()
                new_customdata = df16.iloc[:,0:1]
                data = go.Bar(x=df16['Name of Day'], y=df16['Active Customer'],
                              textposition='auto', marker=dict(color='#800080'),
                              text=df16['Active Customer'],
                              texttemplate='%{text:,.3s}',customdata=new_customdata,
                              hoverinfo='text'
                              ,hovertemplate='Total Active Count:%{text}<br>Description:%{customdata[0]}<extra></extra>'
                              )

                layout = go.Layout(title={'text': 'WeekDay Trend', 'y': 0.95, 'x': 0.5,
                                          'xanchor': 'center', 'yanchor': 'top'},
                                   titlefont={'color': 'black', 'size': 15},
                                   font=dict(family='sans-serif', color='black', size=12),
                                   hovermode='closest', margin=dict(t=30, b=100, l=70, r=10),
                                   paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
                                   xaxis=dict(title='<b>Week Day</b>', color='black',showline=False,showgrid=False),
                                   yaxis=dict(title='<b>Total Active Customer Count</b>', color='black',showline=False,showgrid=False))

                chart2 = go.Figure(data=data, layout=layout)

                #chart2=px.bar(df16, x='Name of Day', y='Active Customer')
    
    df1 = filtered_df_month
    #df1=df1.drop(df1[['Date','Month','Day','WeekNum','Name of Day','Month_Name','Week','Week_Trend','Day_Trend']],axis=1)
    # tooltip_data= [{i: {'value': i,'use_with': 'both'} for i in df.columns}]
    col = [{"name": i, "id": i, "hideable": "last"} for i in df.columns]
    df1 = df1.to_dict('records')
            
    return chart2,df1, col                             
@app.callback(Output("output-8", "children"),
              [Input("save-button1", "n_clicks"),
               ],
              [State("table2", "data")],)

def selected_data_to_csv1(nclicks, table2):
    if nclicks == 0:
        raise PreventUpdate
    else:
        # df=pd.DataFrame(table1)
        # pd.DataFrame(table1).to_csv('C://Users//ch-e05138//Desktop//New folder//gaurav.csv',index=False)
        save_path = 'C:/Users/ch-e05138/Desktop/New folder/'
        file_name =  "Compare_Trend.csv"
        print(file_name)
        completeName = os.path.join(save_path, file_name)
        print(completeName)
        pd.DataFrame(table2).to_csv(completeName, index=False)

        # df.to_csv(completeName,index=False)
        # print(completeName)
        # file1 = open(completeName, "w")
        # file1.write("file")
        # file1.close()
        # send_data_frame(df.to_csv, value+".csv", index=False)
        # return completeName
        # return send_data_frame(df.to_csv, value+".csv", index=False)

        return "Data Saved"

@app.callback([Output('bar-chart6', 'figure')],
              [Output('bar-chart7', 'figure')],
               [Input('demo_dropdown','value'),
               Input("date_picker_sales2","start_date"),
               Input("date_picker_sales2","end_date"),
               Input('demo_dropdown10','value'),
               Input('demo_dropdown11','value')],
              )


def display_graphs1(demo_dropdown_value,date_picker_sales2_start_date, date_picker_sales2_end_date,demo_dropdown10_value, demo_dropdown11_value):
    df =load_data()
    #print(df)
    global chart1,chart2,data
    if demo_dropdown_value == []:
        #print(demo_dropdown2_value)
        
        filtered_df_month1 = df
        start=filtered_df_month1['TRX_DATE'].min()
        #df11=pd.pivot_table(data=filtered_df_month1, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        #print(filtered_df_month1)
        chart1 = {'data': []}
        chart2 = {'data': []}

    elif demo_dropdown_value == ['Full Base']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        #print(filtered_df_month1)
        #filtered_df_month1 = filtered_df_month1[filtered_df_month1['Full_Base'] == ]
        #filtered_df_month1 = df[(df['CG/TG'].isin(a))]    
        #df13=pd.pivot_table(data=filtered_df_month1, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()

    elif demo_dropdown_value == ['Full Base','CG']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))] 
        #start=filtered_df_month1['TRX_DATE'].min()
        #print(filtered_df_month1)

    elif demo_dropdown_value == ['CG','Full Base']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))] 
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown_value == ['Full Base','TG']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        #filtered_df_month1 = filtered_df_month1[filtered_df_month1['Full_Base'] == ]
        #filtered_df_month1 = df[(df['CG/TG'].isin(a))]    

    elif demo_dropdown_value == ['TG','Full Base']:
        print(demo_dropdown_value)
        b=[]
        for i in demo_dropdown_value:
            b.append(i)
        print(b)
        filtered_df_month1 = df[(df['Full_Base'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown_value == ['CG','TG']:
        a=[]
        for i in demo_dropdown_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month1 = df[(df['CG/TG'].isin(a))]  
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1 )
        #filtered_df_month1 = df[df['CG/TG'] == demo_dropdown2_value]
            #print(filtered_df_month1)
            #df1 = df.groupby('CG/TG', as_index=False)['Voice_Benefit'].agg({'Sum_value': 'sum'})

    elif demo_dropdown_value == ['TG','CG']:
        a=[]
        for i in demo_dropdown_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month1 = df[(df['CG/TG'].isin(a))]  
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1 )

    elif demo_dropdown_value == ['CG']:
        a=[]
        for i in demo_dropdown_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month1 = df[(df['CG/TG'].isin(a))]  
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        print(start)
    elif demo_dropdown_value == ['TG']:
        a=[]
        for i in demo_dropdown_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month1 = df[(df['CG/TG'].isin(a))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)    

    elif demo_dropdown_value == ['TG','CG','Full Base']:
        a=[]
        for i in demo_dropdown_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month1 = df[(df['CG/TG'].isin(a))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)    

    elif demo_dropdown_value == ['Full Base','CG','TG']:
        a=[]
        for i in demo_dropdown_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month1 = df[(df['CG/TG'].isin(a))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)    

    elif demo_dropdown_value == ['CG','Full Base','TG']:
        a=[]
        for i in demo_dropdown_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month1 = df[(df['CG/TG'].isin(a))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)    

    elif demo_dropdown_value == ['TG','Full Base','CG']:
        a=[]
        for i in demo_dropdown_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month1 = df[(df['CG/TG'].isin(a))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)    
        
    elif demo_dropdown_value == ['CG','TG','Full Base']:
        a=[]
        for i in demo_dropdown_value:
            a.append(i)
        #a=a.remove("Full Base")    
        filtered_df_month1 = df[(df['CG/TG'].isin(a))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)    

###################################################        
    if demo_dropdown10_value == []:
        #print(demo_dropdown2_value)
        filtered_df_month1 = filtered_df_month1
        #df11=pd.pivot_table(data=filtered_df_month1, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        print(filtered_df_month1)
        chart1 = {'data': []}
        chart1 = {'data': []}
    elif demo_dropdown10_value == ['All']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
#        print(b)
#        b[0]="Full Base"
#        print(b)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type_ALL'].isin(b))]    
        print(filtered_df_month1)
    
    elif demo_dropdown10_value == ['Data']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        print(start)
        
    elif demo_dropdown10_value == ['Voice']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown10_value == ['Combo']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown10_value == ['Voice','Combo']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown10_value == ['Voice','Data']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        
    elif demo_dropdown10_value == ['Data','Voice']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown10_value == ['Combo','Voice']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown10_value == ['Combo','Data']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown10_value == ['Data','Combo']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown10_value == ['Data','Voice','Combo']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)
        
    elif demo_dropdown10_value == ['Data','Voice','Combo']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown10_value == ['Voice','Data','Combo']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown10_value == ['Voice','Combo','Data']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown10_value == ['Combo','Voice','Data']:
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))] 
        start=filtered_df_month1['TRX_DATE'].min()
        print(filtered_df_month1)

    elif demo_dropdown10_value == ['Combo','Data','Voice']:
        print(demo_dropdown10_value)
        b=[]
        for i in demo_dropdown10_value:
            b.append(i)
        filtered_df_month1 = filtered_df_month1[(filtered_df_month1['Type'].isin(b))]
        print(filtered_df_month1)
    
    if date_picker_sales2_start_date == None and date_picker_sales2_end_date == None:
        #print(demo_dropdown2_value)
        filtered_df_month1 = filtered_df_month1
        #df11=pd.pivot_table(data=filtered_df_month1, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        #print(filtered_df_month1)
        chart1 = {'data': []}
        chart2 = {'data': []}
    elif date_picker_sales2_start_date != None and date_picker_sales2_end_date != None:
        
        print(date_picker_sales2_start_date)
        print(date_picker_sales2_end_date)
        global pv,chart,df13
        #filtered_df_month1=filtered_df_month1[(filtered_df_month1['Date']>date_picker_sales1_start_date)&(filtered_df_month1['Date']<date_picker_sales1_end_date)]
        print(filtered_df_month1)
        filtered_df_month1['Date']=pd.to_datetime(filtered_df_month1['TRX_DATE'],errors = 'coerce')
#         filtered_df_month1['Month']=filtered_df_month1['Date'].dt.month
#         filtered_df_month1['Day']=filtered_df_month1['Date'].dt.day
#         #filtered_df_month1['WeekNum'] = filtered_df_month1['Date'].dt.week
#         filtered_df_month1['WeekNum'] = filtered_df_month1['Date'].dt.strftime('%W')
#         filtered_df_month1['Name of Day']=filtered_df_month1['Date'].dt.day_name()
#         #filtered_df_month1['WeekNum'] = filtered_df_month1['WeekNum'].replace([53], 1)
#         filtered_df_month1['Month_Name']=filtered_df_month1['Month'].apply(lambda x:calendar.month_abbr[x])
#         filtered_df_month1["Week"]=str('_Week')
#         filtered_df_month1["Week_Trend"] = filtered_df_month1["WeekNum"].astype(str) + filtered_df_month1["Week"]
#         filtered_df_month1["Day_Trend"] = filtered_df_month1["Day"].astype(str) + filtered_df_month1["Month_Name"]
        
        date_entry=date_picker_sales2_start_date
        year,month,day=map(int,date_entry.split('-'))
        start_date=datetime(year,month,day)

        date_entry1=date_picker_sales2_end_date
        year,month,day=map(int,date_entry1.split('-'))
        end_date=datetime(year,month,day)

        date33=end_date
        date11=start_date

        print(date11)
        print(date33)
        mdate1=date11
        rdate1=date33
        delta=(rdate1-mdate1).days
        print(delta)
        filtered_df_month1=filtered_df_month1[(filtered_df_month1['Date']>=date11)&(filtered_df_month1['Date']<=date33)]
        print(filtered_df_month1)
    if demo_dropdown10_value =="":
        chart1 = {'data': []}
        chart2 = {'data': []}
    if demo_dropdown11_value == 'T10R':
        import numpy as np
        pv = pd.pivot_table(filtered_df_month1, values=['PRICE','Count Cust'],index=['PRODUCT_ID','Type'],aggfunc=np.sum)
        df22=pv.reset_index()
        df22=df22.sort_values(['PRICE','Count Cust'], ascending=False)
        #df23=df22.sort_values('Active Customer', ascending=False)
        data=df22.head(10)
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='PRICE', orientation='v', color='Type',text='PRICE',labels={
            "Type": "Product Type"},width=560,height=400)
        fig.update_traces(texttemplate='%{text:.3s}', textposition='outside',)
        fig.update_layout(yaxis={"title":'<b>Price</b>'},
                          xaxis={'categoryorder': 'total descending',"title":'<b>Product ID</b>'},plot_bgcolor='#FFFFFF',
                        legend=dict(yanchor="bottom",orientation='h',y=-0.25,xanchor="center",x=0.50),
                        margin=dict(l=0, r=0, t=30, b=0)),
         
        chart1=fig
        #df33=filtered_df_month1.groupby(['PRODUCT_ID','Type'])['PRICE'].count().nlargest(10).reset_index()
        data=df22.head(10)
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='PRICE', orientation='v', color='Type',text='Count Cust',custom_data=['Type'],
                     labels={"Type": "Product Type"},width=560,height=400)
        
        fig.update_traces(textposition='outside',texttemplate='%{text:.3s}',
                        hovertemplate = 'Count Cust %{text}<br>PRODUCT_ID %{x}<br>Product Type %{customdata[0]}<extra></extra>'),
        fig.update_layout(yaxis={"title":'<b>Price</b>'}
                          ,xaxis={'categoryorder': 'total descending',"title":'<b>Product ID</b>','visible': True, 'showticklabels': True} ,plot_bgcolor='#FFFFFF',
                         legend=dict(yanchor="bottom",orientation='h',y=-0.25,xanchor="center",x=0.50),
                         margin=dict(l=0, r=0, t=30, b=0))
        chart2=fig
        
    if demo_dropdown11_value == 'T10C':
        import numpy as np
        pv = pd.pivot_table(filtered_df_month1, values=['PRICE','Count Cust'],index=['PRODUCT_ID','Type'],aggfunc=np.sum)
        df22=pv.reset_index()
        #df22=df22.sort_values('PRICE', ascending=False)
        df22=df22.sort_values(['Count Cust','PRICE'], ascending=False)
        data=df22.head(10)
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='Count Cust', orientation='v', color='Type',text='PRICE',labels={
            "Type": "Product Type"},width=560,height=400)
        fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
        fig.update_layout(yaxis={"title":'<b>Count</b>'},
                          xaxis={'categoryorder': 'total descending',"title":'<b>Product ID</b>'},plot_bgcolor='#FFFFFF',
                        legend=dict(yanchor="bottom",orientation='h',y=-0.25,xanchor="center",x=0.50),
                        margin=dict(l=0, r=0, t=30, b=0)),
        chart1=fig
        #df33=filtered_df_month1.groupby(['PRODUCT_ID','Type'])['PRICE'].count().nlargest(10).reset_index()
        data=df22.head(10)
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='Count Cust', orientation='v', color='Type',text='Count Cust',
                     custom_data=['Type'],labels={"Type": "Product Type"},width=560,height=400)
        fig.update_traces(textposition='outside',texttemplate='%{text:.3s}',
                        hovertemplate = 'Count Cust %{text}<br>PRODUCT_ID %{x}<br>Product Type %{customdata[0]}<extra></extra>'),
        fig.update_layout(yaxis={"title":'<b>Count</b>'}
                          ,xaxis={'categoryorder': 'total descending',"title":'<b>Product ID</b>','visible': True, 'showticklabels': True} ,plot_bgcolor='#FFFFFF',
                         legend=dict(yanchor="bottom",orientation='h',y=-0.25,xanchor="center",x=0.50),
                         margin=dict(l=0, r=0, t=30, b=0))
        chart2=fig
        
    if demo_dropdown11_value == 'B10R':
        import numpy as np
        pv = pd.pivot_table(filtered_df_month1, values=['PRICE','Count Cust'],index=['PRODUCT_ID','Type'],aggfunc=np.sum)
        df22=pv.reset_index()
        df22=df22.sort_values(['PRICE','Count Cust'], ascending=False)
        #df23=df22.sort_values('Active Customer', ascending=False)
        data=df22.tail(10)
        data=data.sort_values(['PRICE','Count Cust'], ascending=True)
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='PRICE', orientation='v', color='Type',text='PRICE',labels={
            "Type": "Product Type"},width=560,height=400)
        fig.update_traces(texttemplate='%{text:.3s}', textposition='outside',)
        fig.update_layout(yaxis={"title":'<b>Price</b>'},
                          xaxis={'categoryorder': 'total ascending',"title":'<b>Product ID</b>'},plot_bgcolor='#FFFFFF',
                        legend=dict(yanchor="bottom",orientation='h',y=-0.25,xanchor="center",x=0.50),
                        margin=dict(l=0, r=0, t=40, b=0)),
         
        chart1=fig
        #df33=filtered_df_month1.groupby(['PRODUCT_ID','Type'])['PRICE'].count().nlargest(10).reset_index()
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='PRICE', orientation='v', color='Type',text='Count Cust',custom_data=['Type'],
                     labels={"Type": "Product Type"},width=560,height=400)
        fig.update_traces(textposition='outside',texttemplate='%{text:.3s}',
                        hovertemplate = 'Count Cust %{text}<br>PRODUCT_ID %{x}<br>Product Type %{customdata[0]}<extra></extra>'),
        fig.update_layout(yaxis={"title":'<b>Price</b>'}
                          ,xaxis={'categoryorder': 'total ascending',"title":'<b>Product ID</b>','visible': True, 'showticklabels': True} ,plot_bgcolor='#FFFFFF',
                         legend=dict(yanchor="bottom",orientation='h',y=-0.25,xanchor="center",x=0.50),
                         margin=dict(l=0, r=0, t=40, b=0),hoverlabel=dict(namelength=0))
        chart2=fig
        
    if demo_dropdown11_value == 'B10C':
        import numpy as np
        pv = pd.pivot_table(filtered_df_month1, values=['PRICE','Count Cust'],index=['PRODUCT_ID','Type'],aggfunc=np.sum)
        df22=pv.reset_index()
        #df22=df22.sort_values('PRICE', ascending=False)
        df22=df22.sort_values(['Count Cust','PRICE'], ascending=False)
        
        data=df22.tail(10)
        data=data.sort_values(['Count Cust','PRICE'], ascending=True)
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='Count Cust', orientation='v', color='Type',text='PRICE',labels={
            "Type": "Product Type"},width=560,height=400)
        fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
        fig.update_layout(yaxis={"title":'<b>Count</b>'},
                          xaxis={'categoryorder': 'total ascending',"title":'<b>Product ID</b>'},plot_bgcolor='#FFFFFF',
                        legend=dict(yanchor="bottom",orientation='h',y=-0.25,xanchor="center",x=0.50),
                        margin=dict(l=0, r=0, t=40, b=0)),
        chart1=fig
        #df33=filtered_df_month1.groupby(['PRODUCT_ID','Type'])['PRICE'].count().nlargest(10).reset_index()
        data=df22.tail(10)
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='Count Cust', orientation='v', color='Type',text='Count Cust',
                     custom_data=['Type'],labels={"Type": "Product Type"},width=560,height=400)
        fig.update_traces(textposition='outside',texttemplate='%{text:.3s}',
                        hovertemplate = 'Count Cust %{text}<br>PRODUCT_ID %{x}<br>Product Type %{customdata[0]}<extra></extra>'),
        fig.update_layout(yaxis={"title":'<b>Count</b>'}
                          ,xaxis={'categoryorder': 'total ascending',"title":'<b>Product ID</b>','visible': True, 'showticklabels': True} ,plot_bgcolor='#FFFFFF',
                         legend=dict(yanchor="bottom",orientation='h',y=-0.25,xanchor="center",x=0.50),
                         margin=dict(l=0, r=0, t=40, b=0))
        chart2=fig

    if demo_dropdown11_value == '80TR':
        import numpy as np
        pv = pd.pivot_table(filtered_df_month1, values=['PRICE','Count Cust'],index=['PRODUCT_ID','Type'],aggfunc=np.sum)
        df22=pv.reset_index()
        df22=df22.sort_values(['PRICE','Count Cust'], ascending=False)
        #df23=df22.sort_values('Active Customer', ascending=False)
        # pv1 = pd.pivot_table(df, values=['Active Customer'],index=['PRODUCT_ID','Type'],aggfunc=np.sum)
        # df23=pv1.reset_index()

        df22['Cum_Sum']=df22.PRICE.cumsum()
        # #filtered_df_month1.to_csv("Cum_Sum.csv")
        cummthreshold=df22['PRICE'].sum()*80/100
        print(cummthreshold)

        df22=df22[(df22['Cum_Sum']<=cummthreshold)]
        data=df22
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='PRICE', orientation='v', color='Type',text='PRICE',labels={
            "Type": "Product Type"},width=3650,height=400)
        fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
        fig.update_layout(yaxis={"title":'<b>Price</b>'},
                          xaxis={'categoryorder': 'total descending',"title":'<b>Product ID</b>'},plot_bgcolor='#FFFFFF',
                        legend=dict(yanchor="bottom",orientation='h',y=-0.20,xanchor="left",x=0.02),
                        margin=dict(l=0, r=0, t=30, b=0)),
         
        chart1=fig
        #df33=filtered_df_month1.groupby(['PRODUCT_ID','Type'])['PRICE'].count().nlargest(10).reset_index()
        data=df22
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='PRICE', orientation='v', color='Type',text='Count Cust',custom_data=['Type'],
                     labels={"Type": "Product Type"},width=3650,height=400)
        fig.update_traces(textposition='outside',texttemplate='%{text:.3s}',
                        hovertemplate = 'Count Cust %{text}<br>PRODUCT_ID %{x}<br>Product Type %{customdata[0]}<extra></extra>'),
        fig.update_layout(yaxis={"title":'<b>Price</b>'}
                          ,xaxis={'categoryorder': 'total descending','visible': True, 'showticklabels': True} ,plot_bgcolor='#FFFFFF',
                         legend=dict(yanchor="bottom",orientation='h',y=-0.20,xanchor="left",x=0.02),
                         margin=dict(l=0, r=0, t=30, b=0))
        
        chart2=fig
    if demo_dropdown11_value == '80TC':
        import numpy as np
        pv = pd.pivot_table(filtered_df_month1, values=['PRICE','Count Cust'],index=['PRODUCT_ID','Type'],aggfunc=np.sum)
        df22=pv.reset_index()
        #df22=df22.sort_values('PRICE', ascending=False)
        df22=df22.sort_values(['Count Cust','PRICE'], ascending=False)
        
        df22['Cum_Sum']=df22.PRICE.cumsum()
        # #filtered_df_month1.to_csv("Cum_Sum.csv")
        cummthreshold=df22['PRICE'].sum()*80/100
        print(cummthreshold)

        df22=df22[(df22['Cum_Sum']<=cummthreshold)]
        data=df22
        print(data)

        fig = px.bar(data, x='PRODUCT_ID', y='Count Cust', orientation='v', color='Type',text='PRICE',labels={
            "Type": "Product Type"},width=3650,height=400)
        fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
        fig.update_layout(yaxis={"title":'<b>Count</b>'},
                          xaxis={'categoryorder': 'total descending',"title":'<b>Product ID</b>'},plot_bgcolor='#FFFFFF',
                        legend=dict(yanchor="bottom",orientation='h',y=-0.20,xanchor="left",x=0.02),
                        margin=dict(l=0, r=0, t=30, b=0)),
        chart1=fig
        #df33=filtered_df_month1.groupby(['PRODUCT_ID','Type'])['PRICE'].count().nlargest(10).reset_index()
        data=df22
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='Count Cust', orientation='v', color='Type',text='Count Cust',
                     custom_data=['Type'],labels={"Type": "Product Type"},width=3650,height=400)
        fig.update_traces(textposition='outside',texttemplate='%{text:.3s}',
                        hovertemplate = 'Count Cust %{text}<br>PRODUCT_ID %{x}<br>Product Type %{customdata[0]}<extra></extra>'),
        fig.update_layout(yaxis={"title":'<b>Count</b>'}
                          ,xaxis={'categoryorder': 'total descending','visible': True, 'showticklabels': True} ,plot_bgcolor='#FFFFFF',
                         legend=dict(yanchor="bottom",orientation='h',y=-0.20,xanchor="left",x=0.02),
                         margin=dict(l=0, r=0, t=30, b=0))
        chart2=fig

    if demo_dropdown11_value == '20TR':
        import numpy as np
        import numpy as np
        pv = pd.pivot_table(filtered_df_month1, values=['PRICE','Count Cust'],index=['PRODUCT_ID','Type'],aggfunc=np.sum)
        df22=pv.reset_index()
        df22=df22.sort_values(['PRICE','Count Cust'], ascending=False)
        #df23=df22.sort_values('Active Customer', ascending=False)
        # pv1 = pd.pivot_table(df, values=['Active Customer'],index=['PRODUCT_ID','Type'],aggfunc=np.sum)
        # df23=pv1.reset_index()

        df22['Cum_Sum']=df22.PRICE.cumsum()
        # #filtered_df_month1.to_csv("Cum_Sum.csv")
        cummthreshold=df22['PRICE'].sum()*80/100
        print(cummthreshold)

        df22=df22[(df22['Cum_Sum']>=cummthreshold)]
        data=df22
        data=data.sort_values(['PRICE','Count Cust'], ascending=True)
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='PRICE', orientation='v', color='Type',text='PRICE',labels={
            "Type": "Product Type"},width=1700,height=400)
        fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
        fig.update_layout(yaxis={"title":'<b>Price</b>'},
                          xaxis={'categoryorder': 'total ascending',"title":'<b>Product ID</b>'},plot_bgcolor='#FFFFFF',
                        legend=dict(yanchor="bottom",orientation='h',y=-0.20,xanchor="left",x=0.05),
                        margin=dict(l=0, r=0, t=30, b=0)),
         
        chart1=fig
        #df33=filtered_df_month1.groupby(['PRODUCT_ID','Type'])['PRICE'].count().nlargest(10).reset_index()
        data=df22
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='PRICE', orientation='v', color='Type',text='Count Cust',custom_data=['Type'],
                     labels={"Type": "Product Type"},width=1700,height=400)
        fig.update_traces(textposition='outside',texttemplate='%{text:.3s}',
                        hovertemplate = 'Count Cust %{text}<br>PRODUCT_ID %{x}<br>Product Type %{customdata[0]}<extra></extra>'),
        fig.update_layout(yaxis={"title":'<b>Price</b>'}
                          ,xaxis={'categoryorder': 'total ascending','visible': True, 'showticklabels': True} ,plot_bgcolor='#FFFFFF',
                         legend=dict(yanchor="bottom",orientation='h',y=-0.20,xanchor="left",x=0.05),
                         margin=dict(l=0, r=0, t=30, b=0))
        
        chart2=fig
    

    if demo_dropdown11_value == '20TC':
        import numpy as np        
        pv = pd.pivot_table(filtered_df_month1, values=['PRICE','Count Cust'],index=['PRODUCT_ID','Type'],aggfunc=np.sum)
        df22=pv.reset_index()
        #df22=df22.sort_values('PRICE', ascending=False)
        df22=df22.sort_values(['Count Cust','PRICE'], ascending=False)
        
        df22['Cum_Sum']=df22.PRICE.cumsum()
        # #filtered_df_month1.to_csv("Cum_Sum.csv")
        cummthreshold=df22['PRICE'].sum()*80/100
        print(cummthreshold)

        df22=df22[(df22['Cum_Sum']>=cummthreshold)]
        data=df22
        print(data)

        fig = px.bar(data, x='PRODUCT_ID', y='Count Cust', orientation='v', color='Type',text='PRICE',labels={
            "Type": "Product Type"},width=1700,height=400)
        fig.update_traces(texttemplate='%{text:.3s}', textposition='outside')
        fig.update_layout(yaxis={"title":'<b>Count</b>'},
                          xaxis={'categoryorder': 'total ascending',"title":'<b>Product ID</b>'},plot_bgcolor='#FFFFFF',
                        legend=dict(yanchor="bottom",orientation='h',y=-0.20,xanchor="left",x=0.05),
                        margin=dict(l=0, r=0, t=30, b=0)),
        chart1=fig
        #df33=filtered_df_month1.groupby(['PRODUCT_ID','Type'])['PRICE'].count().nlargest(10).reset_index()
        data=df22
        print(data)
        fig = px.bar(data, x='PRODUCT_ID', y='Count Cust', orientation='v', color='Type',text='Count Cust',
                     custom_data=['Type'],labels={"Type": "Product Type"},width=1700,height=400)
        fig.update_traces(textposition='outside',texttemplate='%{text:.3s}',
                        hovertemplate = 'Count Cust %{text}<br>PRODUCT_ID %{x}<br>Product Type %{customdata[0]}<extra></extra>'),
        fig.update_layout(yaxis={"title":'<b>Count</b>'}
                          ,xaxis={'categoryorder': 'total ascending','visible': True, 'showticklabels': True} ,plot_bgcolor='#FFFFFF',
                         legend=dict(yanchor="bottom",orientation='h',y=-0.20,xanchor="left",x=0.05),
                         margin=dict(l=0, r=0, t=30, b=0))
        chart2=fig
    
    
    return [chart1,chart2]

@app.callback(Output('demo_dropdown17', 'options'),
              Output('table2', 'data'),
              Output('table2', 'columns'),
               [Input('demo_dropdown15','value'),
               Input('demo_dropdown16','value')],
              )


def display_graphs3(demo_dropdown15_value,demo_dropdown16_value):
    df =load_data()
    #print(df)
    global chart3,chart4,filtered_df_month2,a,b
    if demo_dropdown15_value == []:
        print(demo_dropdown15_value)
        filtered_df_month2 = df
        #df11=pd.pivot_table(data=filtered_df_month2, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        #print(filtered_df_month2)
        chart3 = {'data': []}
        chart4 = {'data': []}
    elif demo_dropdown15_value == ['All']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
#        print(b)
#        b[0]="Full Base"
#        print(b)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type_ALL'].isin(b))]    
        #print(filtered_df_month2)
    
    elif demo_dropdown15_value == ['Data']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)
        #print(start)
        
    elif demo_dropdown15_value == ['Voice']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        #print(filtered_df_month2)

    elif demo_dropdown15_value == ['Combo']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        #start=filtered_df_month2['TRX_DATE'].min()
        #print(filtered_df_month2)

    elif demo_dropdown15_value == ['Voice','Combo']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        #start=filtered_df_month2['TRX_DATE'].min()
        #print(filtered_df_month2)

    elif demo_dropdown15_value == ['Voice','Data']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        #start=filtered_df_month2['TRX_DATE'].min()
        #print(filtered_df_month2)
        
    elif demo_dropdown15_value == ['Data','Voice']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        #start=filtered_df_month2['TRX_DATE'].min()
        #print(filtered_df_month2)

    elif demo_dropdown15_value == ['Combo','Voice']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        #start=filtered_df_month2['TRX_DATE'].min()
        #print(filtered_df_month2)

    elif demo_dropdown15_value == ['Combo','Data']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        #start=filtered_df_month2['TRX_DATE'].min()
        #print(filtered_df_month2)

    elif demo_dropdown15_value == ['Data','Combo']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        #start=filtered_df_month2['TRX_DATE'].min()
        #print(filtered_df_month2)

    elif demo_dropdown15_value == ['Data','Voice','Combo']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        #start=filtered_df_month2['TRX_DATE'].min()
        #print(filtered_df_month2)
        
    elif demo_dropdown15_value == ['Data','Voice','Combo']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        #start=filtered_df_month2['TRX_DATE'].min()
        #print(filtered_df_month2)

    elif demo_dropdown15_value == ['Voice','Data','Combo']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        #start=filtered_df_month2['TRX_DATE'].min()
        #print(filtered_df_month2)

    elif demo_dropdown15_value == ['Voice','Combo','Data']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        #start=filtered_df_month2['TRX_DATE'].min()
        #print(filtered_df_month2)

    elif demo_dropdown15_value == ['Combo','Voice','Data']:
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))] 
        #start=filtered_df_month2['TRX_DATE'].min()
        #print(filtered_df_month2)

    elif demo_dropdown15_value == ['Combo','Data','Voice']:
        print(demo_dropdown15_value)
        b=[]
        for i in demo_dropdown15_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Type'].isin(b))]
        #print(filtered_df_month2)

    if demo_dropdown16_value == []:
        #print(demo_dropdown2_value)
        filtered_df_month2 = filtered_df_month2
        #df11=pd.pivot_table(data=filtered_df_month2, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        #print(filtered_df_month2)
        chart3 = {'data': []}
        chart4 = {'data': []}

    elif demo_dropdown16_value == ['All']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
#        print(b)
#        b[0]="Full Base"
#        print(b)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity_ALL'].isin(b))]    
        print(filtered_df_month2)
    
    elif demo_dropdown16_value == ['Daily']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)
        print(start)
        
    elif demo_dropdown16_value == ['Weekly']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)

    elif demo_dropdown16_value == ['Monthly']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)

    elif demo_dropdown16_value == ['Daily','Weekly']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)

    elif demo_dropdown16_value == ['Daily','Monthly']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)
        
    elif demo_dropdown16_value == ['Weekly','Daily']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)

    elif demo_dropdown16_value == ['Weekly','Monthly']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)

    elif demo_dropdown16_value == ['Monthly','Daily']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)

    elif demo_dropdown16_value == ['Monthly','Weekly']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)

    elif demo_dropdown16_value == ['Daily','Weekly','Monthly']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)
        
    elif demo_dropdown16_value == ['Daily','Monthly','Weekly']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)

    elif demo_dropdown16_value == ['Weekly','Daily','Monthly']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)

    elif demo_dropdown16_value == ['Weekly','Monthly','Daily']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)

    elif demo_dropdown16_value == ['Monthly','Weekly','Daily']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))] 
        start=filtered_df_month2['TRX_DATE'].min()
        print(filtered_df_month2)

    elif demo_dropdown16_value == ['Monthly','Daily','Weekly']:
        print(demo_dropdown16_value)
        b=[]
        for i in demo_dropdown16_value:
            b.append(i)
        filtered_df_month2 = filtered_df_month2[(filtered_df_month2['Validity'].isin(b))]
        start=filtered_df_month2['TRX_DATE'].min()

        print(filtered_df_month2)
    df1 = filtered_df_month2
    col = [{"name": i, "id": i, "hideable": "last"} for i in df1.columns]
    df1 = df1.to_dict('records')

    return [{'label': i, 'value': i} for i in filtered_df_month2['PRODUCT_ID'].unique()],df1,col





############################################################
@app.callback([Output('bar-chart8', 'figure')],
              [Output('bar-chart9', 'figure')],
               [
               Input('demo_dropdown17','value'),
               Input('radio_items8','value'),
               Input('radio_items9','value'),
               Input('table2', 'data')
               ],
              )


def display_graphs2(demo_dropdown17_value,radio_items8_value,radio_items9_value,table2):
    df =pd.DataFrame(table2)
    #print(df)
    global chart3,chart4,filtered_df_month2,a,b
    if demo_dropdown17_value == []:
        print(demo_dropdown17_value)
        df=df
        #df11=pd.pivot_table(data=filtered_df_month2, index=['CG/TG'], values=['Voice_Benefit', 'Data_Benefit','Voice_Price','Data_Price','Combo_Price'], aggfunc='sum').reset_index()
        #print(filtered_df_month2)
        chart3 = {'data': []}
        chart4 = {'data': []}
    elif len(demo_dropdown17_value) != "":
        print(demo_dropdown17_value)
        #print(filtered_df_month2)

        if radio_items8_value=="A":
            df5=df[(df['PRODUCT_ID'].isin(demo_dropdown17_value))]
            df5['Date']=pd.to_datetime(df5['TRX_DATE'],errors = 'coerce')
            df5 =df5.sort_values("Date").reset_index(drop=True)
            df5['WeekNum'] = df5['Date'].dt.strftime('%W')
            df5["Week"]=str(' Week')
            df5["Week_Trend"] = df5["WeekNum"].astype(str)+ df5["Week"]
            df5["Week_Trend1"] = "(Product_ID-"+df5['PRODUCT_ID']+" "+"Type-"+df5['Type']+","+"Validity-"+df5['Validity']+")"
            
            #print(df5)
            tab = pd.crosstab([df5['Week_Trend']],df5['Week_Trend1'],df5.PRICE,aggfunc="sum",margins=True).reset_index()
            #print(tab)
            tab=tab.drop(['All'], axis = 1)
            tab=tab.drop(tab.tail(1).index) 
            #print(tab)
            #cols=[]
            #tab.iloc[:,3:]
            df2 = tab.melt('Week_Trend', var_name='cols',  value_name='vals')
            fig=px.line(df2, x='Week_Trend' , y='vals' , color='cols',labels={"cols": " "},text='cols')

            fig.update_traces(mode="markers+lines",
                              hovertemplate = 'Week: %{x}<br>Description: %{text}<br>Revenue: %{y}<extra></extra>')
            fig.update_layout(yaxis={'categoryorder': 'total ascending',"title":'<b>Product Revenue</b>'},
                              xaxis={"title":'<b>Week</b>'+" "+'<b></b>','visible': True, 'showticklabels': True},showlegend= False,plot_bgcolor='#FFFFFF',
                     legend=dict(yanchor="bottom",orientation='h',y=-0.40,xanchor="center",x=0.50),
                    margin=dict(t=20, b=10, l=70, r=10))
            chart3=fig

        if radio_items9_value=="A":  
            df5=df[(df['PRODUCT_ID'].isin(demo_dropdown17_value))]
            df5['Date']=pd.to_datetime(df5['TRX_DATE'],errors = 'coerce')
            df5 =df5.sort_values("Date").reset_index(drop=True)
            df5['WeekNum'] = df5['Date'].dt.strftime('%W')
            df5["Week"]=str(' Week')
            df5["Week_Trend"] = df5["WeekNum"].astype(str)+ df5["Week"]
            df5["Week_Trend1"] = "(Product_ID-"+df5['PRODUCT_ID']+" "+"Type-"+df5['Type']+","+"Validity-"+df5['Validity']+")"
            
            #print(df5)
            tab = pd.crosstab([df5['Week_Trend']],df5['Week_Trend1'],df5.PRODUCT_ID,aggfunc="count",margins=True).reset_index()

            #print(tab)
            tab=tab.drop(['All'], axis = 1)
            tab=tab.drop(tab.tail(1).index) 
            df2 = tab.melt('Week_Trend', var_name='cols',  value_name='vals')
            
            fig=px.line(df2, x='Week_Trend' , y='vals' , color='cols',labels={"cols": " "},text='cols')
            fig.update_traces(mode="markers+lines",
                                    hovertemplate = 'Week: %{x}<br>Description: %{text}<br>Count: %{y}<extra></extra>')                              
            fig.update_layout(yaxis={'categoryorder': 'total ascending',"title":'<b>Product Count</b>'},
                              xaxis={"title":'<b>Week</b>'+" "+'<b></b>','visible': True, 'showticklabels': True},showlegend= False,plot_bgcolor='#FFFFFF',
                     legend=dict(yanchor="bottom",orientation='h',y=-0.40,xanchor="center",x=0.50),
                    margin=dict(t=10, b=10, l=70, r=10))
            chart4=fig
            
        if radio_items8_value=="B":
            df2=df[(df['PRODUCT_ID'].isin(demo_dropdown17_value))]
            df2['Date']=pd.to_datetime(df2['TRX_DATE'],errors = 'coerce')
            df2 =df2.sort_values("Date").reset_index(drop=True)
            df2['WeekNum'] = df2['Date'].dt.strftime('%W')
            df2["Week"]=str(' Week')
            df2["Week_Trend"] = df2["WeekNum"].astype(str)+ df2["Week"]
            df2["Week_Trend1"] = "(Product_ID-"+df2['PRODUCT_ID']+" "+"Type-"+df2['Type']+","+"Validity-"+df2['Validity']+")"
            
            #print(df5)
            cg=df2[(df2['CG/TG']=='CG')]
            tab = pd.crosstab([cg['Week_Trend']],cg['Week_Trend1'],cg.PRICE,aggfunc="sum",margins=True).reset_index()
            #print(tab)
            tab=tab.drop(['All'], axis = 1)
            tab=tab.drop(tab.tail(1).index) 
            df2 = tab.melt('Week_Trend', var_name='cols',  value_name='vals')
            
            fig=px.line(df2, x='Week_Trend' , y='vals' , color='cols',labels={"cols": " "},text='cols')

            fig.update_traces(mode="markers+lines",
                              hovertemplate = 'Week: %{x}<br>Description: %{text}<br>Revenue: %{y}<extra></extra>')
            fig.update_layout(yaxis={'categoryorder': 'total ascending',"title":'<b>Product Revenue</b>'},
                              xaxis={"title":'<b>Week</b>'+" "+'<b></b>','visible': True, 'showticklabels': True},showlegend= False,plot_bgcolor='#FFFFFF',
                     legend=dict(yanchor="bottom",orientation='h',y=-0.40,xanchor="center",x=0.50),
                    margin=dict(t=20, b=10, l=70, r=10))
            chart3=fig

        if radio_items9_value=="B":
            df3=df[(df['PRODUCT_ID'].isin(demo_dropdown17_value))]
            df3['Date']=pd.to_datetime(df3['TRX_DATE'],errors = 'coerce')
            df3 =df3.sort_values("Date").reset_index(drop=True)
            df3['WeekNum'] = df3['Date'].dt.strftime('%W')
            df3["Week"]=str(' Week')
            df3["Week_Trend"] = df3["WeekNum"].astype(str)+ df3["Week"]
            df3["Week_Trend1"] = "(Product_ID-"+df3['PRODUCT_ID']+" "+"Type-"+df3['Type']+","+"Validity-"+df3['Validity']+")"

            print(df3)
            cg=df3[(df3['CG/TG']=='CG')]
            tab = pd.crosstab([cg['Week_Trend']],cg['Week_Trend1'],cg.PRODUCT_ID,aggfunc="count",margins=True).reset_index()
            #print(tab)
            tab=tab.drop(['All'], axis = 1)
            tab=tab.drop(tab.tail(1).index) 
            df2 = tab.melt('Week_Trend', var_name='cols',  value_name='vals')

            fig=px.line(df2, x='Week_Trend' , y='vals' , color='cols',labels={"cols": " "},text='cols')
            fig.update_traces(mode="markers+lines",
                                    hovertemplate = 'Week: %{x}<br>Description: %{text}<br>Count: %{y}<extra></extra>')                              
            fig.update_layout(yaxis={'categoryorder': 'total ascending',"title":'<b>Product Count</b>'},
                              xaxis={"title":'<b>Week</b>'+" "+'<b></b>','visible': True, 'showticklabels': True},showlegend= False,plot_bgcolor='#FFFFFF',
                     legend=dict(yanchor="bottom",orientation='h',y=-0.40,xanchor="center",x=0.50),
                    margin=dict(t=10, b=10, l=70, r=10))
            chart4=fig

        if radio_items8_value=="C":
            df6=df[(df['PRODUCT_ID'].isin(demo_dropdown17_value))]
            df6['Date']=pd.to_datetime(df6['TRX_DATE'],errors = 'coerce')
            df6 =df6.sort_values("Date").reset_index(drop=True)
            df6['WeekNum'] = df6['Date'].dt.strftime('%W')
            df6["Week"]=str(' Week')
            df6["Week_Trend"] = df6["WeekNum"].astype(str)+ df6["Week"]
            df6["Week_Trend1"] = "(Product_ID-"+df6['PRODUCT_ID']+" "+"Type-"+df6['Type']+","+"Validity-"+df6['Validity']+")"

            tg1=df6[(df6['CG/TG']=='TG')]
            tab = pd.crosstab([tg1['Week_Trend']],tg1['Week_Trend1'],tg1.PRICE,aggfunc="sum",margins=True).reset_index()
            tab=tab.drop(['All'], axis = 1)
            tab=tab.drop(tab.tail(1).index) 

            df2 = tab.melt('Week_Trend', var_name='cols',  value_name='vals')

            print(df2)
            fig=px.line(df2, x='Week_Trend' , y='vals' , color='cols',labels={"cols": " "},text='cols')

            fig.update_traces(mode="markers+lines",
                              hovertemplate = 'Week: %{x}<br>Description: %{text}<br>Revenue: %{y}<extra></extra>')
            fig.update_layout(yaxis={'categoryorder': 'total ascending',"title":'<b>Product Revenue</b>'},
                              xaxis={"title":'<b>Week</b>'+" "+'<b></b>','visible': True, 'showticklabels': True},showlegend= False,plot_bgcolor='#FFFFFF',
                     legend=dict(yanchor="bottom",orientation='h',y=-0.40,xanchor="center",x=0.50),
                    margin=dict(t=20, b=10, l=70, r=10))
            chart3=fig
            
        if radio_items9_value=="C":
            df7=df[(df['PRODUCT_ID'].isin(demo_dropdown17_value))]
            
            df7['Date']=pd.to_datetime(df7['TRX_DATE'],errors = 'coerce')
            df7 =df7.sort_values("Date").reset_index(drop=True)
            df7['WeekNum'] = df7['Date'].dt.strftime('%W')
            df7["Week"]=str(' Week')
            df7["Week_Trend"] = df7["WeekNum"].astype(str)+ df7["Week"]
            df7["Week_Trend1"] = "(Product_ID-"+df7['PRODUCT_ID']+" "+"Type-"+df7['Type']+","+"Validity-"+df7['Validity']+")"
            
            print(df7)
            cg2=df7[(df7['CG/TG']=='TG')]
            tab =pd.crosstab([cg2['Week_Trend']],cg2['Week_Trend1'],cg2.PRODUCT_ID,aggfunc="count",margins=True).reset_index()
            tab=tab.drop(['All'], axis = 1)
            tab=tab.drop(tab.tail(1).index) 

            df2 = tab.melt('Week_Trend', var_name='cols',  value_name='vals')
            
            fig=px.line(df2, x='Week_Trend' , y='vals' , color='cols',labels={"cols": " "},text='cols')
            fig.update_traces(mode="markers+lines",
                                    hovertemplate = 'Week: %{x}<br>Description: %{text}<br>Count: %{y}<extra></extra>')                              
            fig.update_layout(yaxis={'categoryorder': 'total ascending',"title":'<b>Product Count</b>'},
                              xaxis={"title":'<b>Week</b>'+" "+'<b></b>','visible': True, 'showticklabels': True},showlegend= False,plot_bgcolor='#FFFFFF',
                     legend=dict(yanchor="bottom",orientation='h',y=-0.40,xanchor="center",x=0.50),
                    margin=dict(t=10, b=10, l=70, r=10))
            chart4=fig

    return [chart3,chart4]

# if __name__ == '__main__':

#     app.run_server(host='10.254.254.90',port=9190)
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050)

