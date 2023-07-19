s = input()
nums = []
ops = []
tmp = 0
for i in s:
    if i != '+' and i != '-':
        tmp *= 10
        tmp += int(i)
    else:
        nums.append(tmp)
        tmp = 0
        ops.append(i)
nums.append(tmp)
try:
    ms = ops.index('-') + 1
    print(sum(nums[:ms]) - sum(nums[ms:]))
except (Exception,):
    print(sum(nums))
