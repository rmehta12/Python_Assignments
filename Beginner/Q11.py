num = int(input("Enter a number: "))
while num >= 10:
    num = sum(int(digit) for digit in str(num))

print(f"Final Output: {num}")
