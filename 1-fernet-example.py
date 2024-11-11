from cryptography.fernet import Fernet
# pip install cryptography

key = Fernet.generate_key()
f = Fernet(key)
#token = f.encrypt(b"my deep dark secret")
pw = "JOULU"
token = f.encrypt(pw.encode('utf-8'))
#print(token)

secret = f.decrypt(token)
#print(secret)
                            #write binary
with open('token-crypted.bin','wb') as file:
    file.write(token)