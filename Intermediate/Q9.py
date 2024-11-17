try:
    arr = list(map(int, input("Enter list elements: ").split()))
    idx = int(input("Enter index to access: "))
    print(arr[idx])
except IndexError:
    print("Index out of range!")
