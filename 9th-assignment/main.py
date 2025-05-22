import streamlit as st
import sqlite3
import bcrypt
import jwt
import datetime
from cryptography.fernet import Fernet
import stripe

# -------------------- Database Setup --------------------
def init_db():
    conn = sqlite3.connect('secure_app.db')
    cursor = conn.cursor()

    # Users Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT UNIQUE,
            is_premium BOOLEAN DEFAULT FALSE
        )
    ''')

    # Encrypted Data Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS encrypted_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            encrypted_text TEXT NOT NULL,
            passkey_hash TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    conn.commit()
    conn.close()

# -------------------- Stripe Payment Check via URL --------------------
query_params = st.query_params
if 'payment_success' in query_params and 'user_id' in query_params:
    user_id = query_params['user_id'][0]

    conn = sqlite3.connect('secure_app.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET is_premium=1 WHERE username=?", (user_id,))
    conn.commit()
    conn.close()

    st.success("🎉 Payment successful! You are now a premium user.")
    st.query_params.clear()

# -------------------- JWT Authentication --------------------
SECRET_KEY = st.secrets["general"]["jwt_secret"]  

def create_jwt_token(username):
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["username"]
    except:
        return None

# -------------------- Password Hashing --------------------
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(input_password, hashed_password):
    return bcrypt.checkpw(input_password.encode(), hashed_password.encode())

# -------------------- Encryption Class --------------------
class EncryptionManager:
    def __init__(self):
        if 'KEY' not in st.session_state:
            st.session_state.KEY = Fernet.generate_key()
        self.cipher = Fernet(st.session_state.KEY)

    def encrypt(self, text):
        return self.cipher.encrypt(text.encode()).decode()

    def decrypt(self, encrypted_text):
        return self.cipher.decrypt(encrypted_text.encode()).decode()

# -------------------- Stripe Setup --------------------
stripe.api_key = st.secrets["stripe"]["api_key"]  

def create_checkout_session(user_id):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': st.secrets["stripe"]["price_id"], 
            'quantity': 1,
        }],
        mode='subscription',
        success_url=f"http://localhost:8501/?payment_success=true&user_id={user_id}",
        cancel_url="http://localhost:8501/?payment_cancelled=true",
    )
    return session.url

# -------------------- Streamlit App --------------------
def main():
    st.title("🔐 Premium Secure Vault")

    if 'user_token' not in st.session_state:
        st.session_state.user_token = None

    current_user = verify_jwt_token(st.session_state.user_token) if st.session_state.user_token else None

    if not current_user:
        tab1, tab2 = st.tabs(["Login", "Signup"])

        with tab1:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
                conn = sqlite3.connect('secure_app.db')
                cursor = conn.cursor()
                cursor.execute("SELECT password_hash FROM users WHERE username=?", (username,))
                result = cursor.fetchone()
                conn.close()

                if result and verify_password(password, result[0]):
                    st.session_state.user_token = create_jwt_token(username)
                    st.success("Logged in successfully!")
                    st.rerun()
                else:
                    st.error("Invalid credentials!")

        with tab2:
            new_username = st.text_input("New Username")
            new_email = st.text_input("Email")
            new_password = st.text_input("New Password", type="password")

            if st.button("Create Account"):
                conn = sqlite3.connect('secure_app.db')
                cursor = conn.cursor()
                try:
                    cursor.execute(
                        "INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)",
                        (new_username, hash_password(new_password), new_email)
                    )
                    conn.commit()
                    st.success("Account created! Please login.")
                except sqlite3.IntegrityError:
                    st.error("Username/Email already exists!")
                finally:
                    conn.close()
    else:
        st.sidebar.success(f"Logged in as: {current_user}")

        conn = sqlite3.connect('secure_app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT is_premium FROM users WHERE username=?", (current_user,))
        is_premium = cursor.fetchone()[0]
        conn.close()

        if not is_premium:
            if st.sidebar.button("🔓 Upgrade to Premium ($5)"):
                payment_url = create_checkout_session(current_user)
                st.write(f"[Click here to pay]({payment_url})")

        menu = ["Store Data", "Retrieve Data"]
        choice = st.sidebar.selectbox("Menu", menu)

        encryptor = EncryptionManager()

        if choice == "Store Data":
            st.subheader("🔒 Store Encrypted Data")
            user_data = st.text_area("Enter your secret data:")
            passkey = st.text_input("Set a passkey:", type="password")

            if st.button("Encrypt & Save"):
                if user_data and passkey:
                    encrypted = encryptor.encrypt(user_data)
                    passkey_hash = hash_password(passkey)

                    conn = sqlite3.connect('secure_app.db')
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO encrypted_data (user_id, encrypted_text, passkey_hash) VALUES ((SELECT id FROM users WHERE username=?), ?, ?)",
                        (current_user, encrypted, passkey_hash)
                    )
                    conn.commit()
                    conn.close()

                    st.success("✅ Data saved securely!")
                    st.code(encrypted)

        elif choice == "Retrieve Data":
            st.subheader("🔍 Retrieve Your Data")
            encrypted_input = st.text_area("Paste Encrypted Text:")
            passkey_input = st.text_input("Enter Passkey:", type="password")

            if st.button("Decrypt"):
                if encrypted_input and passkey_input:
                    conn = sqlite3.connect('secure_app.db')
                    cursor = conn.cursor()
                    cursor.execute(
                        "SELECT passkey_hash FROM encrypted_data WHERE encrypted_text=? AND user_id=(SELECT id FROM users WHERE username=?)",
                        (encrypted_input, current_user)
                    )
                    result = cursor.fetchone()
                    conn.close()

                    if result and verify_password(passkey_input, result[0]):
                        decrypted = encryptor.decrypt(encrypted_input)
                        st.success("✅ Decrypted Data:")
                        st.code(decrypted)
                    else:
                        st.error("❌ Invalid passkey or data not found!")

        if st.sidebar.button("Logout"):
            st.session_state.user_token = None
            st.rerun()

if __name__ == "__main__":
    main()
