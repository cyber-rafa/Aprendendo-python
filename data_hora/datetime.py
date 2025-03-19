from datetime import date

# Create a specific date
d = date(2020, 10, 2)
print(f"The date is: {d}")

# Get today's date
today = date.today()
print(f"Today's date is: {today}")

# Format dates
print(f"Today's date formatted (DD/MM/YYYY): {today:%d/%m/%Y}")