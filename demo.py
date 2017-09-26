import sys
s, t= sys.stdin.readline()[:-1], sys.stdin.readline()[:-1]
flag = False
while t:
    for i in range(len(s)):
        if s[i] == t[0]:
            break
    else:
        flag = True
        break
    s = s[i+1:]
    t = t[1:]
if flag:
    print('No')
else :
    print('Yes')