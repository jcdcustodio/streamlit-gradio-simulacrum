import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Morgage Payment Calculator")

# Input section; Split page into two columns
st.write("### Input Data")
col1, col2 = st.columns(2)
property_value = col1.number_input("Property Value", min_value=1, value=1)
deposit = col1.number_input("Deposit", min_value=0, value=0)
interest_rate = col2.number_input("Interest Rate (%)", min_value=0.0, value=6.0)
loan_term = col2.number_input("Loan Term (years)", min_value=1, max_value=30, value=1)

loan_amount = property_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12
monthly_payment = (
    loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)

# Display repayments; New section with 3 columns
total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

st.write("### Repayments")
col1, col2, col3 = st.columns(3)
col1.metric(label="Monthly Repayments", value=f"PHP {monthly_payment:,.2f}")
col2.metric(label="Total Repayments", value=f"PHP {total_payments:,.0f}")
col3.metric(label="Total Interest", value=f"PHP {monthly_payment:,.0f}")

# Create dataframe with payment schedule
schedule = []
remaining_balance = loan_amount

for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)
    schedule.append(
        [
            i,
            monthly_payment,
            principal_payment,
            interest_payment,
            remaining_balance,
            year
        ]
    )

df = pd.DataFrame(
    schedule, columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"]
)

# Display dataframe as chart
st.write("### Payment Schedule")
payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
st.line_chart(payments_df)