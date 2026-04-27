# 2024 j4 -> run and debug/fix
# count letters input1
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
file_path = cur_dir + '/2024_jr_4.txt'
f = open(file_path, 'r')
input = f.readline

word_org = input()
letters_in_word_org = {}
for w in word_org:
    if w in letters_in_word_org:
        letters_in_word_org[w] += 1
    else:
        letters_in_word_org[w] = 1

# count letters input2
word_printed = input()
letters_in_word_printed = {}
for w in word_printed:
    if w in letters_in_word_printed:
        letters_in_word_printed[w] += 1
    else:
        letters_in_word_printed[w] = 1

# Comapre and identify
key_candidates = {}
for w_org, c_org in letters_in_word_org.items():
    if w_org in letters_in_word_printed:
        if c_org == letters_in_word_printed[w_org]:
            letters_in_word_printed.pop(w_org)
    else:
        key_candidates[w_org] = c_org

s_key = '-'
for l in letters_in_word_printed.keys():
    s_key = l

s_count = letters_in_word_printed[s_key]

s_key_org = ''
e_key = ''
for w_cand, c_cand in key_candidates.items():
    if c_cand == s_count:
        s_key_org = w_cand
    else:
        e_key = w_cand

print(s_key_org, s_key)
if e_key == '':
    print('-')
else:
    print(e_key)