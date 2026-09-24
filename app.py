import streamlit as st
import ollama
st.title("💻 Welcome to Terminal")
st.write("🤖 Welcome to Terminal! Start chatting with AI.")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user", avatar="👤"):
            st.write("You")
            st.write(message["content"])
    elif message["role"] == "assistant":
        with st.chat_message("assistant", avatar="🤖"):
            st.write("AI")
            st.write(message["content"])
prompt = st.chat_input("Enter your prompt...")
if prompt:
    if prompt.strip().lower() == "exit":
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
        with st.chat_message("user", avatar="👤"):
            st.write("You")
            st.write(prompt)
        with st.chat_message("assistant", avatar="🤖"):
            st.write("AI")
            st.write("Session terminated. 👋")
        st.write("### 📜 User History")
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.write("👤 You:", message["content"])
        st.stop()
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    with st.chat_message("user", avatar="👤"):
        st.write("You")
        st.write(prompt)
    with st.chat_message("assistant", avatar="🤖"):
        st.write("AI")
        try:
            with st.spinner("Loading..."):
                response = ollama.chat(
                    model="llama3.2",
                    messages=st.session_state.messages
                )
            answer = response["message"]["content"]
            st.write(answer)
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })
        except Exception as e:
            st.error("Unable to connect to Ollama.")
            st.code(str(e))