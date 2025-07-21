import streamlit as st
from datetime import datetime

st.title("Ghana Gold Invoicing")

# Invoice Details
invoice_number = st.text_input("Invoice Number:")

# Display current date and time
invoice_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
st.write(f"**Invoice Date & Time:** {invoice_date}")

# Seller and Buyer Information
st.subheader("Seller Information")
seller_name = st.text_input("Seller Name:")
seller_address = st.text_area("Seller Address:")
seller_contact = st.text_input("Seller Contact:")

st.subheader("Buyer Information")
buyer_name = st.text_input("Buyer Name:")
buyer_address = st.text_area("Buyer Address:")
buyer_contact = st.text_input("Buyer Contact:")

# Gold Pricing Inputs
top = st.number_input("Top:", value=None, step=0.01)
down = st.number_input("Down:", value=None, step=0.01)
price = st.number_input("Price:", value=None, step=0.01)
pounds = st.number_input("Pounds:", value=None, step=0.01)
density = st.number_input("Density:", value=None, step=0.01)
karat = st.number_input("Karat:", value=None, step=0.01)

# Calculation
if all([invoice_number, seller_name, buyer_name, top, down, price, pounds, density, karat]):
    amount = pounds * price

    # Display Invoice
    st.subheader("Invoice Summary")
    st.write("---")
    st.write(f"**Invoice Number:** {invoice_number}")
    st.write(f"**Invoice Date & Time:** {invoice_date}")

    st.write("**Seller Information**")
    st.write(f"Name: {seller_name}")
    st.write(f"Address: {seller_address}")
    st.write(f"Contact: {seller_contact}")

    st.write("**Buyer Information**")
    st.write(f"Name: {buyer_name}")
    st.write(f"Address: {buyer_address}")
    st.write(f"Contact: {buyer_contact}")

    st.write("**Transaction Details**")
    st.write(f"Top: {top}")
    st.write(f"Down: {down}")
    st.write(f"Price: {price}")
    st.write(f"Pounds: {pounds}")
    st.write(f"Density: {density}")
    st.write(f"Karat: {karat}")

    st.write("---")
    st.write(f"### Total Amount (GHC): {amount:,.2f}")
else:
    st.warning("Please enter all required fields to generate the invoice.")
