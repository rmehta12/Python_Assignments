def parse_string(encoded_string):
    parts = encoded_string.split("0")
    first_name = parts[0]
    i = 1
    while parts[i] == "":
        i += 1
        continue
    last_name = parts[i]
    id_value = parts[-1]
    return {"first_name": first_name, "last_name": last_name, "id": id_value}


encoded_string = "Robert000Smith000123"
result = parse_string(encoded_string)
print(result)
