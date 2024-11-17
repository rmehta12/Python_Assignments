arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter target sum K: "))
pair_count = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == k:
            pair_count += 1


print(f"Pair count: {pair_count}")
