import streamlit as st

ans = 0
num1 = st.number_input('Insert 1st number')
num2 = st.number_input('Insert 2nd number')
if st.button("Add"):
    ans = num1 + num2
elif st.button("Minus"):
    if (num1 > num2):
        ans = num1 - num2
    elif (num2 > num1):
        ans = num2 - num1
elif st.button("Multi"):
    ans = num1 * num2
elif st.button("Div"):
    ans = num1 / num2
    
st.write("Answer = ", ans)
    