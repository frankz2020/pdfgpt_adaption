import streamlit as st

def side_bar() -> None:
    with st.sidebar:
        # Add a title for the instructions section
        st.markdown("### How to use it")
        
        # Display instructions directly in the sidebar
        st.markdown(
            """
            1. **Upload a Document** file (choose one method):
                * method1: Browse and upload your own document file from your local machine.
                * method2: Enter the document URL link directly.
                
                (**support documents**: `.pdf`, `.docx`, `.csv`, `.txt`)
            2. Start asking questions!
            3. More details. [GitHub Repository](https://github.com/Lin-jun-xiang/docGPT-streamlit)
            4. If you have any questions, feel free to leave comments and engage in discussions. [GitHub Issues](https://github.com/Lin-jun-xiang/docGPT-streamlit/issues)
            """
        )