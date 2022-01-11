''' NAME = SHARANG KALRA
SID= 21103012
BRANCH = COMPUTER SCIENCE AND ENGINEERING'''

# Assignment 1
# QUESTION =2

Standard_deduction= 10000
dependent= int(input("NUMBER OF DEPENDENTS ARE :"))
Gross_income = int(input("Enter the gross income :"))
dependent_deduction_amount= dependent*3000
taxable_income = Gross_income - Standard_deduction - dependent_deduction_amount
# Tax is 20% of taxable_income
tax= float((20/100)*(taxable_income))
print("your income tax is :", tax)