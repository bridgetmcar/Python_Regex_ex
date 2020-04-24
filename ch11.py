import re

handle = open("regex_sum_42.txt")

nums = list()

for line in handle:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) == 0 : continue
    for x in stuff:
        num = float(x)
        nums.append(num)
print(len(nums))
print(sum(nums))
# count = 0
# for x in nums:
#     count = count + x
# print(count)
