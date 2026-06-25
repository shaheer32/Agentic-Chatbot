import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY", "").strip()
            selected_groq_model = self.user_controls_input.get("selected_groq_model", "")

            # Fallback to environment variable if not provided in UI
            if not groq_api_key:
                groq_api_key = os.environ.get("GROQ_API_KEY", "")  # ✅ .get() never throws KeyError

            if not groq_api_key:
                st.error("Please enter the Groq API key in the sidebar.")
                return None

            if not selected_groq_model:
                st.error("Please select a Groq model in the sidebar.")
                return None

            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
            return llm

        except Exception as e:
            raise ValueError(f"Error occurred with Exception: {e}")