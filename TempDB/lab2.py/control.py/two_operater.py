a = int(input())
b = int(input())
op_one, op_two = input("Enter only two operators seperator with comma").split(',')
if op_one == '*':
    print(a*b)
elif op_one == '-':
    print(a-b)
elif op_one == '+':
    print(a+b)
elif op_one == '/':
    print(a/b) 
if op_two == '*':  
    print(a*b)
elif op_two == '-':
    print(a-b)
elif op_two == '+':
    print(a+b)
elif op_two == '/':
    print(a/b)   
