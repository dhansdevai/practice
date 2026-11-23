import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv(Path(__file__).resolve().parent.parent / "4_call_llm" / ".env")
load_dotenv()

st.set_page_config(page_title="Movie Buddy", page_icon="🎬")

st.title("🎬 Movie Recommendation Buddy")
st.caption("Tell me what you like, and I'll remember it while we chat.")

if not os.getenv("OPENAI_API_KEY"):
    st.error("Set OPENAI_API_KEY in your environment or in 4_call_llm/.env to start chatting.")
    st.stop()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
system_prompt = (
    "You are a witty, friendly movie buff who loves making light puns. "
    "Remember the user's movie tastes from the conversation and use them for "
    "personalized recommendations. Respect dislikes and avoid recommending "
    "genres the user says they cannot stand. Explain briefly why each movie "
    "fits, avoid spoilers, and answer follow-up questions using the chat history."
)

if "conversation" not in st.session_state:
    st.session_state.conversation = []

with st.sidebar:
    st.subheader("Your movie buddy")
    st.write("Share your favorite genres, movies, or anything you'd rather avoid.")
    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.conversation = []
        st.rerun()

for message in st.session_state.conversation:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("What kind of movie are you in the mood for?")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    messages = [SystemMessage(content=system_prompt)]
    for message in st.session_state.conversation:
        if message["role"] == "user":
            messages.append(HumanMessage(content=message["content"]))
        else:
            messages.append(AIMessage(content=message["content"]))
    messages.append(HumanMessage(content=user_input))

    try:
        with st.spinner("Finding a movie that fits..."):
            response = model.invoke(messages)
    except Exception as error:
        st.error(f"Sorry, I couldn't get a recommendation right now: {error}")
    else:
        reply = response.content
        st.session_state.conversation.extend(
            [
                {"role": "user", "content": user_input},
                {"role": "assistant", "content": reply},
            ]
        )
        with st.chat_message("assistant"):
            st.markdown(reply)
