nums = list(map(int , input().split())) 
m = float('-inf') 
for val in nums:
    if val > m:
        m = val
  