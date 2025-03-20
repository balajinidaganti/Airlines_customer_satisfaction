import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from sqlalchemy import create_engine
df = pd.read_csv('Invistico_Airline.csv')
df = df.replace(" ' "," ", regex=True)
print(df.head())
# Remove duplicate rows (based on all columns)
df = df.drop_duplicates()
# fill the blank details with zero
df = df.fillna(0)
# Save the cleaned Excel file
df.to_csv("cleaned_airlines.csv", index=False)
print("Updated CSV file saved successfully!")
username = "root"
password = "root"
host = "localhost"
port = "3306"
database = "airlines"
engine = create_engine("mysql+pymysql://root:root@localhost:3306/airlines")
df = pd.read_csv("cleaned_airlines.csv")
table_name = "airlines_data"
df.to_sql(table_name, con=engine, if_exists="replace", index=False)
print("CSV file successfully imported into the SQL database!")
# create Dashboard using Dash


# Load the cleaned data
df = pd.read_csv("cleaned_airlines.csv")
#create Dashboard using Dash and plotly
# Create Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Airline Passenger Satisfaction Dashboard"

# Define layout
app.layout = html.Div([
    html.H1("Airline Passenger Satisfaction Dashboard", style={'textAlign': 'center'}),
    dcc.Tabs(id="tabs", value='tab1', children=[
        dcc.Tab(label='Passenger Satisfaction Overview', value='tab1'),
        dcc.Tab(label='Flight Delays Analysis', value='tab2'),
        dcc.Tab(label='Service Ratings Analysis', value='tab3'),
        dcc.Tab(label='Demographic Analysis', value='tab4'),
        dcc.Tab(label='SQL Insights', value='tab5'),
    ]),
    html.Div(id='tabs-content'),
    html.Div([
        html.Label("Enter Custom SQL Query:"),
        dcc.Input(id='sql-input', type='text', value='SELECT * FROM airline_data LIMIT 10;', style={'width': '80%'}),
        html.Button('Run Query', id='run-query', n_clicks=0),
        html.Div(id='sql-output')
    ], style={'margin': '20px'})
])

# Callback to update tabs
@app.callback(
    Output('tabs-content', 'children'),
    Input('tabs', 'value')
)
def update_tab(tab_name):
    if tab_name == 'tab1':
        fig = px.pie(df, names='satisfaction', title='Overall Passenger Satisfaction')
        return html.Div([dcc.Graph(figure=fig)])
    elif tab_name == 'tab2':
        fig = px.box(df, x='Class', y='Arrival Delay in Minutes', title='Arrival Delays by Class')
        return html.Div([dcc.Graph(figure=fig)])
    elif tab_name == 'tab3':
        fig = px.scatter(df, x='Seat comfort', y='satisfaction', title='Seat Comfort vs Satisfaction')
        return html.Div([dcc.Graph(figure=fig)])
    elif tab_name == 'tab4':
        fig = px.histogram(df, x='Age', color='satisfaction', title='Satisfaction by Age Group', nbins=30)
        return html.Div([dcc.Graph(figure=fig)])
    elif tab_name == 'tab5':
        query = "SELECT Class, AVG('Arrival Delay in Minutes') AS Avg_Arrival_Delay FROM airline_data GROUP BY Class;"
        df_sql = pd.read_sql(query, conn)
        fig = px.bar(df_sql, x='Class', y='Avg_Arrival_Delay', title='Average Arrival Delay by Class')
        return html.Div([dcc.Graph(figure=fig)])
    return html.Div()
# Run the app
if __name__ == '__main__':
    app.run(debug=False)