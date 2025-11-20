import sys

if len(sys.argv) == 2:
    salary = sys.argv[1]
    print("User provided input value:", salary)
else:
    print("No input given - using default value:")
    salary = "30000"  # default salary

# Convert string to number (float)
salary_value = float(salary)

bonus = salary_value * 0.10
total = salary_value + bonus

print("Bonus Amount:", bonus)
print("Total Salary after Bonus:", total)
