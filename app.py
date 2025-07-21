import streamlit as st
from datetime import datetime

st.title("Ghana Gold Value Determination")

# Display current date and time
now = datetime.now()
st.write(f"**Date & Time:** {now.strftime('%Y-%m-%d %H:%M:%S')}")

# User Inputs (empty fields for user input)
top = st.number_input("Top:", value=None, step=0.01)
down = st.number_input("Down:", value=None, step=0.01)
price = st.number_input("Price:", value=None, step=0.01)
pounds = st.number_input("Pounds:", value=None, step=0.01)
density = st.number_input("Density:", value=None, step=0.01)
karat = st.number_input("Karat:", value=None, step=0.01)

# Calculation (based on provided formula)
if all([top, down, price, pounds, density, karat]):
    amount = ((top - down) * price * pounds * density * karat) / 24

    # Display Results
    st.subheader("Calculated Gold Value")
    st.write("---")
    st.write(f"**Top:** {top}")
    st.write(f"**Down:** {down}")
    st.write(f"**Price:** {price}")
    st.write(f"**Pounds:** {pounds}")
    st.write(f"**Density:** {density}")
    st.write(f"**Karat:** {karat}")

    st.write("---")
    st.write(f"### Total Amount (GHC): {amount:,.2f}")
else:
    st.warning("Please enter all required values to calculate the gold value.")
