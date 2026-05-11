import streamlit as st


def main():
    st.set_page_config(page_title="Chat avec mutiple pdf", page_icon=":books:")

    st.header("Chat avec multiple PDFs :books:")
    st.text_input("Poser la question sur vos documents:")

    with st.sidebar:
        st.subheader("Vos documents")
        st.file_uploader("Deposer vos pdfs ici et cliquer sur 'process'")
        st.button("process")


if __name__ == "main":
    main()
