nums = list(map(int,input().split()))
nums.sort()
mid = len(nums)//2

if len(nums)%2 == 0:
    print((nums[mid-1]+nums[mid])/2)
else:
    print(nums[mid])