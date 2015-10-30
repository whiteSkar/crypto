from itertools import product 
import hashlib
import random
import sys


if len(sys.argv) != 2:
    print("You gotta supply the SHA1 hash")
    sys.exit()

target_hash = sys.argv[1]
salt = target_hash[:len(target_hash) - 40]
target_hash = target_hash[len(salt):].lower()
print("salt: %s hash: %s" % (salt, target_hash))

seed_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-='
shuffled_seed = list(seed_str)
random.shuffle(shuffled_seed)
seed_str = ''.join(shuffled_seed)
print("Using seed str: %s" % seed_str)

count = 0
total_count = 0
for tuple in product(seed_str, repeat=6):
    word = ''.join(tuple)
    word = salt + word
    
    sha = hashlib.sha1() 
    sha.update(word.encode())
    sha_out = sha.hexdigest()

    count += 1
    if count == 1000000:
        total_count += count
        count = 0
        print("%d hashes compared. Current word: %s" %(total_count, word))

    if (sha_out == target_hash):
        print("Match found: %s %s %s" % (word[len(salt):], target_hash, salt))
        sys.exit()

print("No match found")
