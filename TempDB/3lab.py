total_seconds = int(input())
hours = total_seconds//3600
remaining_seconds = total_seconds % 3600
minuts = remaining_seconds//60
seconds = remaining_seconds%60
print(seconds)
print(hours)
print(minuts)