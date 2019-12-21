import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.offline as offline
from plotly.graph_objs import *
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# pd.options.mode.chained_assignment = None

df = pd.read_csv('data.csv')

df_year = df[(df['Year'] == 2015)]

scl = [[0.0, '#ffffff'], [0.2, '#ff9999'], [0.4, '#ff4d4d'],
        [0.6, '#ff1a1a'], [0.8, '#cc0000'], [1.0, '#4d0000']]

for col in df.columns:
    df_year.loc[col] = df_year[col].astype(str)

x = "State: " + df_year['ST'] + '<br>'+ 'Job Title: ' + df_year['OCC_TITLE'] + '<br>'+ 'Annual Sal: ' + '$' + df_year['A_MEAN']

# df_year['text'] = df_year['STATE'] + '<br>' + df_year['ST'] + '<br>'  + ' Job ' + '<br>' + df_year['OCC_TITLE'] + '<br>' + df_year['A_MEAN']
# 'Fruits ' + df_year['total fruits'] + ' Veggies ' + df_year['total veggies'] + '<br>' + \
# 'Wheat ' + df_year['wheat'] + ' Corn ' + df_year['corn']

fig = go.Figure(data=go.Choropleth(
    locations=df['ST'],
    z=df['A_MEAN'],
    locationmode='USA-states',
    colorscale=scl,
    autocolorscale=False,
    text=x,  # hover text 
    marker_line_color='white',  # line markers between states
    colorbar_title="USD"
))

fig.update_layout(
    title_text='Technical Job<br>(Hover for breakdown)',
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=False,  # lakes
        lakecolor='rgb(255, 255, 255)'),
)

fig.show()
