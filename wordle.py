import re
import copy

tmp_list = []

f = open('wordle.txt', 'r')
datalist = f.read().splitlines()

print("correct and wrong:")

in_str_list = list(input())

for i, in_str in enumerate(in_str_list):
    if re.match("[A-Z]", in_str):
        for wd in datalist:
            if wd[i] == in_str.lower():
                tmp_list.append(wd)
        datalist = copy.copy(tmp_list)
        tmp_list.clear()
    elif re.match("[a-z]", in_str):
        for wd in datalist:
            if in_str.lower() in wd:
                tmp_list.append(wd)
        datalist = copy.copy(tmp_list)
        tmp_list.clear()

print("not in any spot:")

in_str_list = list(input())
for i, in_str in enumerate(in_str_list):
    for wd in datalist:
        if not in_str.lower() in wd:
            tmp_list.append(wd)
    datalist = copy.copy(tmp_list)
    tmp_list.clear()

for str in datalist:
    print(str)
