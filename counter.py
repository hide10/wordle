import collections
import pprint

fst_char = [0] * 26
second_char = [0] * 26
third_char = [0] * 26
forth_char = [0] * 26
Fifth_char = [0] * 26

with open('wordle_ma.txt', 'r') as f:
    contents = f.read()
    count = collections.Counter(contents)
    pprint.pprint(count.most_common())

with open('wordle_ma.txt', 'r') as f:
    for line in f:
        for i in range(26):
            fst_char[i] += line[0].count(chr(ord('a')+i))
            second_char[i] += line[1].count(chr(ord('a')+i))
            third_char[i] += line[2].count(chr(ord('a')+i))
            forth_char[i] += line[3].count(chr(ord('a')+i))
            Fifth_char[i] += line[4].count(chr(ord('a')+i))

    for i in range(26):
        print(chr(ord('a')+i) + ": " + str(fst_char[i]) + ", " + str(second_char[i]) + ", " + str(third_char[i]) + ", " + str(forth_char[i]) + ", " + str(Fifth_char[i]))
