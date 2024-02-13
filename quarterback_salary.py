#question 1 Collect the base salary 
base_salary = float(input("Input the base salary: "))

#question 2 Collect the number of touchdown passes
touchdown_passes = int(input("How many touchdowns? "))

#question 3 Collect the number of fumbles 
qb_fumbles = int(input("How many fumbles? "))

#Salary Calculation 
additional_salary = 0.01 * base_salary * touchdown_passes
fumble_deductions = 5500 * qb_fumbles
total_salary = base_salary + additional_salary - fumble_deductions

#Calculating the quarterback contract for collection of 88% of the contract value
amount_collected = 0.88 * total_salary 

#Calculating amount donated to charity
donated_charity = 0.12 * total_salary 

#Printing the Output Statement 
print(f"The total salary is {total_salary}. The quarterback will take home {amount_collected} and donate {donated_charity}.")

