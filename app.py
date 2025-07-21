import streamlit as st
from datetime import datetime

st.title("Ghana Gold Value Determination")

# Current date & time
now = datetime.now()
st.write(f"**Date & Time:** {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Inputs clearly left empty for user entry
top = st.number_input("Top:", value=None, step=0.01)
down = st.number_input("Down:", value=None, step=0.01)
price = st.number_input("Price:", value=None, step=0.01)

if top and down:
    pounds = int((top / 7.75) * 100) / 100  # TRUNCATE to 2 decimal places
    density = int((top / down) * 100) / 100  # TRUNCATE to 2 decimal places
    karat = int(((density - 10.51) * 52.838 / density) * 100) / 100  # TRUNCATE to 2 decimal places

    st.write(f"**Pounds:** {pounds:.2f}")
    st.write(f"**Density:** {density:.2f}")
    st.write(f"**Karat:** {karat:.2f}")

    if price:
        amount = int((karat / 23) * price * pounds)  # TRUNCATE to 0 decimal places clearly as in Excel
        
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
