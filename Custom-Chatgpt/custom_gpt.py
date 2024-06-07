from langchain_community.chat_models import ChatOpenAI
from langchain.schema import(
    SystemMessage,
    HumanMessage,
    AIMessage
)
import streamlit as st
from streamlit_chat import message

import os
from apikey4 import apikey

os.environ["OPENAI_API_KEY"] = apikey

st.set_page_config(
    page_title="You Custom Assistant",
    page_icon="🗣️"
)

st.subheader('Your custom chatgpt 🗣️')

chat = ChatOpenAI(model_name='gpt-4-turbo', temperature=0.9)

if 'messages' not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    system_message = st.text_input(label='System role')
    user_prompt = st.text_input(label='send a message')
    if system_message:
        if not any(isinstance(x, SystemMessage) for x in st.session_state.messages):
            st.session_state.messages.append(
                SystemMessage(content=system_message)
                )
            
    # st.write(st.session_state.messages)

    if user_prompt:
        st.session_state.messages.append(
            HumanMessage(content=user_prompt)
        )

        with st.spinner('Working on you request....'):
            response = chat(st.session_state.messages)

        st.session_state.messages.append(AIMessage(content=response.content))

if len(st.session_state.messages) >= 1:
    if not isinstance(st.session_state.messages[0],SystemMessage):
        st.session_state.messages.insert(0, SystemMessage(content='You are helpful assistent.'))


for i,msg in enumerate(st.session_state.messages[1:]):
    if i % 2 == 0:
        message(msg.content, is_user=True, key=f'{i} + 👤')
        
    else:
        message(msg.content, is_user=False, key=f'{i} + 🗣️')



# breakpoint()
# st.session_state.messages

# message('this is chatgpt', is_user=False)
# message('this is user', is_user=True)
