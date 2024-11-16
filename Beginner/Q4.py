start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
odd_sum = sum(num for num in range(start, stop + 1) if num % 2 != 0)

print(f"Sum of odd numbers: {odd_sum}")
