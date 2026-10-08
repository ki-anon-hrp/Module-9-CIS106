# Kirill M9P2 10/07/2026

# Define a function
def batting_average(number_hits, bats):
    average_bat = number_hits / bats
    return average_bat

# Asking to continue program 
start = input("Do you want to continue? (Y/N) ")

# Define a variable for count of users
total_players = 0

# Beginning of the loop
while start == "Y":

# Asking to enter last name, number of hits, and bats
    last_name = input("Enter your last name: ")
    number_hits = int(input("Enter number of hits: "))
    bats = int(input("Enter number of bats: "))

# Calling for function
    average_bat = batting_average(number_hits, bats)
# Additing into variable one user
    total_players += 1

# Printing 2 conditions
    print(f"Last name: {last_name}")
    print(f"Batting average: {average_bat:,.2f}")

# Asking to continue program 
    start = input("Do you want to continue? (Y/N)")

# Printing final statmenet
print(f"Total number of players: {total_players}") 