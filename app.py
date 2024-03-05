import streamlit as st
import numpy as np
import pickle

st.title('👋 **Hello!!**')
st.write('On essaie de prédire ici le type de fleur en se basant sur ses caractéristiques')
with open('model.pkl', 'rb') as file:
    loaded = pickle.load(file)

sepal_length = st.slider('Sepal length', 4.3, 7.9, 5.4)
sepal_width = st.slider('Sepal width', 2.0, 4.4, 3.4)
petal_length = st.slider('Petal length', 1.0, 6.9, 1.3)
petal_width = st.slider('Petal width', 0.1, 2.5, 0.2)

if st.button('Predict'):
    prediction = loaded.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    class_names = ['Setosa', 'Versicolor', 'Virginica']
    predicted_class = class_names[prediction[0]]
    class_colors = {'Setosa': '#FFC0CB', 'Versicolor': '#ADD8E6', 'Virginica': '#90EE90'}
    st.markdown(f'<div style="background-color: {class_colors[predicted_class]};padding:10px;border-radius:10px;">'
                f'<h1 style="color:white;text-align:center;">{predicted_class}</h1>'
                '</div>', unsafe_allow_html=True)

