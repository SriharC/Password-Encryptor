import string
import secrets
from cryptography.fernet import Fernet
import bcrypt

## Prompt user for password they want encrypted and the method of enryption to be used      
password = input("Enter your password: ")
encryption_method = input("\nPick how you want your password to be encrypted:\n\n1. Random Letters/Numbers\n\n2. Hash Encryption\n\n3. AES128-bit Encryption\n\n>> ")
#Random Char Algorithm using secrets module
if encryption_method == '1':
    listed_pass = list(password)
    count = 0
    for _ in listed_pass:
        if (count % 2) == 0:
            listed_pass[count] = secrets.choice(string.ascii_lowercase)
        else:
            listed_pass[count] = str(secrets.randbelow(100))
        count += 1
    encrypted_password = ''.join(listed_pass)
    print("\nRandom Char Encrypted password: {}".format(encrypted_password))
#Hash Encryption using Bycrypt and salt
elif encryption_method == '2':
    byte_pass = password.encode('utf-8')
    salt = bcrypt.gensalt()
    encrypted_password = bcrypt.hashpw(byte_pass, salt)
    print("\nHash Encrypted password: {}".format(encrypted_password))
#AE28 Bit Encryption Algorithm using Fernet module
elif encryption_method == '3':
    encryption_key = Fernet.generate_key()
    f = Fernet(encryption_key)
    encrypted_password = f.encrypt(password.encode('utf-8'))
    print("\nAe28 Bit Encrypted password: {}".format(encrypted_password))
#Option to save enrypted passwords to a file or exit 
option = input("\n\n(1)Save encrypted passwords to a file\n\n(2)Exit\n\nSelect an option: ")
if option == '1':
    with open('EncryptedPwds.txt', 'a') as pass_file:
        pass_file.write('{}\n\n'.format(str(encrypted_password)))
elif option == '2':
    print("\n\nExitting...")
