# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 02:10:39 2023

@author: ma228
"""


annual_salary = float(input('Enter the starting salary:'))

minimum_saving_rate = 0
maximum_saving_rate = 10000
best_saving_rate = 1



total_cost = 1000000
portion_down_payment = 0.25 *total_cost
semi_annual_raise = 0.07
r=0.04 #annual_rate

steps_in_bisection_search = 0

is_best_saving_found = False

while(not is_best_saving_found):
    
    current_saving = 0 
    number_of_months = 0
    monthly_salary = annual_salary/12
    monthly_portion_saved = best_saving_rate * monthly_salary
    
    for i in range(36):
        current_saving += (current_saving*(r/12) + monthly_portion_saved)
        number_of_months += 1
        if(number_of_months%6 == 0):  
            monthly_salary += (semi_annual_raise* monthly_salary)
            monthly_portion_saved = best_saving_rate * monthly_salary
            
    if(best_saving_rate == 1 and current_saving<portion_down_payment):
        break
    
    
    if(abs(current_saving-portion_down_payment) <= 100):
        is_best_saving_found = True
    elif(current_saving>portion_down_payment):
        maximum_saving_rate = best_saving_rate * 10000
    else:
        minimum_saving_rate = best_saving_rate * 10000
        
    if(best_saving_rate != 1):
        steps_in_bisection_search += 1
    
    best_saving_rate = ((minimum_saving_rate+maximum_saving_rate)//2)/10000 
    
    
    
    
    
    
if(current_saving<portion_down_payment):
    print('It is not possible to pay the down payment in three years.')
else:
    print('Best savings rate:',best_saving_rate)
    print('Steps in bisection search:',steps_in_bisection_search)      
