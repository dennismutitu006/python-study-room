#!/usr/bin/env python3
'''example of bcrypt hashing'''
import bcrypt

#harshing a password

password = b"my_secure_password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

#checking if password is succesfully hashed

if bcrypt.checkpw(password, hashed):
    print("Password matches!")
else:
    print("password does not match")
