import streamlit as st
from math import *
import pandas as pd
import numpy as np
st.title("Quadratic solver")
a = float(st.text_input("A", 1.0,help="Enter the a value"))
b = float(st.text_input("B", 0.0))
c = float(st.text_input("C", 0.0))
b_squared_minus_four_a_c = b**2 - 4 * a * c
if b_squared_minus_four_a_c > 0:
    positive = -b + sqrt(b_squared_minus_four_a_c)/2*a
    negative = -b - sqrt(b_squared_minus_four_a_c)/2*a
    vertex = (positive+negative)/2
    if positive == negative:
        st.write(f'The Solution is {positive}')
    else:
        data = {"plus":[positive], "minus":[negative], "vertex":[vertex]}
        dataframe = pd.DataFrame(data)
        st.table(dataframe,width="content")
else:
    st.write("The vertexes would be complex numbers!")
