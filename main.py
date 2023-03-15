import bcrypt
import cryptography
import sqlite3
"""
Password Manager with encryption - Build a password manager application with Python using encryption libraries like cryptography. The application should allow users to create, store, and manage strong passwords for their accounts. The application should also encrypt the stored passwords to protect them from unauthorized access.
        ◦ To set up the project, you can start with installing Python and the cryptography package using pip. You can then use a simple text editor like Notepad or Sublime Text to create the Python script for the application.
"""
    
con = sqlite3.connect("./data.db")
cur = con.cursor()

def gen_key():
    key = cryptography.Fernet.generate_key()

def load_key(user: str) -> str:
    return cur.execute(f"SELECT key FROM users where {user} == username")