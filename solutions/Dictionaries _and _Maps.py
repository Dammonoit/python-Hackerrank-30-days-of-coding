n=int(input()) 
d = dict(input().split() for i in range(n))
print(d)
for i in d:
    #print(i)
    n1=input()
    #print(n1)
    if n1==i:
      print(i,"=",d[i])
    else:
      print("Not found.")


        
