def display(x):
    if x == 50:
        return
    else:
        print(x)
        x += 1
    display(x)
display(4)