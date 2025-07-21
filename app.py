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
    # Correct Pounds calculation
    pounds = int((top / 7.75) * 100) / 100  # clearly truncating to 2 decimals

    # Correct Density calculation
    density = int((top / down) * 100) / 100  # clearly truncating to 2 decimals

    # Correct Karat calculation (exactly as your Excel formula)
    karat_calc = (density - 10.51) * 52.838 / density
    karat = int(karat_calc * 100) / 100  # clearly truncating to 2 decimals

    # Display corrected intermediate values
    st.write(f"**Pounds:** {pounds:.2f}")
    st.write(f"**Density:** {density:.2f}")
    st.write(f"**Karat:** {karat:.2f}")

    if price:
        # Correct Amount calculation (exact Excel formula)
        amount_calc = (karat / 23) * price * pounds
        amount = int(amount_calc)  # clearly truncating decimals exactly like Excel
        
        # Display final corrected results clearly
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
