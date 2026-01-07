import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('dataframe/vehicles.csv') # lendo os dados

st.header('Análise de anúncios de veículos')

hist_button = st.button('Criar histograma') # criar um botão

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

criar um histograma
    fig_hist = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão') # criar um botão

if scatter_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão entre preço e kilometragem para o conjunto de dados de anúncios de vendas de carros')

criar um histograma
    fig_scatter = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)
