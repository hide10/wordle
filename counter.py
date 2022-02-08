counter = [0] * 26

f = open('wordle_la.txt', 'r')

lines = f.readlines()
for line in lines:
    for i in range(26):
        counter[i] += line.count(chr(97+i))

for i in range(26):
    print(chr(97+i), counter[i])
