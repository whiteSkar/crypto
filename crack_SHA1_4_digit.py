from itertools import product 
import hashlib
import sys


if len(sys.argv) != 2:
    print("You gotta supply the SHA1 hash")
    sys.exit()

target_hash = sys.argv[1]
salt = target_hash[:len(target_hash) - 40]
target_hash = target_hash[len(salt):].lower()

seed_str = '0123456789'
for tuple in product(seed_str, repeat=4):
    word = ''.join(tuple)
    word = salt + word
    sha = hashlib.sha1() 
    sha.update(word.encode())
    sha_out = sha.hexdigest()
    print("%s %s" %(word, sha_out))
    if (sha_out == target_hash):
        print("Match found: %s %s %s" % (word[len(salt):], target_hash, salt))
        sys.exit()

print("No match found")
