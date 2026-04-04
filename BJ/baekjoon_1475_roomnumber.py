# import sys
# import collections

# count = 1
# room_number = sys.stdin.readline().strip()

# counter_number = collections.Counter(room_number)

# six_nine = counter_number['6'] + counter_number['9']

# for c in counter_number:
#     if c != '6' and c != '9':  # or → and
#         if counter_number[c] > count:
#             count = counter_number[c]
#     else:
#         if (six_nine + 1) // 2 > count:
#             count = (six_nine + 1) // 2

# print(count)

import sys
import collections

room = sys.stdin.readline().strip()
cnt = collections.Counter(room)

six_nine = cnt['6'] + cnt['9']
# 올림 나눗셈 - 669와 같이 갯수가 홀수이더라도 여전히 한 세트가 더 필요하기 때문
cnt['6'] = (six_nine + 1) // 2
cnt['9'] = 0

print(max(cnt.values()))