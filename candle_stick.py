import streamlit as st
import plotly.graph_objs as go
from data import get_data

data = get_data()

candlestick = go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'])

layout = go.Layout(title = "Reliance",
                   xaxis= dict(title = 'Date'),
                   yaxis = dict(title= 'Price')

                   ,height=500,width=800
                   )

chart= [candlestick]

config = {
    'displayModeBar': True,
    'displaylogo':False,
    'modeBarButtonsToRemove': ['lasso2d', 'select2d', 'autoScale2d', 'resetScale2d', 'toggleSpikelines', 'zoomIn2d', 'zoomOut2d', 'hoverClosestCartesian', 'hoverCompareCartesian']
}

fig = go.Figure(data= chart,layout=layout)


st.plotly_chart(fig,config=config)


