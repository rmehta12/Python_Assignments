def run_length_encode(input_string):
    encoded = []
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded.append(f"{input_string[i - 1]}{count}")
            count = 1

    encoded.append(f"{input_string[-1]}{count}")
    return "".join(encoded)


input_string = input("Enter the string: ")
encoded_string = run_length_encode(input_string)
print(encoded_string)
