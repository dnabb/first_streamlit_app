import streamlit
import pandas

streamlit.title('This is a title')

streamlit.header('This is a header')
streamlit.text('This is a text')
streamlit.text('This is another text')
streamlit.text('This is yet another text with emojis 🥣 🥗 🐔 🥑🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)