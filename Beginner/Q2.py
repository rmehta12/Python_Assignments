string = input("Enter a string: ")
letters = sum(c.isalpha() for c in string)
digits = sum(c.isdigit() for c in string)

print(f"Alphabets: {letters} & Numbers: {digits}")
