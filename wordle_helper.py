import re
import copy
import sys

tmp_list = []
frq_str = "earotlisncuydhpmgbfkwvzxqj"
frq_lists = list(frq_str)


while True:
    f = open('wordle_ma.txt', 'r')
    datalist = f.read().splitlines()
    tmp_list.clear()

    print("correct and wrong: ", end='')
    correct_str_list = list(input())
    if len(correct_str_list) > 5:
        print("Error: The input is more than 5 characters.")
        continue

    print("not in any spot: ", end='')
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
            if in_str.lower() not in wd or in_str.lower() in correct_str_list or in_str.upper() in correct_str_list:
                tmp_list.append(wd)
        datalist = copy.copy(tmp_list)
        tmp_list.clear()

    print("Possible words: ", end='')
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

            if len(tmp_list) > 1:
                break
            else:
                possible_list.clear()
                possible_list = copy.copy(datalist)

    for i in range(len(possible_list)):
        print(possible_list[i].upper() + ",", end='')
        if i > 1:
            break

    print()
