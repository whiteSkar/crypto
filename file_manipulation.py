import re
import sys


def extract_alphanumeric_text(min_len, max_len, in_file, out_file):
    content = in_file.readlines()
    regex = '^(?=.*[a-z])(?=.*[0-9])[a-z0-9]+$'

    for line in content:
        if len(line) >= min_len and len(line) <= max_len and re.match(regex, line):
            out_file.write(line)


if len(sys.argv) != 5:
    sys.exit()

in_file_path = sys.argv[1]
out_file_path = sys.argv[2]
min_len = int(sys.argv[3])
max_len = int(sys.argv[4])

in_file = open(in_file_path, 'r')
out_file = open(out_file_path, 'w')

extract_alphanumeric_text(min_len, max_len, in_file, out_file)

in_file.close()
out_file.close()
