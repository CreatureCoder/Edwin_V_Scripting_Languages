#
#
#

Max_Length = 40
Column_Length = 30


print("=" * Max_Length)
print(" The Salary Calculator Program")
print("=" * Max_Length)


Salary_Hour = float (input(f"{'  Salary per hour':.<{Column_Length}}: ",))
Hours_Week = float (input(f"{'  Hours per week':.<{Column_Length}}: ",))
Days_Week = float (input(f"{'  Days per week':.<{Column_Length}}: ",))
Holidays = float (input(f"{'  Holidays per year':.<{Column_Length}}: ",))
Vacations = float (input(f"{'  Vacation days per year':.<{Column_Length}}: ",))
print("=" * Max_Length)

Unadjusted_Salary = (Salary_Hour * Hours_Week * 52)
Adjusted_Salary = (Salary_Hour * 8 * (Days_Week * 52 - Holidays - Vacations))

print(f"{' Your Unadjusted Salary':.<{Column_Length}}: ${Unadjusted_Salary:6,.2f}")
print(f"{' Your Adjusted Salary':.<{Column_Length}}: ${Adjusted_Salary:6,.2f}")
