s = int(input())
l = []
for i in range(s):
    _id ,name, age, salary = input().split(',')
    l.append([int(_id), name, int(age), float(salary)])
print(l)