# Written by: Edwin V
# Date: January 25, 2023
# Creator's GitHub URL: https://github.com/CreatureCoder/Edwin_V_Scripting_Languages.git
# Description:
#     This program is designed, with a little design, to calculate the total salary with
# or without holidays or vacations of a person using the person's salary per hour, hours
# per week, days per week, Holidays, and vacation days

# Defined variables
Max_Length = 40
Column_Length = 30

# Start of program
print("=" * Max_Length)
print(" The Salary Calculator Program")
print("=" * Max_Length)

# Place where user inputs salary per hour, hours per week, days per week, holidays, and vacation days
Salary_Hour = float (input(f"{'  Salary per hour':.<{Column_Length}}: ",))
Hours_Week = float (input(f"{'  Hours per week':.<{Column_Length}}: ",))
Days_Week = float (input(f"{'  Days per week':.<{Column_Length}}: ",))
Holidays = float (input(f"{'  Holidays per year':.<{Column_Length}}: ",))
Vacations = float (input(f"{'  Vacation days per year':.<{Column_Length}}: ",))
print("=" * Max_Length)

# Calculation of salary with and without holidays, and vacation days
Unadjusted_Salary = (Salary_Hour * Hours_Week * 52)
Adjusted_Salary = (Salary_Hour * 8 * (Days_Week * 52 - Holidays - Vacations))

# Prints the calculated salaries
print(f"{' Your Unadjusted Salary':.<{Column_Length}}: ${Unadjusted_Salary:6,.2f}")
print(f"{' Your Adjusted Salary':.<{Column_Length}}: ${Adjusted_Salary:6,.2f}")

print("=" * Max_Length)
print("Goodbye!")
print("=" * Max_Length)
# End of program
