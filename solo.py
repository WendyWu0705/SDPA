# import packages
import flower_shop as fs
import check_status as cs
import shop as sh


def one_run(balance,shop1):
    print('Before the month starts, there are some owner actions for you to carry out.' \
    ' First, review the number of staff, then decide how many bouquets to sell.')
    
    # add/remove florist and calculate the number of florists
    rent = 800
    shop1 = shop1
    florist, salary= shop1.process_input_florist()
    print('Current Staff:\n',[florist_name for florist_name in florist])

    # Automatically check if the target is technically allowed
    # making sure the target quantity is within the market demand range
    # labor_constraint_check
    # capacity check

    bouquet1 = cs.Target(shop1.number) # bouquet1 represents the production/sales target
    bouquet1 = bouquet1.process()
    # according to the selling target, calculate the fees, quant and total_making_time


    # compute cost and fees
    bouquet1.operation() 
    vendor = fs.vendor()
    vendor_price = vendor.Vendor_price()
    fees = bouquet1.flower_fee # cash flow
    quant = bouquet1.quant # 1x3
    total_making_time = bouquet1.total_making_time
    print(f'ingrediant fee is {fees}',end='\n')
    print(f'required amount of ingrediant is{quant} perspectively',end='\n')
    print(f'required working hour is {total_making_time}h',end='\n')


    bouquet1.repleinishment(vendor_price)
    total_greenhouse_cost = bouquet1.greenhouse_cost
    total_replenish_cost = bouquet1.replenish_cost
    total_cost = total_greenhouse_cost + total_replenish_cost + salary + rent
    print('salary=', salary)
    print('total_greenhouse_cost', total_greenhouse_cost[0],end='\n')
    print('total_replenish_cost', total_replenish_cost[0],end='\n')
    print('total_cost =',total_cost[0],end='\n')
    print('-------------------')


    # calculate the income
    starting_balance = balance
    shop1.operation(bouquet1.quantity)
    income = shop1.income
    balance = balance + income - total_cost
    balance = balance[0]

    # Monthly summary: cash flow, greenhouse inventory and staff
    print('-------------------')
    print('Monthly summary')
    print(f'Starting balance: {starting_balance}')
    print(f'Total income from sales: {income[0]}')
    print(f'Flower purchase cost (cash flow): {fees[0]}')
    print(f'Greenhouse operating cost: {total_greenhouse_cost[0]}')
    print(f'Replenishment cost: {total_replenish_cost[0]}')
    print(f'Staff salary cost: {salary}')
    print(f'Rent cost: {rent}')
    print(f'Net cash flow this month: {(income - total_cost)[0]}')
    print(f'Ending balance: {balance}')

    # Greenhouse stock situation (after depreciation)
    if hasattr(bouquet1, "remains"):
        # remains is a 1x3 array: [roses, daisies, greenery]
        remaining_stock = bouquet1.remains
        print('Greenhouse remaining stock after depreciation (roses, daisies, greenery):')
        print(remaining_stock)

    # Staff situation
    print('Staff situation at the end of the month:')
    print(f'Number of florists: {shop1.number}')
    print('Florist names:', shop1.florist)

    print('-------------------')
    print('Complete operation within one month!')
    print('Balance is', balance)
    if balance <= 0:
        print('Your shop is bankrupted')
        exit()
    return balance, shop1

