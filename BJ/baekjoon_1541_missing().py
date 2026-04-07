import sys

a = sys.stdin.readline().strip()
# a = "00009-00009"

if "-" in a:
    b = a.split("-")

    for i in range(len(b)):
        if "+" in b[i]:
            c = b[i].split("+")
            s = 0
            for x in range(len(c)):
                s += int(c[x])
            b[i] = s
    # print(b)

    minus = int(b[0])
    for i in range(1, len(b)):
        minus = minus - int(b[i])
    print(minus)
else:
    b = a.split("+")
    s = 0
    for i in range(len(b)):
        s += int(b[i])
    print(s)
