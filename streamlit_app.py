import streamlit
import pandas

streamlit.title('This is a title')

streamlit.header('This is a header')
streamlit.text('This is a text')
streamlit.text('This is another text')
streamlit.text('This is yet another text with emojis 🥣 🥗 🐔 🥑🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)