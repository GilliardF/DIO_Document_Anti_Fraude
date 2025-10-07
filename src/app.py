import streamlit as st


def configurete_interface():
    st.title("Upload de Arquivo DIO - Desafio 1 - Azure - Fake Docs")
    uploaded_file=st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if __name__ == "__main__":
        configure_interface()