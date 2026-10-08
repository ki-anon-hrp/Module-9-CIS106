# Kirill M9P4 10/07/2026

# Define function
def determine(job_code):
# If statement with comparison of job code
    if job_code == "L":
        pay_rate = 25
    elif job_code == "A":
        pay_rate = 30
    elif job_code == "H":
        pay_rate = 50
    return job_code, pay_rate

# Asking to continue program 
start = input("Do you want to continue? (Y/N) ")

# Define total gross variable
total_gross = 0

# Beggining of the loop
while start == "Y":

# Entering last name, job code, and hours worked
    last_name = input("Enter last name: ")
    job_code = str(input("Enter job code (L / A / H): "))
    hours_worked = int(input("Enter hoursed worked: "))

# Calling function in the loop
    job_code, pay_rate = determine(job_code)

# If statement for comparing hours worked and additing into gross pay
    if hours_worked >= 40:
        regular_pay = 40 * pay_rate
        over_time = (hours_worked - 40) * (pay_rate * 1.5)  
        gross_pay = regular_pay + over_time
    else:
        gross_pay = hours_worked * pay_rate

# Additing in total gross, gross pay from the loop
    total_gross += gross_pay

# Printing last name and gross pay
    print(f"Last name : {last_name}")
    print(f"Gross pay: ${gross_pay}")

# Asking to continue program 
    start = input("Do you want to continue? (Y/N) ")

# Printing final statement
print(f"Total of all gross pay: {total_gross}")