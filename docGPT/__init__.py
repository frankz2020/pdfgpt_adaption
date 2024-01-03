import os

import openai
import streamlit as st
from langchain.chat_models import ChatOpenAI
from streamlit import logger

from .agent import AgentHelper
from .check_api_key import OpenAiAPI, SerpAPI
from .docGPT import DocGPT

# Set a default OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')
module_logger = logger.get_logger(__name__)


@st.cache_resource(ttl=1200, max_entries=3)
def create_doc_gpt(_docs: list) -> DocGPT:
    docGPT = DocGPT(docs=_docs)

    try:
        # Initialize the OpenAI GPT-3.5 Turbo model
        llm_model = ChatOpenAI(
            temperature=0.2,
            max_tokens=200,
            model_name='gpt-3.5-turbo'
        )
        docGPT.llm = llm_model

        # Create a QA chain and return the DocGPT object
        docGPT.create_qa_chain(chain_type='refine', verbose=False)
        return docGPT

    except Exception as e:
        print(e)
        module_logger.info(f'{__file__}: {e}')
