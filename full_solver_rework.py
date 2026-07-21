import streamlit as st
from time import *
def solve_standered_form(a=1,b=1,c=1):
    determintant = b**2 - (4* a* c)

    if determintant == 0:
        r = (b*-1)/(2*a)
        st.write(f"Your quadratic has one root, that root is ({r},0)")

    elif determintant > 0:
        st.write('determintant is > 0')
        #return the 2 roots
    else:
        st.write("The roots are complex the numbers below are just estimations!")
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
input_tab,output_tab= st.tabs(['Inputs', 'Outputs'])
with input_tab:
    st.write("Input the coefficents of ax^2 + bx + c")
    a = st.number_input("A", help="Enter the A term of your quadratic",placeholder="Enter your A Term",width=250,value=1.00)
    b = st.number_input("B", help="Enter the B term of your quadratic",placeholder="Enter your B Term",width=250,value=1.00)
    c = st.number_input("C", help="Enter the C term of your quadratic",placeholder="Enter your C Term",width=250, value=1.00)
with output_tab:
    solve_standered_form(a,b,c)






