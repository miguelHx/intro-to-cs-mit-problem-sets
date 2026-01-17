## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

yearly_salary = float(input('enter yearly salary: '))
portion_saved = float(input('enter % of salary to save, as a decimal: '))
cost_of_dream_home = float(input('enter cost of dream home: '))

portion_down_payment = 0.25

r = 0.05

down_payment_amount = cost_of_dream_home * portion_down_payment


first_month_saved = (yearly_salary / 12.0) * portion_saved
amt_saved = 0
monthly_return = first_month_saved * (r / 12)

months = 0
while amt_saved <= down_payment_amount:
    amt_saved += first_month_saved + monthly_return
    monthly_return = amt_saved * (r / 12)
    months += 1


print('number of months: ', months)

