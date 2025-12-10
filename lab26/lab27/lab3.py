n = int(input())
for i in range(n+1):
    p = n
    for j in range(i+1):
        print(p,end='')
        p -= 1
    print()    