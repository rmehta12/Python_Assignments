username = input("Enter username: ")
password = input("Enter password: ")

for attempt in range(3):
    pwd = input("Re-enter password: ")

    if pwd == password:
        print("Login successful!")
        break
    else:
        print("Incorrect username or password.")
else:
    print("Too many attempts. Access denied!")
