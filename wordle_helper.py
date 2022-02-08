import re
import copy
import sys

tmp_list = []
frq_str = "earotlisncuydhpmgbfkwvzxqj"
frq_lists = list(frq_str)

f = open('wordle_la.txt', 'r')

datalist = f.read().splitlines()
tmp_list.clear()

while True:
    print("correct and wrong:")
    correct_str_list = list(input())

    print()

    print("not in any spot:")
    not_in_str_list = list(input())

    if not correct_str_list and not not_in_str_list:
        sys.exit()

    for i, in_str in enumerate(correct_str_list):
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

    for i, in_str in enumerate(not_in_str_list):
        for wd in datalist:
            if not in_str.lower() in wd:
                tmp_list.append(wd)
        datalist = copy.copy(tmp_list)
        tmp_list.clear()

    print()
    print("Possible words:")
    possible_list = copy.copy(datalist)
    tmp_list.clear()

    for i in range(len(correct_str_list)):
        correct_str_list[i] = correct_str_list[i].lower()

    for frq in frq_lists:
        if frq not in correct_str_list and frq not in not_in_str_list:
            for str in possible_list:
                if frq in str:
                    tmp_list.append(str)

            possible_list = copy.copy(tmp_list)

            if len(tmp_list) > 6:
                not_in_str_list.append(frq)
                tmp_list.clear()
                continue
            elif len(tmp_list) > 0:
                break
            else:
                possible_list = copy.copy(datalist)

    [print(possible) for possible in possible_list]

    print()
