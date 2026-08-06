from quadratic_solver_functions import *
import streamlit as st
from time import *
import numpy as np 
import pandas as pd
from math import sqrt
from fractions import Fraction
import numpy as np

if "Tabs" not in st.session_state:
    st.session_state["Tabs"] = None


standered_form_inputs,factored_form_inputs,outputs = st.tabs(["Standered Form Inputs", "Factored Form Inputs", "Outputs"], key="Tabs", on_change="rerun")

with standered_form_inputs:
    a = st.number_input("A",help="Enter The A term of your quadratic", value=1)
    b = st.number_input("B",help="Enter The B term of your quadratic", value=1)
    c = st.number_input("C",help="Enter The C term of your quadratic", value=1)
    st.write(f'{a},{b},{c}')

    equation_in_factored_form = factor_standered_form_quadratic(a,b,c)
    if equation_in_factored_form:
        st.write(equation_in_factored_form)
    else:
        st.write('...')
st.write(st.session_state['Tabs'])

