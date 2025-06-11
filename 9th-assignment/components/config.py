import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class SupabaseConfig:
    def __init__(self):
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        self.tables = {
            "users": "users",
            "encrypted_data": "encrypted_data",
            "payments": "payments"
        }

