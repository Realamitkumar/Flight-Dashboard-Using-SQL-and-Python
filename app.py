import streamlit as st
from db_helper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

# to run app: python -m streamlit run app.py

st.sidebar.title("Flights Analytics")

user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option == 'Check Flights':
    st.title("Check Flights")

    col1,col2 = st.columns(2)

    with col1:
        city = db.fetch_cities()
        source = st.selectbox('Source',sorted(city))
    with col2:
        city = db.fetch_cities()
        destination = st.selectbox('Destination',sorted(city))    

    if st.button('Search'):
        result = db.fetch_all_flights(source,destination)
        st.dataframe(result)

elif user_option == 'Analytics':
    st.title("Analytics")
    Airline,Frequency = db.fetch_flight_pie()
    #pie chart
    fig = go.Figure(
        go.Pie(
            labels=Airline,
            values=Frequency,
            hoverinfo='label+percent',
            textinfo='value')
    )
    st.header("Pie Chart")
    st.plotly_chart(fig)
# --------------------------------------------------------------    
    Airport,Busy = db.most_busiest_aiport()
    #bar
    fig = px.bar(

        x=Airport,
        y=Busy
    )
    st.plotly_chart(fig)
# --------------------------------------------------------------    
    Date,Number = db.no_of_flights()
    #bar
    fig = px.line(

        x=Date,
        y=Number
    )
    st.plotly_chart(fig)    

else:
    st.title("Tell Me About Your Project")    
