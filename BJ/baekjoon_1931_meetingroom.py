import sys

n = int(sys.stdin.readline().strip())

meeting_room = [[] for _ in range(n)]
meeting_room_schedule = [[0] for _ in range(n)]

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    for i in range(len(meeting_room)):
        # if meeting_room[i][start] == 0:
        #     meeting_room[i][start : end - 1] = [1] * (end - start)
        #     meeting_room_schedule[i][0] += 1
        #     break
        if not meeting_room[i]:
            meeting_room[i].append((start, end))
            break
        else:
            for x in len(meeting_room[i]):
                s1, e1 = x
                if e1:
                    meeting_room[i].append((start, end))


print(max(meeting_room_schedule)[0])
