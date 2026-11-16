# Get the total hours worked from the user
hours = float(input("Enter total hours worked: "))

# Calculate weekly pay ($20/hr for first 40 hours, $30/hr for overtime)
if hours > 40:
    pay = (40 * 20) + ((hours - 40) * 30)
else:
    pay = hours * 20

# Output the final paycheck amount
print(f"Total weekly pay: ${pay:.2f}")