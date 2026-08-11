from quadratic_solver_functions import *
import streamlit as st
from time import *
import pandas as pd
from math import sqrt
from fractions import Fraction
import numpy as np

if "Tabs" not in st.session_state:
    st.session_state["Tabs"] = None

if "Factored_Equation" not in st.session_state:
    st.session_state["Factored_Equation"] = None

if "Standered_Equation" not in st.session_state:
    st.session_state["Standered_Equation"] = None

if "last_tab_with_data_entered" not in st.session_state:
    st.session_state["last_tab_with_data_entered"] = None

if 'a' not in st.session_state:
    st.session_state['a'] = None
if 'b' not in st.session_state:
    st.session_state['b'] = None
if 'c' not in st.session_state:
    st.session_state['c'] = None
standered_form_inputs,factored_form_inputs,outputs = st.tabs(["Standered Form Inputs", "Factored Form Inputs", "Outputs"], key="Tabs", on_change="rerun")

with standered_form_inputs:
    a = st.number_input("A",help="Enter The A term of your quadratic", value=1,on_change=standered_form_inputs_input_on_change)
    b = st.number_input("B",help="Enter The B term of your quadratic", value=-5,on_change=standered_form_inputs_input_on_change)
    c = st.number_input("C",help="Enter The C term of your quadratic", value=6,on_change=standered_form_inputs_input_on_change)
    if st.session_state["last_tab_with_data_entered"] == "standered_form_inputs":
        if b >= 0 and c >= 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 + {b}x + {c}'
        elif b < 0 and c < 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 - {-b}x - {-c}'
        elif b < 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 - {-b}x + {c}'
        elif c < 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 + {b}x - {-c}'
        st.session_state['a'] = a
        st.session_state['b'] = b
        st.session_state['c'] = c
        equation_in_factored_form = factor_standered_form_quadratic(a,b,c)
        if equation_in_factored_form:
            st.session_state["Factored_Equation"] = equation_in_factored_form
        else:
            st.session_state["Factored_Equation"] = "This calculator does not correctly calculate the factored form for this equation"
    



with factored_form_inputs:
    factored_equation = st.text_input("Equation",help="Enter your quadratic in factored form.",value="(1x-3.0)(1.0x-2)",on_change=factored_form_inputs_on_change)
    if st.session_state["last_tab_with_data_entered"] == "factored_form_inputs":
        st.session_state["Factored_Equation"] = factored_equation
        standered_equation,a,b,c = parse_factored_form_quadratic(factored_equation)
        st.session_state['a'] = a
        st.session_state['b'] = b
        st.session_state['c'] = c
        if b >= 0 and c >= 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 + {b}x + {c}'
        elif b < 0 and c < 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 - {-b}x - {-c}'
        elif b < 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 - {-b}x + {c}'
        elif c < 0:
            st.session_state["Standered_Equation"] = f'{a}x^2 + {b}x - {-c}'
        print(standered_equation)




with outputs:
    if  st.session_state["Factored_Equation"] == None:
        st.write("Please enter a equation.")
    else:
        a = st.session_state['a']
        b = st.session_state['b']
        c = st.session_state['c']
        roots,identifyer = solve_standered_form(a,b,c)
        
        if identifyer == 1:
            root1 = roots
            root2 = 'N/A'
            vertex = root1
        elif identifyer == 2:    
            root1 = roots[0]
            root2 = roots[1]
            vertex = roots[2]
        else:
            root1 = "N/A"
            root2 = "N/A"
            vertex = "This calculator does not calculate the vertex for parabolas with imaginary roots"
            
        data = {"Standered Form":st.session_state["Standered_Equation"],"Factored Equation": st.session_state["Factored_Equation"], "Root One": root1,"Root Two": root2, "Vertex": vertex}
        st.table(data)
