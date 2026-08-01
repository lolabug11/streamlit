import streamlit as st
from time import *
import numpy as np 
import pandas as pd
from math import sqrt
from fractions import Fraction
def find_roots_with_discriminant_greater_than_0(a:float,b:float,c:float,discriminant:float):
    r1 = (-b + sqrt(discriminant))/(2*a)
    r2 = (-b - sqrt(discriminant))/(2*a)
    if '.' in str((-b + sqrt(discriminant))/(2*a)):
        r1 = Fraction(str((-b + sqrt(discriminant))/(2*a)))
        r1 = r1.limit_denominator(1000)
    if '.' in str((-b - sqrt(discriminant))/(2*a)):
        r2 = Fraction(str((-b - sqrt(discriminant))/(2*a)))
        r2 = r2.limit_denominator(1000)
    vertex_x = (r1+r2)/2
    x = vertex_x
    vertex_y = ((a) * (vertex_x**2)) + (vertex_x * b) + c
    if '.' in str(vertex_y):
        vertex_y = Fraction(str(vertex_y))
        vertex_y = vertex_y.limit_denominator(1000)
    return [str(r1),str(r2),str(vertex_x),str(vertex_y)]
def find_roots_with_discriminant_less_than_0(a:float,b:float,c:float,discriminant:float):
    r1 = round((-b + sqrt(-discriminant))/(2*a), 4)
    r2 = round((-b - sqrt(-discriminant))/(2*a), 4)
    return [(f'{r1}i,0'),str(f'{r2}i,0')]
    
def solve_standered_form(a=1,b=1,c=1) -> tuple:
    """Solves a quadratic equation givin a term b term and c term
    Args:
        a: the a term of the quadratic
        b: the b term of the quadratic
        c: the c term of the quadratic  
    Returns:
        Tuple: a tuple contaning
            - cords (list): returns a list of tuples that contains the cords of the [first_root,second_root (if applicable),vertex (if applicable)]
            - identifyer (int): returns a number to help identify how many roots the equation has. If the equation has one solution the identifyer will equal 1, if the equation has 2 real solutions the identifyer will equal 2, if the equation has 2 imaginary solutions the identifyer will equal 3
    """
    discriminant = (b**2) - (4 * a * c)
    print(f'discriminant = {discriminant}')
    if discriminant == 0:
        r = (b*-1)/(2*a)
        return (r,0), 1
    elif discriminant > 0:
        return find_roots_with_discriminant_greater_than_0(a=a,b=b,c=c,discriminant= discriminant), 2
    else:
        return find_roots_with_discriminant_less_than_0(a = a, b = b, c = c, discriminant=discriminant), 3
def parse_factored_form_quadratic(quadratic:str):
    before_first_x = True
    before_first_parenthacys = True
    before_second_x = True
    a = ''
    b = ''
    c = ''
    d = ''
    for char in quadratic:     

        if char == '-':

            if before_first_x:

                a += char

            elif not before_first_x and before_first_parenthacys:

                b += char

            elif not before_first_x and not before_first_parenthacys and before_second_x:

                c += char

            else:

                d += char

        elif char.isnumeric():

            if before_first_x:

                a += char

            elif not before_first_x and before_first_parenthacys:

                b += char

            elif not before_first_x and not before_first_parenthacys and before_second_x:
                
                c += char

            else:

                d += char

        else:

            if char != '(':

                if char != '+':

                    if before_first_x:

                        before_first_x = False

                    elif not before_first_x and before_first_parenthacys:

                        before_first_parenthacys = False

                    elif not before_first_parenthacys and not before_first_x and before_second_x:

                        before_second_x = False

        print(f'-------\nchar = {char}\nbefore_first_x = {before_first_x}\nbefore first perenthacys = {before_first_parenthacys}\n before second x = {before_second_x}\n a = {a}\n b = {b} \nc = {c}\nd = {d}\n-------')

    if a == '':

        a = 1.0

    else:

        a = float(a)
        a = round(a,4)

    if b == '':

        b = 1.0

    else:

        b = float(b)
        b = round(b,4)

    if c == '':

        c = 1.0

    else:

        c = float(c)
        c = round(c,4)

    if d == '':

        d = 1.0

    else:

        d = float(d)
        d = round(d,4)

    org_a = a
    org_b = b
    org_c = c
    a = org_a * org_c
    b = (org_a * d) + (org_c * b)
    c = org_b * d
    st.session_state['equation'] = f'{a}x^2 + {b}x + c'
    
    return solve_standered_form(a=a,b=b,c=c)




