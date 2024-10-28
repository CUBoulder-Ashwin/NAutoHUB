import csv
import os
import time
import string
import secrets
from cryptography.fernet import Fernet

# Load or generate encryption key for password storage (store securely in production)
key = Fernet.generate_key()  # Replace this with a securely stored key in production
cipher_suite = Fernet(key)

# Define file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
ipam_dir = os.path.join(script_dir, '..', 'IPAM')
hosts_csv = os.path.join(ipam_dir, 'hosts.csv')
check_interval = 1800  # 30 minutes

def generate_random_password(length=12):
    """Generates a secure random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def generate_password():
    """Generates a new random password and encrypts it."""
    new_password = generate_random_password()
    encrypted_password = cipher_suite.encrypt(new_password.encode()).decode()
    return new_password, encrypted_password

def main():
    """Main function to rotate passwords and update CSV every interval."""
    while True:
        updated_rows = []

        # Read and update password fields in CSV
        with open(hosts_csv, mode='r') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames if 'old_password' in reader.fieldnames else reader.fieldnames + ['old_password', 'new_password']
            
            for row in reader:
                # Rotate old and new passwords
                if 'new_password' in row:
                    row['old_password'] = row['new_password']

                # Generate new password and encrypt it
                _, encrypted_password = generate_password()
                row['new_password'] = encrypted_password  # Update with the encrypted new password
                
                updated_rows.append(row)  # Store updated row for writing

        # Write updated data back to the CSV file
        with open(hosts_csv, mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_rows)

        print("Password rotation complete for all devices in CSV. Waiting for next interval.")
        time.sleep(check_interval)

if __name__ == "__main__":
    main()
