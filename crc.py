from itertools import permutations
from binascii import crc32
from nltk.corpus import words


# using english words as words_set seems sufficient
def crc_attack_strong_collision(words_set):
    crc_values = dict()
    for word in words_set:
        crc_value = crc32(bytes(word, 'UTF-8'))
        #print("word: %s\t\tcrc_value: %s" % (word, crc_value))
        if crc_value in crc_values:
            return crc_values[crc_value], word
        crc_values[crc_value] = word
    return None

# takes about 40 min to find the solution with length 6 for my hash
def crc_attack_weak_collision():
    crc_value_of_x = crc32(bytes('6231168D48743EB081D20AF60CD967E6', 'UTF-8'))
    perm_length = 1
    seed_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+`-=|/.,;l:"][{}'
    while perm_length <= len(seed_str):
        for tuple in permutations(seed_str, perm_length):
            word = ''.join(tuple)
            crc_value = crc32(bytes(word, 'UTF-8'))
            #print("word: %s\t\tcrc_value: %s" % (word, crc_value))
            if crc_value == crc_value_of_x:
                return word
        perm_length += 1
    return None


words_set = set();
for word in words.words():
    words_set.add(word.lower())

print("Starting strong collision attack")
print("strong collision: x = %s and y = %s" % (crc_attack_strong_collision(words_set)))
print("Starting weak collision attack")
print("y = %s" % crc_attack_weak_collision())
