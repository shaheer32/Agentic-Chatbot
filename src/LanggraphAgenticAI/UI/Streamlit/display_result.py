import streamlit as st
from langchain_core.messages import AIMessage

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        if self.usecase == "Basic Chatbot":
            with st.chat_message("user"):
                st.write(self.user_message)

            for event in self.graph.stream({'messages': ("user", self.user_message)}):
                for value in event.values():
                    messages = value.get("messages")  # ✅ safely get messages

                    # Handle both list and single AIMessage
                    if isinstance(messages, list):
                        ai_message = messages[-1]      # ✅ last message if list
                    else:
                        ai_message = messages          # ✅ direct AIMessage object

                    # Extract content safely
                    if isinstance(ai_message, AIMessage):
                        with st.chat_message("assistant"):
                            st.write(ai_message.content)
                    elif isinstance(ai_message, str):
                        with st.chat_message("assistant"):
                            st.write(ai_message)