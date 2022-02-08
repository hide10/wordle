import re
import copy

tmp_list = []
frq_str = "earotlisncuydhpmgbfkwvzxqj"
frq_lists = list(frq_str)

f = open('wordle_la.txt', 'r')
datalist = f.read().splitlines()

print("correct and wrong:")

correct_list = list(input())

for i, in_str in enumerate(correct_list):
    if re.match("[A-Z]", in_str):
        for wd in datalist:
            if wd[i] == in_str.lower():
                tmp_list.append(wd)
        datalist = copy.copy(tmp_list)
        tmp_list.clear()
    elif re.match("[a-z]", in_str):
        for wd in datalist:
            if in_str.lower() in wd and not wd[i] == in_str.lower():
                tmp_list.append(wd)
        datalist = copy.copy(tmp_list)
        tmp_list.clear()

print()
print("not in any spot:")

not_in_str_list = list(input())
for i, in_str in enumerate(not_in_str_list):
    for wd in datalist:
        if not in_str.lower() in wd:
            tmp_list.append(wd)
    datalist = copy.copy(tmp_list)
    tmp_list.clear()

print()
print("Possible words:")

for i in range(len(correct_list)):
    correct_list[i] = correct_list[i].lower()

printable = False

for frq in frq_lists:
    if frq not in correct_list and frq not in not_in_str_list:
        for str in datalist:
            if frq in str:
                print(str)
                printable = True
        break

if not printable:
    for str in datalist:
        print(str)
