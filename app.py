import streamlit as st

st.title("Movie Recommendation System")
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("Welcome to Streamlit!")

