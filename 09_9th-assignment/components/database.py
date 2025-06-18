from supabase import create_client, Client
from datetime import datetime
from typing import Dict, Optional, List, Tuple
from uuid import UUID
from .config import SupabaseConfig

class DatabaseHandler:
    def __init__(self, config: SupabaseConfig):
        self.config = config
        try:
            self.client: Client = create_client(config.url, config.key)
            # Test connection with a simple query
            self.client.table("encrypted_data").select("id").limit(1).execute()
            print("✅ Successfully connected to Supabase")
        except Exception as e:
            print("❌ Failed to connect to Supabase:")
            print(f"URL: {config.url}")
            print(f"Error: {str(e)}")
            raise e
    
    def authenticate_user(self, email: str, password: str) -> Tuple[bool, str]:
        try:
            response = self.client.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            return True, response.session.access_token
        except Exception as e:
            print("Login Error:", str(e))
            return False, str(e)
    
    def signup_user(self, email: str, password: str) -> Tuple[bool, str]:
        try:
            response = self.client.auth.sign_up({
                "email": email,
                "password": password
            })
            return True, "Signup successful! Please login."
        except Exception as e:
            print("Signup Error:", str(e))
            return False, str(e)
    
    def store_encrypted_data(self, user_id: str, encrypted_text: str, hashed_passkey: str) -> bool:
        try:
            # Validate UUID format
            try:
                UUID(user_id)
            except ValueError as e:
                print(f"Invalid UUID format: {e}")
                return False
            
            data = {
                "user_id": user_id,
                "encrypted_text": encrypted_text,
                "passKey_hash": hashed_passkey  # Corrected to match table column name
            }
            
            # Debug print
            print("\n=== Attempting to store data ===")
            print(f"User ID: {user_id}")
            print(f"Encrypted Text Length: {len(encrypted_text)}")
            print(f"Passkey Hash Length: {len(hashed_passkey)}")
            
            # Insert data
            response = self.client.table("encrypted_data").insert(data).execute()
            
            # Check if insert was successful
            if hasattr(response, 'data'):
                print("✅ Data stored successfully")
                return True
            return False
            
        except Exception as e:
            print("\n❌ Error storing data:")
            print(f"Error Type: {type(e).__name__}")
            print(f"Error Message: {str(e)}")
            
            # Check for common Supabase errors
            if "Row Level Security" in str(e):
                print("\n🔐 RLS Error: Check your Row Level Security policies")
                print("Suggested fix: Create an insert policy for authenticated users")
            
            return False
    
    def get_encrypted_data(self, user_id: str) -> List[Dict]:
        try:
            response = self.client.table("encrypted_data")\
                .select("*")\
                .eq("user_id", user_id)\
                .execute()
            return response.data if response.data else []
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return []
    
    def get_single_encrypted_data(self, user_id: str, data_id: int) -> Optional[Dict]:
        try:
            response = self.client.table("encrypted_data")\
                .select("*")\
                .eq("user_id", user_id)\
                .eq("id", data_id)\
                .single()\
                .execute()
            return response.data
        except Exception as e:
            print(f"Error retrieving single record: {e}")
            return None
    
    def create_payment_record(self, user_id: str, amount: float, description: str) -> bool:
        try:
            data = {
                "user_id": user_id,
                "amount": amount,
                "description": description,
                "payment_date": str(datetime.now()),
                "status": "pending"
            }
            self.client.table("payments").insert(data).execute()
            return True
        except Exception as e:
            print(f"Error creating payment: {e}")
            return False 