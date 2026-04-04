import sys
import collections

word = sys.stdin.readline().strip().upper()

counter_str = collections.Counter(word).most_common(2)
if len(counter_str) >1:
    print(counter_str[0][0] if counter_str[0][1] != counter_str[1][1] else "?")
else:
    print(counter_str[0][0])