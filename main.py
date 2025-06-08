import streamlit as st
from app.interface import ChatInterface
from app.chatbot import ChatBot

def main():
    chatbot_instance = ChatBot()

    chat_interface = ChatInterface(chatbot_instance)

    chat_interface.run()

if __name__ == "__main__":
    main()