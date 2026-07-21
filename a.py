# The comments are buns dont trust them completly
# Enter either a standered form quadratic or a factored form quadratic in the following forms
# Standered form = ax^2 + bx + c
# Factored form  = (ax + b)(cx+d)

import streamlit as st
from math import *
import pandas as pd
import numpy as np
import time as t
from decimal import Decimal
# gets the greatist common factor of 3 numbers a b and c then returns it
def GCF(a ,b ,c ): 
    a = int(a)
    b = int(b)
    c = int(c)
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if c < 0:
        c *= -1

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
    

    gcf = gcf[a][0]

    return gcf


st.markdown("##### Quadratic Solver!!!")
quadratic = st.text_input("Equation",help="Enter your quadratic Equation")
if quadratic != '':


    #check if equation is in standered form ax^2 + bx + c or factored (ax +b )(cx+d)
    is_in_factored = False
    is_in_standered = False
    if '(' in quadratic or ')' in quadratic:
        is_in_factored = True
    elif '^2' in quadratic:
        is_in_standered = True
    else:
        st.write("Please enter a valid equation!")
    
    if is_in_standered:
        

        # pull a b c from ax^2 + bx + c
        before_x_squared = True
        before_x_to_the_first = True
        is_square_2 = False
        a = "0"
        b = ""
        c = ""

        for char in quadratic:
            if char.isnumeric() or char == "." or char == '-':
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

        # use a b and c to solve the quadratic formula
        b_squared_minus_four_a_c = ((b**2) -( 4 * a * c))

        if b_squared_minus_four_a_c == 0:
            positive = ((b * -1) + sqrt((b**2) - (4*a*c)))/(2*a)
            negative = (((b * -1) - (sqrt(b_squared_minus_four_a_c)))/((2)*a))
            vertex = (positive+negative)/2
            st.write(f"({vertex},{a*(vertex**2)+b*vertex+c})")
            complex_num = False
        elif b_squared_minus_four_a_c > 0:
            positive = ((b * -1) + sqrt((b**2) - (4*a*c)))/(2*a)
            negative = (((b * -1) - (sqrt(b_squared_minus_four_a_c)))/((2)*a))
            vertex = (positive+negative)/2

            data = {"plus":[f"({positive},0)"], "minus":[f"({negative},0)"], "vertex":[f"({vertex},{a*(vertex**2)+b*vertex+c})"]}
            dataframe = pd.DataFrame(data)
            st.table(dataframe,width="content")
            complex_num = False

        else:
            complex_num = True
            st.write("The vertexes would be complex numbers!")

        # factor out the greatist common factor and get the new equation
        if not complex_num:
            gcf = GCF(a,b,c)
            if gcf != 1:
                out_side_parenthacys = gcf
                a /= gcf
                b /= gcf
                c /= gcf
                st.write(f'{out_side_parenthacys}({a}x^2 + {b}x + {c})')
            # check if c is a perfict square and if 2 * sqrt of c = b


            if c > 0:
                sqrt_c = sqrt(c)
                if'.0' in str(sqrt_c):
                    if sqrt_c * 2 == b:
                        pass
                        #simplifys the equation as if the equation is a perfict square
                    



        





    elif is_in_factored:
        # seperate the terms of the factored equation
        terms = []
        current_term = ""
        for char in quadratic:
            if char != "(" and char != ")":
                current_term  += char
            else:
                if current_term != "":
                    
                    terms.append(current_term)
                    current_term = ''
        # extract a b c and d from the terms
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

        #convert the a b c and d into standered form to use quadratic formula
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