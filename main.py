from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# load env variables
load_dotenv()

#streamlit page setup
st.set_page_config(
    page_title="GroQ API",
    layout="centered",
    page_icon="🤖",
)
st.title("Generative AI ChatBot")

#initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#initiate llm
llm=ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.0,
)

#input box
user_prompt = st.chat_input("Ask Chatbot")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})

    response = llm.invoke(
        input=[{"role":"system","content":"you are helpful assistant"},*st.session_state.chat_history]
    )
    assistant_response= response.content
    st.session_state.chat_history.append({"role":"assistant","content":"assistant response"})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)