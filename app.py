import streamlit as st
from datetime import datetime
import math

st.title("Heritage Trail - Gold Costing")

# Excel TRUNC function exact equivalent
def excel_trunc(value, decimals=2):
    factor = 10 ** decimals
    return math.trunc(value * factor) / factor

# Display current date and time
now = datetime.now()
st.write(f"**Date & Time:** {now.strftime('%Y-%m-%d %H:%M:%S')}")

# User Inputs (initially empty)
top = st.number_input("Top:", value=None, step=0.01)
down = st.number_input("Down:", value=None, step=0.01)
price = st.number_input("Price:", value=None, step=0.01)

# Perform calculations when inputs are provided
if top and down:
    # Pounds calculation (exact Excel TRUNC)
    pounds = excel_trunc(top / 7.75, 2)

    # Density calculation (exact Excel TRUNC)
    density = excel_trunc(top / down, 2)

    # Karat calculation (exact Excel TRUNC)
    if density != 0:
        karat = excel_trunc((density - 10.51) * 52.838 / density, 2)
    else:
        karat = 0

    # Check if Karat is within the valid range (20 - 24)
    if karat < 20 or karat > 24:
        st.warning("**Karat value is outside the valid range (20 - 24). Please review your inputs.**")

    # Display intermediate calculations
    st.write(f"**Pounds:** {pounds:.2f}")
    st.write(f"**Density:** {density:.2f}")
    st.write(f"**Karat:** {karat:.2f}")

    # Final Amount calculation (exact Excel TRUNC, 0 decimals)
    if price:
        amount = excel_trunc((karat / 23) * price * pounds, 0)

        # Display Final Results
        st.subheader("Calculated Gold Value")
        st.write("---")
        st.write(f"**Top:** {top}")
        st.write(f"**Down:** {down}")
        st.write(f"**Price:** {price}")
        st.write(f"**Pounds:** {pounds:.2f}")
        st.write(f"**Density:** {density:.2f}")
        st.write(f"**Karat:** {karat:.2f}")

        st.write("---")
        st.write(f"### Total Amount (GHC): {amount:,.2f}")
    else:
        st.warning("Please enter the Price value to calculate the gold value.")
else:
    st.warning("Please enter both Top and Down values to calculate Pounds, Density, and Karat.")
