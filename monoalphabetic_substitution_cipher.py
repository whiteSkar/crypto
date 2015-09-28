import random
from ngram_score import ngram_score


def decipher(str, key_list):
    key_dict = dict()
    val = ord('A')
    for c in key_list:
        key_dict[c] = chr(val)
        val += 1
    result = ""
    for c in str:
        if c in key_dict:
            result += key_dict[c]
    return result


fit = ngram_score('quadgrams.txt')
c_text = open('cipher_text.txt', 'r').read()
out_file = open('monoalphabetic_substitution_cipher_output.txt', 'w')

global_best_score = -999999999
global_best_key = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

while True:
    local_best_key = global_best_key[:]
    random.shuffle(local_best_key)
   
    local_p_text = decipher(c_text, local_best_key)
    local_best_score = fit.score(local_p_text)
    loop_count = 0
    while loop_count < 1000:
        index1 = random.randint(0, 25)
        index2 = random.randint(0, 25)
        if index1 == index2:
            continue

        cur_key = local_best_key[:]
        cur_key[index1], cur_key[index2] = cur_key[index2], cur_key[index1]
        cur_p_text = decipher(c_text, cur_key)
        cur_score = fit.score(cur_p_text)
        if (cur_score > local_best_score):
            local_best_score = cur_score
            local_best_key = cur_key
            loop_count = 0
        else:
            loop_count += 1

    if local_best_score > global_best_score:
        global_best_score = local_best_score
        global_best_key = local_best_key
        global_best_p_text = decipher(c_text, global_best_key)
        output_str = "Best score so far: %d, key: %s, plaintext:\n%s\n\n"
        print(output_str % (global_best_score, ''.join(global_best_key), global_best_p_text))
        out_file.write(output_str % (global_best_score, ''.join(global_best_key), global_best_p_text)) 
        out_file.flush()

out_file.close()
