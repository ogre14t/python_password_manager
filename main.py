import bcrypt
import cryptography
import sqlite3
import os
"""
Password Manager with encryption - A password manager application with Python using encryption libraries like cryptography. The application should allow users to create, store, and manage strong passwords for their accounts. The application should also encrypt the stored passwords to protect them from unauthorized access.
"""

def main():
    con = sqlite3.connect("./data.db")
    cur = con.cursor()

    if os.path.getsize('./data.db') < 100:
        cur.execute("CREATE TABLE users(username, pass_hash, key)")
        cur.execute("CREATE TABLE passwords(username, site_username, pass, site)")

def gen_key():
    key = cryptography.Fernet.generate_key()

def load_key(cur: sqlite3.Cursor, user: str) -> str:
    return cur.execute(f"SELECT key FROM users where {user} = username")

def encrypt_pass(password: str, key: cryptography.Fernet.key) -> str:
    fern = cryptography.Fernet(key)
    encrypted_pass = fern.encrypt(password)
    return encrypted_pass

def decrypt_pass(user: str, password: str) -> str:
    key = load_key(user)
    fern = cryptography.Fernet(key)
    decrypted_pass = fern.decrypt(password)
    return decrypted_pass

def create_user(username: str, password: str, cur: sqlite3.Cursor):
    gensalt = bcrypt.gensalt()
    hash_pass = bcrypt.hashpw(password, gensalt)
    new_key = gen_key()
    cur.execute(f"INSERT INTO users VALUES({username}, {hash_pass}, {new_key})")

def add_site(username: str, password: str, site: str, cur: sqlite3.Cursor):
    cur.execute(f"INSERT INTO passwords VALUES({username}, {password}, {site})")

if __name__ == "__main__": main()