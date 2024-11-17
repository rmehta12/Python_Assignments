arr = list(map(int, input("Enter array elements: ").split()))
d = int(input("Enter number of elements to rotate: "))
rotated_arr = arr[-d:] + arr[:-d]

print(f"Rotated array: {rotated_arr}")
