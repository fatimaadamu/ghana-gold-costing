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

# Automatically calculated values
if top:
    pounds = top / 7.75
    density = pounds / 20.81
    karat = density / 0.82

    st.write(f"**Pounds:** {pounds:.2f}")
    st.write(f"**Density:** {density:.2f}")
    st.write(f"**Karat:** {karat:.2f}")

    # Final Calculation
    if price:
        amount = pounds * price

        # Display Results
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
    st.warning("Please enter the Top value to calculate Pounds, Density, and Karat.")
