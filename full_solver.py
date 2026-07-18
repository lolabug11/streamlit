import streamlit as st
from math import *
import pandas as pd
import numpy as np
import time as t
from decimal import Decimal
def GCF(a,c,b):
    a_factor_pairs = {}
    b_factor_pairs = {}
    c_factor_pairs = {}
    for number in range(a):
        number += 1
        if a % number == 0:
            a_factor_pairs[number] = a/number
    for number in range(b):
        number += 1
        if b % number == 0:
            b_factor_pairs[number] = b/number
    for number in range(c):
        number += 1
        if c % number == 0:
            c_factor_pairs[number] = c/number
    gcf = {}
    for key in a_factor_pairs:
        if key in b_factor_pairs and key in c_factor_pairs:
            gcf[a] = [key,a_factor_pairs[key]]
            gcf[b] = [key,b_factor_pairs[key]]
            gcf[c] = [key,c_factor_pairs[key]]
    st.write(gcf)



GCF(1000000,0,0)
st.title("Quadratic Solver!!!")
quadratic = st.text_input("Equation",help="Enter your quadratic Equation")
if quadratic != '':
    is_in_factored = False
    is_in_standered = False
    if '(' in quadratic or ')' in quadratic:
        is_in_factored = True
    elif '^2' in quadratic:
        is_in_standered = True
    else:
        st.Write("Please enter a valid equation!")
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
                    is_square_2 = False
                else:
                    if before_x_squared and before_x_to_the_first:
                        a += char
                    elif not before_x_squared and before_x_to_the_first:
                        b += char
                    elif not before_x_squared and not before_x_to_the_first:
                        c += char
                    else:
                        st.write("Something whent horribly wrong for you to see this >:( what did you do????")
            else:
                if char == "^":
                    is_square_2 = True
                elif char == "x":
                    if before_x_squared:
                        before_x_squared = False
                    elif not before_x_squared and before_x_to_the_first:
                        before_x_to_the_first = False
                    else:
                        st.write("FIX YOUR DAM CODE!!!")
        if int(a) == 0:
            a = 1
        else:
            a = round(float(a),3)
        b = round(float(b),3)
        c = round(float(c),3)

        d = a * c
        pairs = {}
        for i in range(int(d)):
            i += 1
            if d % i == 0 :
                if d/i not in pairs.values():
                    pairs[i] = d/i
        st.write(pairs)
        factors = []
        for pair in pairs:
            if int(pair) + int(pairs[pair]) == b:
                factors.append([int(pair),int(pairs[pair])])



        b_squared_minus_four_a_c = ((b**2) -( 4 * a * c))

        if b_squared_minus_four_a_c > 0:
            positive = ((b * -1) + sqrt((b**2) - (4*a*c)))/(2*a)
            negative = (((b * -1) - (sqrt(b_squared_minus_four_a_c)))/((2)*a))
            vertex = (positive+negative)/2
            if b_squared_minus_four_a_c == 0:
                st.write(f'The Solution is {positive}')
            else:
                data = {"plus":[f"({positive},0)"], "minus":[f"({negative},0)"], "vertex":[f"({vertex},{a*(vertex**2)+b*vertex+c})"]}
                dataframe = pd.DataFrame(data)
                st.table(dataframe,width="content")

        else:
            st.write("The vertexes would be complex numbers!")

        





    elif is_in_factored:
        terms = []
        current_term = ""
        for char in quadratic:
            if char != "(" and char != ")":
                current_term  += char
            else:
                if current_term != "":
                    
                    terms.append(current_term)
                    current_term = ''
        before_x = True
        second_term = False
        a = ""
        b = ""
        c = ""
        d = ""
        for term in terms:
            for char in term:
                if char == "x":
                    before_x = False

                elif char.isnumeric() or char == '-' :
                    if before_x and not second_term:
                        a += char
                    elif not before_x and not second_term:
                        b += char
                    elif before_x and second_term: 
                        c += char
                    elif not before_x and second_term:
                        d += char
                    else:
                        st.title("WHAT DID YOU DO")
                
            before_x = True
            second_term = True
        if a == "":
            a = 1
        else: 
            a = float(a)
        if  c == '':
            c = 1
        else: 
            c = float(c)
        b = float(b)
        d = float(d)
        print(f'a = {a} b = {b} c = {c} d = {d}')
        standered_form = f'{(a * c)}x^2 + {(c *b) + (a * d)}x + {b * d} = 0'
        st.write(standered_form)
        org_a = a
        org_b = b
        org_c = c
        a = org_a*c
        b = (c*b)+(org_a*d)

        c =  org_b * d
        a = round(a,3)
        b = round(b,3)
        
        c = round(c,3)
        b_squared_minus_four_a_c = ((b**2) -( 4 * a * c))
        if b_squared_minus_four_a_c > 0:
            positive = ((b * -1) + sqrt((b**2) - (4*a*c)))/(2*a)
            negative = round(((b * -1) - (sqrt(b_squared_minus_four_a_c)))/((2)*a),3)
            vertex = (positive+negative)/2
            if b_squared_minus_four_a_c == 0:
                st.write(f'The Solution is {positive}')
            else:
                data = {"plus":[f"({round(positive,3)},0)"], "minus":[f"({round(negative,3)},0)"], "vertex":[f"({vertex},{round(a*(vertex**2)+b*vertex+c, 3)})"]}
                dataframe = pd.DataFrame(data)
                st.table(dataframe,width="content")
        else:
            st.write("The vertexes would be complex numbers!")