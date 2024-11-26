# Initialize a variable to store the sum
total = 0

# Loop to get 10 numbers from the user
for i in range(10):
    number = float(input(f"Enter number {i + 1}: "))
    total += number

# Print the total sum
print(f"The total sum of the 10 numbers is: {total}")
