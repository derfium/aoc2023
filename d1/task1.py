import re

with open("d1/input.txt") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        nums = re.findall(r'\d', line)
        sum += int(nums[0] + nums[-1])
        
print(sum) # 54632
        
            
                