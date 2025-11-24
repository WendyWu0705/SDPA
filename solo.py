# import packages
import flower_shop as fs
import code_1 as fc


def one_run(balance):
    # set and show a shop configuration
    florist0 = fs.florist('Mike')
    rent = 800
    shop1 = fs.shop() # default running period is 6
    shop1.add_florist(florist0)
    print('Initial Florist is:')
    print([florist_name.name for florist_name in shop1.florists])

    # add/remove florist and calculate the number of florists
    print('Do you want to add/remove florists?')
    #florist1 = fs.florist('Jack')
    florist2= fs.florist('John')
    # 目前只能一个一个加，之后可以一个列表加
    #shop1.add_florist(florist1)
    shop1.add_florist(florist2)
    shop1.rem_florists(florist2)
    print('In this month we have listed florists working in our shop:')
    print([florist_name.name for florist_name in shop1.florists])
    print(f'The number of existing florists is {shop1.number}')
    # calculate the salary expenditure
    salary = shop1.salary

    # Automatically check if the target is technically allowed
    # making sure the target quantity is within the market demand range
    # labor_constraint_check
    # capacity check

    bouquet1 = fc.Target(shop1.number)
    bouquet1 = bouquet1.process()
    # according to the selling target, calculate the fees, quant and total_making_time

    bouquet1.bouquet_quan()


    fees = bouquet1.flower_fee # cash flow
    quant = bouquet1.quant # 1x3
    total_making_time = bouquet1.total_making_time
    #print(f'ingrediant fee is {fees}',end='\n')
    #print(f'required amount of ingrediant is{quant} perspectively',end='\n')
    #print(f'required working hour is {total_making_time}h',end='\n')


    bouquet1.repleinishment()
    total_greenhouse_cost = bouquet1.greenhouse_cost
    total_replenish_cost = bouquet1.replenish_cost
    total_cost = total_greenhouse_cost + total_replenish_cost + salary + rent
    #print('salary=', salary)
    #print('total_greenhouse_cost', total_greenhouse_cost[0],end='\n')
    #print('total_replenish_cost', total_replenish_cost[0],end='\n')
    #print('total_cost =',total_cost[0],end='\n')
    #print('-------------------')


    # calculate the income
    shop1.operation(bouquet1.quantity)
    income = shop1.income
    balance = balance + income - total_cost
    balance = balance[0]
    print('-------------------')
    print('Complete Operation within one month!')
    print('balance is', balance)
    return balance

