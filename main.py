import numpy as np
import code as cd
target = {'Fern-tastic':20,'Be-Leaf in Yourself':100,'You Rose to the Occasion':20}
time_cons = {'Fern-tastic':1/3,'Be-Leaf in Yourself':1/2,'You Rose to the Occasion':3/4}


shop1 = cd.shop(target)
price = [1.6,1.2,0.95] #自己设置选每种最便宜的进货
selling_price  = [18.5,17.5,32.5]


bouquet1 = cd.bouquet('Fern-tastic',100)
bouquet1.supplies_consumption(price)
supplies_fee = bouquet1.supplies_fee

supplies_cons = bouquet1.supplies_consump

profit = shop1.profits(selling_price=selling_price,productivity=target,supplies_cost=supplies_fee)
balance = shop1.balance

rose_cons = supplies_cons['rose']
rose_supplies = cd.supplies('rose','FloraGrow_Distributors',rose_cons)
rose_supplies_cost = rose_supplies.cost
