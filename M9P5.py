# Kirill M9P5 10/07/2026

# Define function
def owed(district_code):
# If statment with specific value of credit cost
    if district_code == "I":
        credit_cost = 250
    elif district_code == "O":
        credit_cost = 550
    return district_code, credit_cost

# Asking to continue program 
start = input("Do you want to continue? (Y/N) ")

# Defing variable for total tution
total_tution = 0

# Beggining of the loop
while start == "Y":

# Entering last name, credit hours, distrcit code
    last_name = input("Enter student last name: ")
    credit_hours = int(input("Enter credit hours: "))
    district_code = str(input("Enter distrcit code (I / O): "))

# Calling function in the loop
    district_code, credit_cost = owed(district_code)

# Finding cost of all credits for user 
    cost_definder = credit_hours * credit_cost

# Additing cost of user into total tution variable
    total_tution += cost_definder

# Printing student name and tution owed
    print(f"Student name: {last_name}")
    print(f"Tution owed: ${cost_definder}")

# Asking to continue program 

    start = input("Do you want to continue? (Y/N) ")

# Printing final statement
print(f"Total of all tuition owed: ${total_tution}")