import hashlib
import os
import sys


file_name = '30172092.program2.exe'
index_of_pass_hash = 75792


def get_sha1(pt):
    sha = hashlib.sha1()
    sha.update(pt.encode())
    return sha.hexdigest()

def patch_file(file_name, new_hash):
    hash_in_hex = bytearray.fromhex(new_hash)
    print(hash_in_hex)
    
    success = False
    with open(file_name, 'rb') as f:
        out_file = open(file_name + 'temp', 'wb')

        byte = f.read(index_of_pass_hash)
        out_file.write(byte)

        #for i in range(0, 20):
        out_file.write(hash_in_hex)
        print(hash_in_hex)
        f.read(20)
        byte = f.read()
        out_file.write(byte)
        out_file.close()
        success = True
    
    if success:
        os.remove(file_name)
        os.rename(file_name + 'temp', file_name)
    

if len(sys.argv) != 2:
    print("Wrong number of arguemnts. Please input only the new password")
    sys.exit()

new_pass = sys.argv[1]
sha1_hash = get_sha1(new_pass)
print("new hash:", sha1_hash)

patch_file(file_name, sha1_hash)
