from hashlib import sha256
import os
import random

path = "test"
way = "#"


key = input("clÃ© de sÃ©curitÃ©")
h_key = sha256(key.encode('utf-8')).digest()

for filename in os.listdir(path):
    f = os.path.join(path, filename)

    if os.path.isfile(f):
        with open(f, 'rb') as f_entree:
            if f_entree.name[-1] == "#":
               way = " "

            with open(f_entree.name[0:-1] + way , 'wb') as f_sortie:

                i = 0
                while f_entree.peek():
                    c = ord(f_entree.read(1))
                    j = i % len(h_key)
                    b = bytes([c^h_key[j]])
                    f_sortie.write(b)
                    i += 1
            os.remove(f)
