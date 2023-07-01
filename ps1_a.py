# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 12:52:09 2023

@author: ma228
"""

annual_salary = float(input('Enter your annual salary:'))
monthly_salary = annual_salary/12
portion_saved = float(input('Enter the monthly percent of your salary to save, as a decimal:'))
monthly_portion_saved = portion_saved * monthly_salary
total_cost = float(input('Enter the cost of your dream home:'))

portion_down_payment = 0.25 *total_cost
current_saving = 0 
number_of_months = 0
r=0.04 #annual_rate

while(current_saving<portion_down_payment):
    current_saving += (current_saving*(r/12) + monthly_portion_saved)
    number_of_months += 1
print('Number of months:',number_of_months)
