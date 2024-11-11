import bcrypt #pip install bcrypt
# for password hashing

password = 'qwerty123'

# convert password to byte array:
password_as_bytes = password.encode('utf-8')

# generate the salt
salt  = bcrypt.gensalt()

# hash the password using salt
hash = bcrypt.hashpw(password_as_bytes,salt)

#print(hash)

# check if password is correct
result = bcrypt.checkpw(password_as_bytes,hash) 
print(result)# True or False