from math import ceil


def get_IofC_for_key_length_from_starting_pos(str, key_length, starting_pos):
    total_char_count = ceil((len(str) - starting_pos) / float(key_length))
    frequency = {}

    for i in xrange(starting_pos, len(str), key_length):
        c = str[i]
        if c in frequency:
            frequency[c] += 1
        else:
            frequency[c] = 1
    
    index_of_coincidence = 0.0
    for key, value in frequency.iteritems():
        index_of_coincidence += value * (value - 1)
    index_of_coincidence /= total_char_count * (total_char_count - 1)

    return index_of_coincidence


def get_avg_IofC_for_key_length(str, key_length):
    avg_index_of_coincidence = 0.0
    for i in range(0, key_length):
        avg_index_of_coincidence += get_IofC_for_key_length_from_starting_pos(str, key_length, i)
    avg_index_of_coincidence /= key_length
    return avg_index_of_coincidence


def get_avg_IofC(str, max_key_length):
    avg_IofC_list = []
    for i in range(1, max_key_length + 1):
        avg_IofC_list.append(get_avg_IofC_for_key_length(str, i))
    return avg_IofC_list



input_file = open('cipher_text.txt', 'r')
input = input_file.read()

total_char_count = 0.0
frequency = {}
for i in range(ord('A'), ord('Z') + 1):
    frequency[chr(i)] = 0

for c in input:
    frequency[c] += 1
    total_char_count += 1

output_file = open('frequency_analysis.txt', 'w')

output_file.write("frequency\n")
for key, value in frequency.iteritems():
    output_file.write("%s: %d times\t%f percentage\n" % (key, value, value / total_char_count))

output_file.write("\n sorted frequency\n")
for key in sorted(frequency, key=frequency.get, reverse=True):
    output_file.write("%s: %d times\t%f percentage\n" % (key, frequency[key], frequency[key] / total_char_count))

output_file.write("\nIndex of coincidence: %f\n" % get_avg_IofC_for_key_length(input, 1))
output_file.write("Total character count: %d\n" % total_char_count)

key_length = 1
output_file.write("\nAVG IofC for each key lengths:\n")
for iofc in get_avg_IofC(input, len(input) / 2):
    output_file.write("key length: %d -> %s\n" % (key_length, iofc))
    key_length += 1


input_file.close()
output_file.close()
