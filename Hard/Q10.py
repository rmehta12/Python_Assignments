def unserviced_customers(N, S):
    available = set()
    left_customers = set()

    for char in S:
        if char in available:
            available.remove(char)
        elif len(available) < N:
            available.add(char)
        else:
            left_customers.add(char)

    return len(left_customers)


N = int(input("Enter the number of computers: "))
S = input("Enter the sequence of customer events: ")
result = unserviced_customers(N, S)
print(f"Number of customers who left: {result}")
