import streamlit as st
from datetime import datetime

st.title("Ghana Gold Value Determination")

# Current date and time
now = datetime.now()
st.write(f"**Date & Time:** {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Inputs
top = st.number_input("Top:", value=None, step=0.01)
down = st.number_input("Down:", value=None, step=0.01)
price = st.number_input("Price:", value=None, step=0.01)

if top and down:
    # Pounds calculation (exact Excel formula)
    pounds = int((top / 7.75) * 100) / 100

    # Corrected Density calculation (exact Excel formula provided clearly)
    density = int((top / down) * 100) / 100

    # Karat calculation (exact Excel formula provided)
    if density != 0:
        karat_calc = (density - 10.51) * 52.838 / density
        karat = int(karat_calc * 100) / 100
        karat = min(karat, 23)  # Ensures Karat NEVER exceeds 23 clearly
    else:
        karat = 0

    # Display intermediate results clearly
    st.write(f"**Pounds:** {pounds:.2f}")
    st.write(f"**Density:** {density:.2f}")
    st.write(f"**Karat:** {karat:.2f}")

    if price:
        # Amount calculation exactly your Excel formula
        amount_calc = (karat / 23) * price * pounds
        amount = int(amount_calc)  # clearly truncates decimals exactly as Excel

        # Display clearly calculated results
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
