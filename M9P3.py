# Kirill M9P3 10/07/2023

# Define dunction
def compute(miles, galon):
# Finding MPG
    average = miles / galon
    return average

# Asking to continue program 
start = input("Do you want to continue? (Y/N) ")
entries_made = 0

# Beggining of the loop
while start == "Y":

# Asking to user enter destination city, miles, and galon
    destination_city = input("Enter destination city: ")
    miles = int(input("Enter miles travelled: "))
    galon = int(input("Enter galon used for a trip: "))

# Calling function in the loop
    average = compute(miles, galon)

# Additing one more user in variable 
    entries_made += 1

# Printing 3 conditions
    print(f"Destination city: {destination_city}")
    print(f"Miles: {miles}")
    print(f"MPG: {average:.2f}")

# Asking to continue program 
    start = input("Do you want to continue? (Y/N) ")

# Printing final statement
print(f"Entries made: {entries_made}")