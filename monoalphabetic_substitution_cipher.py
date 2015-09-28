input = open('cipher_text.txt', 'r').read()
potential_key = {'V': 'E',
                 'C': 'T',
                 'J': 'A',
                 'E': 'O',
                 'O': 'I',
                 'L': 'N',
                 'R': 'S',
                 'H': 'H',
                 'U': 'R',
                 'S': 'D',
                 'K': 'L',
                 'A': 'U',
                 'Z': 'C',
                 'P': 'M',
                 'Q': 'W',
                 'X': 'F',
                 'W': 'G',
                 'G': 'Y',
                 'F': 'P',
                 'I': 'B',
                 'D': 'V',
                 'B': 'K',
                 'Y': 'J',
                 'M': 'X',
                 'N': 'Q',
                 'T': 'Z'
                 }

output = ''
for c in input:
    output +=  potential_key[c]

open('monoalphabetic_substitution_cipher_output.txt', 'w').write(output)
