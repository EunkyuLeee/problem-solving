import sys

t = int(input())
for i in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    nums = sys.stdin.readline().split(',')
    nums[0] = nums[0].replace('[', '')
    nums[len(nums)-1] = nums[len(nums)-1].replace(']\n', '')
    reverse = 0
    out = 1
    for j in range(len(p)):
        if p[j] == 'R':
            reverse += 1
        elif p[j] == 'D':
            if len(nums) == 0 or n == 0:
                print("error")
                out = 0
                break
            else:
                if reverse % 2 == 0:
                    nums.pop(0)
                else:
                    nums.pop(len(nums)-1)
    if reverse % 2 == 1:
        nums.reverse()
    if out == 1:
        print('[', end='')
        for index, value in enumerate(nums):
            print(value, end='')
            if index != len(nums)-1:
                print(',', end='')
        print(']')
