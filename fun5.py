import time
def sum():
    s = 0
    for i in range(1, 100000):
        s += i
    return s
start = time.time()
res = sum()
end = time.time()
print(res)
print(start-end)