import streamlit as st
import time
import getpass
import os
from langchain_groq import ChatGroq
st.title("Ask Me Anything")

os.environ["GROQ_API_KEY"]='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'
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
# take input from user
url=st.text_input("How may I help you?",value="  ")
clicked=st.button("Ask")
if (clicked):
    "Generating response for you..."
    response=llm.invoke(url)
    st.write(response.content)
    st.button('Ask Next')
if __name__ == '__main__':
   pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
