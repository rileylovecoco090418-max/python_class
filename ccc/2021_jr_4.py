########### Read file block
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
print(cur_dir)

file_path = cur_dir + '/2021_jr_4.txt'
print(file_path)

# Read
f = open(file_path, 'r')
lines = f.readlines()
# print(lines)
lines = [line.strip() for line in lines]
# print(lines)
########### Read file block

########### Logic block
def arranging_books(books):
    l, m, s = 0
    for book in books:
        if book == 'L':
            l += 1
        elif book == 'M':
            m += 1
        elif book == 'S':
            s += 1
    print()
########### Logic block

########### Run block
arranging_books(lines)
########### Run block

########### Read file block
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
print(cur_dir)

file_path = cur_dir + '/2021_jr_4.txt'
print(file_path)

# Read
f = open(file_path, 'r')
lines = f.readlines()
# print(lines)
lines = [line.strip() for line in lines]
# print(lines)
########### Read file block

########### Logic block
def arranging_books(books):
    # books = 'LLSLM'

    # count books by types
    l, m, s = 0
    for book in books:
        if 'L' == book:
            l += 1
        elif 'M' == book:
            m += 1
        elif 'S' == book:
            s += 1

    # count wrong books in the block ranges
    # LLSSLM 
    # LLLMSS
    # books[:l] all L : LLS -> S1
    # books[l:l+m] all M : S -> S1
    # books[l+m:] all S : LM -> L1, M1
    l_block = books[:l]
    m_block = books[l:l+m]
    s_block = books[l+m:]

    l_dict = {'L':0, 'M':0, 'S': 0}
    for book in l_block:
        if 'L' == book:
            l_dict['L'] += 1
        elif 'M' == book:
            l_dict['M'] += 1
        elif 'S' == book:
            l_dict['S'] += 1

    m_dict = {'L':0, 'M':0, 'S': 0}
    for book in m_block:
        if 'L' == book:
            m_dict['L'] += 1
        elif 'M' == book:
            m_dict['M'] += 1
        elif 'S' == book:
            m_dict['S'] += 1

    s_dict = {'L':0, 'M':0, 'S': 0}
    for book in s_block:
        if 'L' == book:
            s_dict['L'] += 1
        elif 'M' == book:
            s_dict['M'] += 1
        elif 'S' == book:
            s_dict['S'] += 1

    result = 0
    while l_dict['M'] != 0 and m_dict['L'] != 0:
        l_dict['M'] -= 1
        m_dict['L'] -= 1
        result += 1
    
    while l_dict['S'] != 0 and s_dict['L'] != 0:
        l_dict['S'] -= 1
        m_dict['L'] -= 1
        result += 1
    
    # l_dict[S], s_dict[L]
    # l_dict[S], s_dict[L]

    # l_dict[S], s_dict[L]
    # l_dict[S], s_dict[L]

    result = l_dict['L'] + l_dict['S'] # + ...
    return result
    # print()
########### Logic block

########### Run block
arranging_books(lines)
########### Run block


