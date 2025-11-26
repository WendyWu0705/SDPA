# import packages
import flower_shop as fs
import check_status as cs
import shop as sh


def one_run(balance):
    print('Before the month starts, there are some owner actions for you to carry out.' \
    ' First, review the number of staff, then decide how many bouquets to sell.')
    
    # add/remove florist and calculate the number of florists
    rent = 800
    shop1 = sh.shop()
    florist, salary= shop1.process_input_florist()
    print('Current Staff:\n',[florist_name for florist_name in florist])

    # Automatically check if the target is technically allowed
    # making sure the target quantity is within the market demand range
    # labor_constraint_check
    # capacity check

    bouquet1 = cs.Target(shop1.number) #bouquet1指生产/销售目标
    bouquet1 = bouquet1.process()
    # according to the selling target, calculate the fees, quant and total_making_time


    # compute cost and fees
    bouquet1.operation() 
    vendor = fs.vendor()
    vendor_price = vendor.vendor_price
    fees = bouquet1.flower_fee # cash flow
    quant = bouquet1.quant # 1x3
    total_making_time = bouquet1.total_making_time
    #print(f'ingrediant fee is {fees}',end='\n')
    #print(f'required amount of ingrediant is{quant} perspectively',end='\n')
    #print(f'required working hour is {total_making_time}h',end='\n')


    bouquet1.repleinishment(vendor_price)
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
    return balance, shop1

