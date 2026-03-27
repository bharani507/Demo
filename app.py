import streamlit as st

# Title
st.title("🚀 My First Streamlit App")

# Description
st.write("This is a simple sample app for deployment.")

# User input
name = st.text_input("Enter your name:")

# Slider input
age = st.slider("Select your age:", 1, 100, 25)

# Button action
if st.button("Submit"):
    if name:
        st.success(f"Hello {name}! 👋")
        st.write(f"You are {age} years old.")
    else:
        st.warning("Please enter your name!")

# Checkbox example
if st.checkbox("Show more info"):
    st.info("Streamlit makes it easy to build web apps with Python!")

# File uploader
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file:
    st.write("File uploaded successfully!")