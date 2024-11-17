nums = sorted(map(int, input("Enter numbers: ").split()))
n = len(nums)
median = (nums[n // 2] + nums[(n - 1) // 2]) / 2

print(f"Median: {median}")
