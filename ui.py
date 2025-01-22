import streamlit as st
from chatbot import process_legal_query

st.set_page_config(page_title="LegalBot", page_icon="⚖️")

st.title("⚖️ LegalBot - AI Legal Assistant")
st.write("Ask me about any legal topic, law, or regulation from around the world.")

# Chat section
user_query = st.text_input("Enter your legal question:")

if user_query:
    with st.spinner("Loading information..."):
        response = process_legal_query(user_query)
        st.write("**LegalBot:**", response)
