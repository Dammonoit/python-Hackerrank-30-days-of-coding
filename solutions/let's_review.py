n=int(input())
s=[input() for i in range(n)]
for i in range(len(s)):
    print(s[i][::2]+" "+s[i][1::2])

