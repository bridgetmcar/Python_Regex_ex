import re

nums = list()

handle = open("regex_sum_458719.txt")
for line in handle:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0: continue
    for x in stuff:
        num = float(x)
        nums.append(num)
print(len(nums))
print(sum(nums))
