# import packages
import numpy as np
import flower_shop as fs

# initial setting
target = {'Fern-tastic':29,'Be-Leaf in Yourself':10,'You Rose to the Occasion':10}
target_quantity = list(target.values()) # 1x3 矩阵
making_time = {'Fern-tastic':1/3,'Be-Leaf in Yourself':1/2,'You Rose to the Occasion':3/4}
bouquet_demand = [175,100,250] # Fern-tastic, be-leaf in yourself and you rose to the occasion
greenhouse_cost = [1.5,0.8,0.2] # rose, daises and greenery
capacity_limit = [200,250,400] # rose, daises and greenery
composition = np.array([[4,0,2],[2,1,3],[2,4,2]])
wage_rate = 15.5
florist0 = fs.florist('Mike')
rent = 800
balance = 7500

# set a shop configuration
shop1 = fs.shop(target_quantity) # default running period is 6
florist1 = fs.florist('Jack')
florist2= fs.florist('John')

# add/remove florist and calculate the number of florists
shop1.add_florist([florist1,florist2])
shop1.rem_florists(florist2)
print(f'The number of existing florist is {shop1.number}')
# calculate the salary expenditure
salary = shop1.salary

# Automatically check if the target is technically allowed
# making sure the target quantity is within the market demand range
bouquet1 = fs.bouquet(target_quantity) 

# according to the selling target, calculate the fees, quant and total_making_time
bouquet1.bouquet_quan()
fees = bouquet1.flower_fee # cash flow
quant = bouquet1.quant # 1x3
total_making_time = bouquet1.total_making_time
print(f'ingrediant fee is {fees}')
print(f'required amount of ingrediant is{quant} perspectively')
print(f'required working hour is {total_making_time}h')

bouquet1.repleinishment()
total_greenhouse_cost = bouquet1.greenhouse_cost
total_replenish_cost = bouquet1.replenish_cost
total_cost = total_greenhouse_cost + total_replenish_cost + salary + rent
print('total_greenhouse_cost', total_greenhouse_cost[0])
print('total_replenish_cost', total_replenish_cost[0])
print('total_cost =',total_cost[0])
print('-------------------')


# calculate the income
shop1.operation()
income = shop1.income
balance = balance- income - total_cost
balance = balance[0]
print('-------------------')
print('Complete Operation within one month!')
print('balance is', balance)

