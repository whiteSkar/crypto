cipher_text_file = open('cipher_text.txt', 'r')
cipher_text = cipher_text_file.read()

output_file = open('caesar_output.txt', 'w')

for i in range(1, 27):
    output = ''
    for c in cipher_text:
        c_unicode = ord(c) + i
        if c_unicode > ord('Z'):
            c_unicode -= 26
        output += chr(c_unicode)
    output_file.write("%s\n\n" % output)

cipher_text_file.close()
output_file.close()
