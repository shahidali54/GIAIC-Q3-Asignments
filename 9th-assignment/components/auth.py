import streamlit as st
import hashlib
from typing import Optional
from .database import DatabaseHandler

class AuthService:
    def __init__(self, db_handler: DatabaseHandler):
        self.db_handler = db_handler
        if 'user' not in st.session_state:
            st.session_state.user = None
        if 'failed_attempts' not in st.session_state:
            st.session_state.failed_attempts = 0
    
    def hash_passkey(self, passkey: str) -> str:
        return hashlib.sha256(passkey.encode()).hexdigest()
    
    def login(self, email: str, password: str) -> bool:
        success, token_or_error = self.db_handler.authenticate_user(email, password)
        if success:
            user = self.db_handler.client.auth.get_user(token_or_error)
            if not user.user:
                st.error("Failed to get user ID")
                return False
                
            st.session_state.user = {
                "email": email,
                "token": token_or_error,
                "id": str(user.user.id)
            }
            st.session_state.failed_attempts = 0
            return True
        else:
            st.error(f"Login failed: {token_or_error}")
            return False
    
    def signup(self, email: str, password: str) -> bool:
        success, message = self.db_handler.signup_user(email, password)
        if success:
            st.success(message)
            return True
        else:
            st.error(f"Signup failed: {message}")
            return False
    
    def is_authenticated(self) -> bool:
        return st.session_state.user is not None
    
    def get_user_id(self) -> Optional[str]:
        return st.session_state.user.get("id") if self.is_authenticated() else None
    
    def logout(self):
        st.session_state.user = None
        st.session_state.current_page = "auth"
        