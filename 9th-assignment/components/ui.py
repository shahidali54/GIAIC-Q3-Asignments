import streamlit as st
from .auth import AuthService
from .encryption import EncryptionService
from .database import DatabaseHandler

class UIComponents:
    def __init__(self, auth_service: AuthService, encryption_service: EncryptionService, db_handler: DatabaseHandler):
        self.auth_service = auth_service
        self.encryption_service = encryption_service
        self.db_handler = db_handler

    def render_auth_page(self):
        st.title("🔐 Secure Data App")
        
        tab1, tab2 = st.tabs(["Login", "Sign Up"])
        
        with tab1:
            st.subheader("Login to Your Account")
            email = st.text_input("Email:", key="login_email")
            password = st.text_input("Password:", type="password", key="login_pass")
            
            if st.button("Login", key="login_btn"):
                if self.auth_service.login(email, password):
                    st.session_state.current_page = "home"
                    st.rerun()
        
        with tab2:
            st.subheader("Create New Account")
            new_email = st.text_input("Email:", key="signup_email")
            new_password = st.text_input("Password:", type="password", key="signup_pass1")
            confirm_password = st.text_input("Confirm Password:", type="password", key="signup_pass2")
            
            if st.button("Sign Up", key="signup_btn"):
                if new_password == confirm_password:
                    if self.auth_service.signup(new_email, new_password):
                        st.session_state.current_page = "auth"
                else:
                    st.error("Passwords do not match!")

    def render_home(self):
        st.title(f"🛡️ Welcome, Secure Your Data {st.session_state.user['email']}")
        st.write("---")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📥 Store Data"):
                st.session_state.current_page = "store"
                st.rerun()
        
        with col2:
            if st.button("📤 Retrieve Data"):
                st.session_state.current_page = "retrieve"
                st.rerun()
        
        with col3:
            if st.button("💳 Make Payment"):
                st.session_state.current_page = "payment"
                st.rerun()
        
        if st.button("🚪 Logout", type="primary"):
            self.auth_service.logout()
            st.rerun()

    def render_store_data(self):
        st.title("📥 Store Encrypted Data")
        st.write("---")
        
        user_data = st.text_area("Enter your secret data:")
        passkey = st.text_input("Set a passkey:", type="password")
        
        if st.button("🔒 Encrypt & Save"):
            if user_data and passkey:
                # Debug information
                st.write("Debug Information:")
                user_id = self.auth_service.get_user_id()
                st.write(f"User ID: {user_id}")
                
                encrypted = self.encryption_service.encrypt_data(user_data)
                hashed = self.auth_service.hash_passkey(passkey)
                
                st.write(f"Encrypted Text Length: {len(encrypted)}")
                st.write(f"Hashed Passkey Length: {len(hashed)}")
                
                if user_id:
                    try:
                        success = self.db_handler.store_encrypted_data(user_id, encrypted, hashed)
                        if success:
                            st.success("✅ Data encrypted and saved securely!")
                            st.text_area("Encrypted Text (save this to retrieve later):", 
                                       value=encrypted, height=100)
                        else:
                            st.error("Failed to save to database. Please check your connection.")
                    except Exception as e:
                        st.error(f"Error saving data: {str(e)}")
                else:
                    st.error("No user ID found. Please login again.")
            else:
                st.error("Please provide both data and passkey")
        
        if st.button("⬅️ Back to Home"):
            st.session_state.current_page = "home"
            st.rerun()

    def render_retrieve_data(self):
        st.title("📤 Retrieve Encrypted Data")
        st.write("---")
        
        encrypted_text = st.text_area("Enter encrypted text:")
        passkey = st.text_input("Enter passkey:", type="password")
        
        if st.button("🔓 Decrypt"):
            if encrypted_text and passkey:
                user_id = self.auth_service.get_user_id()
                hashed_passkey = self.auth_service.hash_passkey(passkey)
                
                # Get all encrypted data for the user
                stored_data_list = self.db_handler.get_encrypted_data(user_id)
                # Find the matching encrypted text
                stored_data = next((data for data in stored_data_list if data["encrypted_text"] == encrypted_text), None)
                
                if stored_data and stored_data["passKey_hash"] == hashed_passkey:
                    try:
                        decrypted = self.encryption_service.decrypt_data(encrypted_text)
                        st.success("✅ Data decrypted successfully!")
                        st.text_area("Decrypted Data:", value=decrypted, height=100)
                    except Exception as e:
                        st.error("Failed to decrypt data. Invalid passkey or corrupted data.")
                else:
                    st.error("Invalid passkey or data not found")
            else:
                st.error("Please provide both encrypted text and passkey")
        
        if st.button("⬅️ Back to Home"):
            st.session_state.current_page = "home"
            st.rerun()

    def render_payment(self):
        st.title("💳 Make a Payment")
        st.write("---")
        
        amount = st.number_input("Amount:", min_value=0.0, step=0.01)
        description = st.text_input("Description:")
        
        if st.button("💸 Process Payment"):
            if amount > 0 and description:
                user_id = self.auth_service.get_user_id()
                if self.db_handler.create_payment_record(user_id, amount, description):
                    st.success("✅ Payment processed successfully!")
                else:
                    st.error("Failed to process payment")
            else:
                st.error("Please provide valid amount and description")
        
        if st.button("⬅️ Back to Home"):
            st.session_state.current_page = "home"
            st.rerun()

