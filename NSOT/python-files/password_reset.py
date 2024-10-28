import csv
import os
import time
import string
import secrets
from cryptography.fernet import Fernet

# Generate encryption key for password storage and load from a secure location
key = Fernet.generate_key()  # Replace with a securely stored key
cipher_suite = Fernet(key)

# Set up file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
ipam_dir = os.path.join(script_dir, '..', 'IPAM')
hosts_csv = os.path.join(ipam_dir, 'hosts.csv')
check_interval = 1800  # 30 minutes in seconds

def generate_random_password(length=12):
    """Generates a secure random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def generate_password():
    """Generates a new password and encrypts it."""
    new_password = generate_random_password()  # Generates a new random password
    encrypted_password = cipher_suite.encrypt(new_password.encode()).decode()
    return new_password, encrypted_password

def main():
    while True:
        updated_rows = []

        # Read existing CSV content and update password fields
        with open(hosts_csv, mode='r') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames if 'old_password' in reader.fieldnames else reader.fieldnames + ['old_password', 'new_password']
            
            for row in reader:
                # If 'new_password' exists, set it as 'old_password'
                if 'new_password' in row:
                    row['old_password'] = row['new_password']

                # Generate new password and encrypted version
                new_password, encrypted_password = generate_password()
                row['new_password'] = encrypted_password  # Update new password field
                
                updated_rows.append(row)  # Save updated row

        # Write updated data back to the same CSV file
        with open(hosts_csv, mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_rows)

        print("Password rotated for all devices in CSV. Waiting for next interval.")
        time.sleep(check_interval)

if __name__ == "__main__":
    main()
