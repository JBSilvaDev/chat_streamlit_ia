import streamlit as st
from app.chatbot import ChatBot

class ChatInterface:
    def __init__(self, chatbot: ChatBot):
        self.chatbot = chatbot
        if "lista_mensagens" not in st.session_state:
            st.session_state["lista_mensagens"] = []

    def display_messages(self):
        """Exibe todas as mensagens do histórico na interface do Streamlit."""
        for mensagem in st.session_state["lista_mensagens"]:
            role = mensagem["role"]
            content = mensagem["content"]
            st.chat_message(role).write(content)

    def handle_user_input(self):
        """Processa a entrada do usuário e obtém a resposta do chatbot."""
        mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

        if mensagem_usuario:
            st.chat_message("user").write(mensagem_usuario)
            mensagem_user_dict = {"role": "user", "content": mensagem_usuario}
            st.session_state["lista_mensagens"].append(mensagem_user_dict)

            with st.spinner("Pensando..."):
                resposta_ia = self.chatbot.get_response(st.session_state["lista_mensagens"])

            st.chat_message("assistant").write(resposta_ia)
            mensagem_ia_dict = {"role": "assistant", "content": resposta_ia}
            st.session_state["lista_mensagens"].append(mensagem_ia_dict)

    def run(self):
        """Executa a interface principal do chat."""
        st.write("### ChatBot com IA")
        self.display_messages()
        self.handle_user_input()