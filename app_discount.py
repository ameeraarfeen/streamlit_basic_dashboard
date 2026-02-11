import streamlit as st 
discounted_price=0

price = st.number_input("Original Price: ", min_value=0, max_value=100)
discount= st.slider("Select discount percentage: ", 0, 50)

if st.button("Final Price"):
    discounted_price = price * (1 - discount / 100)
    st.success(f"Final Price: ₹ {discounted_price:.2f}")

    st.table({
        "Original Price": [f"₹ {price:.2f}"],
        "Discount (%)": [f"{discount}%"],
        "Final Price": [f"₹ {discounted_price:.2f}"],
        
    })
