import sys 
if len(sys.argv) == 2: 
salary = sys.argv[1] 
print("User provided input value:") 
else: 
print("No input given - using default value:") 
salary = "30000"  # default salary 
bonus = eval(salary) * 0.10 
total = eval(salary) + bonus 
print("Bonus Amount:", bonus) 
print("Total Salary after Bonus:", total) 
