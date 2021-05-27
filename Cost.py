#expenses = [10.5,8,15,20,5,3]
#sum = 0
#for x in expenses:
   # sum+=x
#total = sum(expenses)
#print("you spent $", sum, " on lunch this week.", sep='')
#print("you spent $",total, " on lunch this week.", sep='')
#---------------------------------------#
total = 0
expenses = []
num_expenses = int(input("Enter # expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expenses: ")))
total = sum(expenses)
print("you spent $", total, sep='')
