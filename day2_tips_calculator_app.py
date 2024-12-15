import streamlit as st
from day2_tips_calculator import calculate_bill_per_person
from footer_utils import load_footer

# Streamlit App
st.title("💰 Tip Calculator")
st.write("Calculate your tip and split the bill hassle-free. 😎")

# Inputs
st.subheader("📝 Enter details:")
bill = st.number_input("What was the total bill?", min_value=100.00, step=0.01)
tips_percentage = st.selectbox("How much tip would you like to give?", options=[10, 12, 15])
pax_count = st.number_input("How many people to split the bill?", min_value=2)

# Calculate button
if st.button("Calculate"):
    if bill > 0 and pax_count > 0:
        final_bill, tips_amount, payable_per_pax = calculate_bill_per_person(bill, tips_percentage, pax_count)

        st.success(f"💸 Each person should pay: **${payable_per_pax:.2f}**")

        # Display breakdown using st.write
        st.info(
            f"""
             ℹ️ Total Bill Breakdown"
            | **Description**         | **Amount**        |
            |------------------------ |------------------ |
            | Original Bill           | ${bill:.2f}       |
            | Tip ({tips_percentage}%)| ${tips_amount:.2f}|
            | Final Bill              | ${final_bill:.2f} |
            """
        )

    else:
        st.error("Please make sure the bill amount and number of people are positive.")

# Display the footer with the dynamic day number
footer_html = load_footer(2)
st.markdown(footer_html, unsafe_allow_html=True)
