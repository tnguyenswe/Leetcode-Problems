
target = 9
nums = [3, 15, 21, 42]

hashmap = {}

for i, val in enumerate(nums):
  new_target = target - nums[i]
  if new_target in hashmap:
     print(hashmap[new_target], i)
  else:
     hashmap[val] = i
