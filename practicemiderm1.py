print("Enter the hours worked: ")
hours_worked = float(input())
bonus_pay=0
total_hours=0
payRate = 10.0
overtime_pay = 0
while hours_worked >= 0:
    total_hours += hours_worked
    if hours_worked > 10:
        bonus_pay += 13
    if total_hours > 40:
        normal_pay = 40*payRate
        overtime_pay = (total_hours-40) * (1.5*payRate)
    elif total_hours <= 40:
        normal_pay = total_hours * payRate
    hours_worked = float(input())
total_pay = bonus_pay + overtime_pay + normal_pay
print("Bonus pay: ", bonus_pay)
print("Overtime pay: ", overtime_pay)
print("Total pay: ", total_pay)
