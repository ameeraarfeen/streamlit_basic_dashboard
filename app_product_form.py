import streamlit as st

st.title("Product Management System")

with st.sidebar:
    st.header("Add Product")

    with st.form("product_form"):
        product_name = st.text_input("Product Name")

        category = st.selectbox(
            "Category",
            ["Electronics", "Clothing", "Books", "Food", "Accessories"]
        )

        price = st.number_input("Price", min_value=0.0)

        submit = st.form_submit_button("Add Product")

if submit:
    st.success("Product Added Successfully!")
    st.write("### Product Details")
    st.write("Name:", product_name)
    st.write("Category:", category)
    st.write("Price: ₹", price)
