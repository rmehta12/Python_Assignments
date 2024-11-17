string = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0

for c in string:
    if c in vowels:
        count += 1
print(f"Number of vowels: {count}")