def GCD(a,b):
    if a < 0 :
        a *= -1
    if b < 0:
        b *= -1
    a_factor_pairs = {}
    b_factor_pairs = {}
    for number in range(int(a)):
        number += 1
        if a % number == 0:
            a_factor_pairs[number] = a/number
    for number in range(int(b)):
        number += 1
        if b % number == 0:
            b_factor_pairs[number] = b/number
    gcf = {}
    for key in a_factor_pairs:
        if key in b_factor_pairs and key :
            gcf[a] = [key,a_factor_pairs[key]]
            gcf[b] = [key,b_factor_pairs[key]]
    gcf = gcf[a][0]
    return gcf



st.markdown("##### QUADRATIC SOLVER!!!!")

if 'in_factored_form' not in st.session_state:

    st.session_state['in_factored_form'] = True

if 'quadratic_tab' not in st.session_state:

    st.session_state['quadratic_tab'] = 0

if 'equation' not in st.session_state:

    st.session_state['equation'] = None

solve_standered_form_input_tab,factored_form_input,output_tab= st.tabs(['Standered form Inputs', 'Factored Form Input', 'Outputs'],key="quadratic_tab",on_change="rerun")


if st.session_state['quadratic_tab'] == "Standered form Inputs":

    st.session_state['in_factored_form'] = False

elif st.session_state['quadratic_tab'] == "Factored Form Input":

    st.session_state['in_factored_form'] = True


with solve_standered_form_input_tab:

    st.write("Input the coefficents of ax^2 + bx + c")
    a = st.number_input("A", help="Enter the A term of your quadratic",placeholder="Enter your A Term",width=250,value=1.00)
    b = st.number_input("B", help="Enter the B term of your quadratic",placeholder="Enter your B Term",width=250,value=1.00)
    c = st.number_input("C", help="Enter the C term of your quadratic",placeholder="Enter your C Term",width=250, value=1.00)
    st.session_state['equation'] = f'{a}x^2 + {b}x + {c}'

with factored_form_input:

    equation = st.text_input("Enter your quadratic",placeholder="Enter your quadratic")

with output_tab:

    if st.session_state['in_factored_form']  == None:

        if st.session_state['quadratic_tab'] == "Outputs":

            st.write('Please enter either a standered form quadratic or a factored form quadratic.')

    elif  st.session_state['in_factored_form']:

        points_on_cord_plain, identifyer = parse_factored_form_quadratic(st.session_state['equation'])

    elif not st.session_state['in_factored_form']:

        points_on_cord_plain, identifyer = solve_standered_form(a,b,c)


    if identifyer == 1:

        st.write(f"Your quadratic equation {st.session_state['equation']} has 1 real root\nYour equations root is {points_on_cord_plain[0]}")

    elif identifyer == 2:
        
        st.write(f'Your quadratic equation {st.session_state['equation']} has 2 real roots')
        data = {"plus":[f'({points_on_cord_plain[1]}, 0)'], 'minus': [ f'({points_on_cord_plain[0]},0)'], 'vertex': [f'({points_on_cord_plain[2]}, {points_on_cord_plain[3]})']}
        dataframe = pd.DataFrame(data)
        st.table(data=dataframe,width="content")

    elif identifyer == 3: 

        st.write(f"Your quadrtatic equation {st.session_state['equation']} has 2 imaginary roots")




