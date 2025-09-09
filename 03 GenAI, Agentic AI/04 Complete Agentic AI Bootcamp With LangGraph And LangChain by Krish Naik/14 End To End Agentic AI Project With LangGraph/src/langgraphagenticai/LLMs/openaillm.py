import os
import streamlit as st
from langchain_openai import ChatOpenAI

class OpenAILLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input
        
    def get_llm_model(self):
        try:
            # Get API key from user input or environment
            openai_api_key = self.user_controls_input.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
            selected_openai_model = self.user_controls_input.get("selected_openai_model", "gpt-4o-mini")  # fallback model

            # Validate API key
            if not openai_api_key:
                st.error("Please enter your OpenAI API key to proceed.")
                return None  # stop execution if no key

            # Initialize LLM
            llm = ChatOpenAI(
                api_key= openai_api_key,
                model= selected_openai_model
            )

            return llm

        except Exception as e:
            raise ValueError(f"Error initializing OpenAI LLM: {e}")
