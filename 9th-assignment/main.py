
import streamlit as st
from components.config import SupabaseConfig
from components.database import DatabaseHandler
from components.encryption import EncryptionService
from components.auth import AuthService
from components.ui import UIComponents

class SecureDataApp:
    def __init__(self):
        self.config = SupabaseConfig()
        self.db_handler = DatabaseHandler(self.config)
        self.encryption_service = EncryptionService()
        self.auth_service = AuthService(self.db_handler)
        self.ui = UIComponents(self.auth_service, self.encryption_service, self.db_handler)
        
        if 'stored_data' not in st.session_state:
            st.session_state.stored_data = {}
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "auth"
    
    def run(self):
        if not self.auth_service.is_authenticated():
            self.ui.render_auth_page()
        else:
            if st.session_state.current_page == "home":
                self.ui.render_home()
            elif st.session_state.current_page == "store":
                self.ui.render_store_data()
            elif st.session_state.current_page == "retrieve":
                self.ui.render_retrieve_data()
            elif st.session_state.current_page == "payment":
                self.ui.render_payment()

if __name__ == "__main__":
    app = SecureDataApp()
    app.run()

