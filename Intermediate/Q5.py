temps = list(map(int, input("Enter temperature readings: ").split()))
average_temp = sum(temps) / len(temps)
highest_temp = max(temps)
lowest_temp = min(temps)

print(f"Average: {average_temp}, Highest: {highest_temp}, Lowest: {lowest_temp}")
