import streamlit as st

from backend.chatbot import LLMChatbot


st.set_page_config(page_title="Deployment Test Chatbot", page_icon=":speech_balloon:")

st.title("Deployment Test Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chatbot" not in st.session_state:
    try:
        st.session_state.chatbot = LLMChatbot()
        st.session_state.startup_error = None
    except Exception as exc:
        st.session_state.chatbot = None
        st.session_state.startup_error = str(exc)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.startup_error:
    st.error(st.session_state.startup_error)
else:
    prompt = st.chat_input("Ask something")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = st.session_state.chatbot.get_response(prompt)
                st.markdown(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})
