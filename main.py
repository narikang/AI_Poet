# from dotenv import load_dotenv
# load_dotenv()

from langchain.chat_models import ChatOpenAI
import streamlit as st
chat_model = ChatOpenAI()

st.title("Artificial Intelligence Poet")
content = st.text_input("Please specify the subject of the poet you're interested in")

if st.button("Request to write a poem"):
    with st.spinner("I am writing now.."):
        st.write(chat_model.predict("write a poem about" + content))