num = float(input())
score_list = list(map(float, input().split()))
new_score = []
max_score = max(score_list)
for i in score_list:
    new = float(i) / max_score * 100
    new_score.append(new)
avg = sum(new_score)/len(new_score)
print(avg)