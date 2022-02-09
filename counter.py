import collections
import pprint

f = open('wordle_la.txt', 'r')

contents = f.read()
count = collections.Counter(contents)
pprint.pprint(count.most_common())
