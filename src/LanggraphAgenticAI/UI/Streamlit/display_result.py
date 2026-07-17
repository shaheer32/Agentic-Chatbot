import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage


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
                    messages = value.get("messages")

                    if isinstance(messages, list):
                        ai_message = messages[-1]
                    else:
                        ai_message = messages

                    if isinstance(ai_message, AIMessage):
                        with st.chat_message("assistant"):
                            st.write(ai_message.content)
                    elif isinstance(ai_message, str):
                        with st.chat_message("assistant"):
                            st.write(ai_message)

        elif self.usecase == "Chatbot With Web Search":
            initial_state = {"messages": [self.user_message]}
            res = self.graph.invoke(initial_state)

            for message in res["messages"]:
                if isinstance(message, HumanMessage):
                    with st.chat_message("user"):
                        st.write(message.content)
                elif isinstance(message, ToolMessage):
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")
                elif isinstance(message, AIMessage) and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)
