import hashlib
import csv
from csv_handler import CSVHandler

class LoginUser:
    def __init__(self, email, password, role):
        self.email = email
        self.password = self.encrypt_password(password)
        self.role = role

    def encrypt_password(self, password):
        """Encrypt the password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, input_password):
        """Verify the input password against the stored encrypted password"""
        return self.encrypt_password(input_password) == self.password

    @staticmethod
    def register_user(email, password, role, filename="data/login.csv"):
        """Registers a new user by storing an encrypted password"""
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([email, encrypted_password, role])
        print(f"✅ User {email} registered successfully!")

    @staticmethod
    def authenticate(email, password, filename="data/login.csv"):
        """Authenticates a user by checking email and encrypted password"""
        users = CSVHandler.load_from_csv(filename)
        for row in users:
            if len(row) == 3 and row[0] == email:
                stored_password = row[1]
                if hashlib.sha256(password.encode()).hexdigest() == stored_password:
                    print(f"🔐 Login Successful! Welcome, {email}")
                    return True
        print("❌ Login Failed! Invalid credentials.")
        return False
