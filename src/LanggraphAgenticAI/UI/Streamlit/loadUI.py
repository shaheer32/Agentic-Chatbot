import streamlit as st
import os

from src.LanggraphAgenticAI.UI.uniconfig import Config


class LoadStremlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="Agentic AI")
        st.header("Agentic AI Assistant")

        if 'timeframe' not in st.session_state:
            st.session_state.timeframe = ''
        if 'topic' not in st.session_state:
            st.session_state.topic = ''
        if 'IsFetchButtonClicked' not in st.session_state:
            st.session_state.IsFetchButtonClicked = False

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)
            if self.user_controls["selected_llm"] == 'Groq':
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input(
                    "API Key", type="password", key="groq_api_key_input"
                )
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please Enter your GROQ API Key to proceed. Don't have? refer: https://console.groq.com/home")

            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if self.user_controls["selected_usecase"] != "AI News":
                st.session_state.IsFetchButtonClicked = False

            if self.user_controls["selected_usecase"] in ("Chatbot With Web Search", "AI News"):
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input(
                    "TAVILY_API Key", type="password", key="tavily_api_key_input"
                )
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter your TAVILY_API_KEY to proceed. Don't have? refer: https://app.tavily.com/home")

            if self.user_controls['selected_usecase'] == "AI News":
                st.subheader("AI News Explorer")

                time_frame = st.selectbox(
                    "Select Time Frame",
                    ["Daily", "Weekly", "Monthly"],
                    index=0,
                    key="time_frame_select"
                )

                topic = st.text_input(
                    "Enter topic/keywords to search",
                    value="Artificial Intelligence (AI) technology news",
                    key="topic_input"
                )

                if st.button("Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame
                    st.session_state.topic = topic

            return self.user_controls
