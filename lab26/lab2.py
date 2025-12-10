n = int(input())
for i in range(n,0,-1):
    p = n
    for j in range(1,i+1):
        print(j,end="")
        p -= 1
    print()