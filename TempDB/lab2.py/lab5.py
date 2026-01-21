p = int(input())
t = int(input())
r = int(input())
s = p*t*r/100
c = p*((1+r/100)**t)-t
print("simple intrest" + str(s))
print("coumpound intrest" + str(c))
