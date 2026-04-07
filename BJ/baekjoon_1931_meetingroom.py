import sys

n = int(sys.stdin.readline().strip())

schedule = []
meeting_room = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    schedule.append((start, end))

## 끝나는 시간 기준 오름차순, 끝이 같으면 시작시간 빠른 순
schedule.sort(key=lambda x: (x[1], x[0]))

# print(schedule)
# 회의실 사용 끝난 시간
time = 0
# 선택한 회의 갯수
count = 0
for meeting in schedule:
    if time <= meeting[0]:
        time = meeting[1]
        count += 1

print(count)
