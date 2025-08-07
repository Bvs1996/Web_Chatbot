import streamlit as st
st.title("Ben chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input("Ask Ben anything!"):
    st.session_state.messages.append({"role": "user","content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    if "hi" in prompt.lower():
        response = "Hello"
    elif "how are you" in prompt.lower():
        response = "Iam fine, what about you"
    elif "help me" in prompt.lower():
        response = "Yes, Tell me how can I help you"
    elif "support number" in prompt.lower():
        response = "contact support team 987654321"

    else:
        response = "I cant understand what you are asking about: Can you provide more details? or contact support"

    # Dispaly assistant response      
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history    
    st.session_state.messages.append({"role": "assistant", "content": response}) 


