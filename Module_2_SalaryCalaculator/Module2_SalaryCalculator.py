
Max_Length = 40
Column_Length = 30


print("=" * Max_Length)
print(" The Salary Calculator Program")
print("=" * Max_Length, end="\n\n")


Salary_Hour = float (input(f"{'  Salary per hour':.<{Column_Length}}",))
Hours_Week = float (input(f"{'  Hours per week':.<{Column_Length}}",))
Days_Week = float (input(f"{'  Days per week':.<{Column_Length}}",))
Holidays = float (input(f"{'  Holidays per year':.<{Column_Length}}",))
Vacations = float (input(f"{'  Vacation days per year':.<{Column_Length}}",))
print("\n", "=" * Max_Length)


Unadjusted_Wage = Salary_Hour * Hours_Week * (365 - Days_Week * 52 + 1)
adjusted_Wage = Salary_Hour * Hours_Week * ((365 - Days_Week * 52 + 1) - Holidays - Vacations)

print = (Unadjusted_Wage)
print = (adjusted_Wage)

13.3
40
5

