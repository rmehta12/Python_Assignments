num = int(input("Enter a number: "))
sum_divisors = sum(i for i in range(1, num // 2 + 1) if num % i == 0)

if sum_divisors == num:
    print("Yes, it's a Perfect Number")
else:
    print("No, it's not a Perfect Number")
