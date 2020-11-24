


nums = [7,1,5,3,6,4]

best_day = 0
min_val = 9999999

for i, val in enumerate(nums):
  if nums[i] < min_val:
    min_val = nums[i]
  else:
    best_day = max(best_day, nums[i] - min_val)

print(best_day)
