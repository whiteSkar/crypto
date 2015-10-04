from itertools import permutations


key_table = {'e': 0b000, 'h': 0b001, 'i': 0b010, 'k': 0b011,
             'l': 0b100, 'r': 0b101, 's': 0b110, 't': 0b111}

key_table_reverse = dict()
for key, value in key_table.iteritems():
    key_table_reverse[value] = key

key_string = "ehiklrst"

ct1 = "KHHLTK"
ct2 = "KTHLLE"

ct1 = ct1.lower()
ct2 = ct2.lower()

count = 0
for tuple in permutations(key_string, len(ct1)):
    possible_key = ''.join(tuple)
    pt1 = ""
    pt2 = ""
    for i in range(0, len(ct1)):
        p1 = key_table[ct1[i]] ^ key_table[possible_key[i]]
        p2 = key_table[ct2[i]] ^ key_table[possible_key[i]]
        pt1 += key_table_reverse[p1]
        pt2 += key_table_reverse[p2] 
    count += 1
    print("pt1: %s\tpt2: %s\tkey: %s" % (pt1, pt2, possible_key))
print("count: %d" % count)
