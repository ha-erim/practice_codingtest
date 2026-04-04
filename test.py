n = int(input())
count=1
s = 1
s_i = 1
e_i = 1

while e_i != n:
    if s == n:
        count+=1
        e_i+=1
        s += e_i
    elif s > n:
        s -= s_i
        s_i += 1
    elif s < n:
        e_i += 1
        s += e_i

print(count)