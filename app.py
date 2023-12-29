import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from streamlit import logger
from streamlit_chat import message

from components import get_response, side_bar, theme, upload_and_process_document
from docGPT import create_doc_gpt

OPENAI_API_KEY = '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'
model = None

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

st.session_state.openai_api_key = None
st.session_state.g4f_provider = None
st.session_state.button_clicked = None


if 'response' not in st.session_state:
    st.session_state['response'] = []

if 'query' not in st.session_state:
    st.session_state['query'] = []

app_logger = logger.get_logger(__name__)


def main():
    global model
    theme()
    #side_bar()

    doc_container = st.container()
    with doc_container:
        docs = upload_and_process_document()

        if docs:
            model = create_doc_gpt(docs)
            app_logger.info(f'{__file__}: Created model: {model}')
            del docs
        st.write('---')

    user_container = st.container()
    response_container = st.container()
    with user_container:
        query = st.text_input(
            "#### 提问:",
            placeholder='在此输入问题'
        )

        if model and query and query != '' and not st.session_state.button_clicked:
            response = get_response(query, model)
            st.session_state.query.append(query)
            st.session_state.response.append(response) 

    with response_container:
        if st.session_state['response']:
            for i in range(len(st.session_state['response'])-1, -1, -1):
                message(
                    st.session_state["response"][i], key=str(i),
                    #logo=('./static/img/logo.png')
                )
                message(
                    st.session_state['query'][i], is_user=True, key=str(i) + '_user'
                    #logo=('https://api.dicebear.com/6.x/adventurer/svg?hair=short16&hairColor=85c2c6&eyes=variant12&size=100&mouth=variant26&skinColor=f2d3b1')
                )


if __name__ == "__main__":
    main()


'''
Copyright (c) 2023 JunXiang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''