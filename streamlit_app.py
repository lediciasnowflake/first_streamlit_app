# create the main python file

import streamlit
import pandas

streamlit.title('My parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard boiled Eree-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", options = list(my_fruit_list.Fruit), default = ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list[my_fruit_list.Fruit[fruits_selected]]

streamlit.dataframe(fruits_to_show)






