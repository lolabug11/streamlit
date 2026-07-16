import streamlit as st
from math import *
import pandas as pd
import numpy as np
from decimal import Decimal
quadratic = st.text_input("Equation",help="Enter your quadratic Equation")
if quadratic != '':
    st.write("Is your equation in Standerd form or Factoerd Form?")
    is_in_standered = st.checkbox("Standered form")
    is_in_factored = st.checkbox("Factored Form")
    if is_in_standered:
        
        before_x_squared = True
        before_x_to_the_first = True
        is_square_2 = False
        a = "0"
        b = "0"
        c = "0"

        for char in quadratic:
            if char.isnumeric() or char == ".":
                if is_square_2:
                    print("square 2")
                    is_square_2 = False
                else:
                    if before_x_squared and before_x_to_the_first:
                        a += char
                    elif not before_x_squared and before_x_to_the_first:
                        b += char
                    elif not before_x_squared and not before_x_to_the_first:
                        c += char
                    else:
                        print("Something whent horribly wrong for you to see this >:( what did you do????")
            else:
                if char == "^":
                    is_square_2 = True
                elif char == "x":
                    if before_x_squared:
                        before_x_squared = False
                    elif not before_x_squared and before_x_to_the_first:
                        before_x_to_the_first = False
                    else:
                        print("FIX YOUR DAM CODE!!!")
        if int(a) == 0:
            a = 1
        else:
            a = Decimal(a)
        b = Decimal(b)
        c = Decimal(c)
        st.write("Do you want to factor or solve your equation?")
        want_to_solve = st.checkbox("Solve the equation")
        want_to_factor = st.checkbox("Factor the equation")


        if want_to_solve:
            b_squared_minus_four_a_c = Decimal((b**2) -( 4 * a * c))
            st.write(f'b^2 == {b**2}, 4ac = {4 * a * c}, a = {a} , b = {b} , c = {c}')
            st.write(b_squared_minus_four_a_c)
            if b_squared_minus_four_a_c > 0:
                positive = -b + sqrt(b_squared_minus_four_a_c)/Decimal(2)*a
                negative = Decimal(-b - Decimal(sqrt(b_squared_minus_four_a_c)))/Decimal(2)*a
                vertex = (positive+negative)/2
                if b_squared_minus_four_a_c == 0:
                    st.write(f'The Solution is {positive}')
                else:
                    data = {"plus":[f"({positive},0)"], "minus":[f"({negative},0)"], "vertex":[vertex]}
                    dataframe = pd.DataFrame(data)
                    st.table(dataframe,width="content")
            else:
                st.write("The vertexes would be complex numbers!")
        elif want_to_factor: 
            st.write("FUCK")
    elif is_in_factored:
        st.write("BITCH")