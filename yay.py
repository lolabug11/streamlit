import streamlit as st
from math import *
st.title("Quadratic solver")
a = st.slider('A', 0.0,10000.0)
b = st.slider('B', 0.0,10000.0)
c = st.slider('C', 0.0,10000.0)
b_squared_minus_four_a_c = b** - 4 * a * c
positive = -b + sqrt(b_squared_minus_four_a_c)/2*a
negative = -b - sqrt(b_squared_minus_four_a_c)/2*a
if positive == negative:
    st.write(f'The Awnser is {positive}')
else:
    st.write(f'The + of the +- is {positive}\nThe - of the -+ is {negative}')
