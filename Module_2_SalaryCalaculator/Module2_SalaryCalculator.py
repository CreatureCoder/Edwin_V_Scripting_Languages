
Max_Length = 40
Column_Length = 30


print("=" * Max_Length)
print(" The Salary Calculator Program")
print("=" * Max_Length, end="\n\n")


Salary_Hour = float (input(f"{'  Salary per hour':.<{Column_Length}}",))
Hours_Week = float (input(f"{'  Hours per week':.<{Column_Length}}",))
Holidays = float (input(f"{'  Holidays per year':.<{Column_Length}}",))
Vacations = float (input(f"{'  Vacation days per year':.<{Column_Length}}",))
print("\n", "=" * Max_Length)


print(Salary_Hour)
print(Hours_Week)
print(Holidays)
print(Vacations)
