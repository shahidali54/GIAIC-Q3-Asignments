import streamlit as st
from cryptography.fernet import Fernet

class EncryptionService:
    def __init__(self):
        if 'KEY' not in st.session_state:
            st.session_state.KEY = Fernet.generate_key()
        self.cipher = Fernet(st.session_state.KEY)
    
    def encrypt_data(self, text: str) -> str:
        return self.cipher.encrypt(text.encode()).decode()
    
    def decrypt_data(self, encrypted_text: str) -> str:
        return self.cipher.decrypt(encrypted_text.encode()).decode()

