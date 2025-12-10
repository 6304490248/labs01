n = int(input())
p = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        p +=1
        print(p,end='')
    print()  