#Nick Caravaggio
# main controller for final project- Example interface with buttons and minor
# functionalities include temporary key encryption and decryption.

import sys
import scapy.all as scapy
import socket
from cryptography.fernet import Fernet, MultiFernet
from faker import Faker

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

# Instantiation of keys for cryptography, so that keys can be de-crypted
# in the same session.
main_key = Fernet(Fernet.generate_key())

# Main faker output function
def fake_choice(choice):
    fake = Faker()
    if choice == 1:
        return fake.name()
    elif choice == 2:
        return fake.address()
    elif choice == 3:
        return fake.text()
    elif choice == 4:
        return fake.company()

# Note: when decryption is invalid, it leaves a nasty terminal message which
# is just the norm for this module I suppose. There is no "verification"
# function that I could find.
def crypt_choice(input_str,choice):
    if choice == 1:
        encrypted_str = str(main_key.encrypt(bytes(input_str,'utf-8')))
        encrypted_str = encrypted_str[:-1]
        encrypted_str = encrypted_str[2:]
        return encrypted_str
    elif choice == 2:
        try:
            encrypted_str = str(main_key.decrypt(bytes(input_str,'utf-8')))
        # I can't get this except to work for the life of me, but i really did
        # try to avoid the ugly text, but that's just what happens when tokens
        # are invalid for now because I can't get it to work properly.
        except (cryptography.fernet.InvalidToken, NameError):
            return ("Invalid or Expired Token.")
        encrypted_str = encrypted_str[:-1]
        encrypted_str = encrypted_str[2:]
        return encrypted_str

