import streamlit as st
st.title("🤖 Welcome AI Chatbot")
prompt = st.text_input("Enter your prompt:")
if st.button("Send"):
    if prompt:
        st.success("Success! " + prompt)
    else:
        st.warning("Please enter a prompt!")