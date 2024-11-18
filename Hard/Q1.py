with open("doc.txt", "r") as file:
    content = file.read().split()
    even_length_strings = [word for word in content if len(word) % 2 == 0]

print(f"Even length strings: {' '.join(even_length_strings)}")
