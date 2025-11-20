# a shop has a balance, a production
import numpy as np

class florist:
    def __init__(self,name):
        self.name = name        

class shop:
    '''
    period means the number of months to run the simulation
    balance = default balance - costs
    productivity = {type of bouquets: quantity}
    '''
    def __init__(self,target):
        self.target = np.array(target)
        self.florists = []
        self.salary = 15.5 # only one florist hired by default
        self.max_working = 80

    def add_florist(self, name):
        '''add more florist'''
        self.florists.append(name) 
        number = len(self.florists)
        self.number = number
        self.salary = 15.5 * number
        self.max_working = 80 * number

    def rem_florists(self,name):
        '''remove existed florists'''
        if name in self.florists:
            self.florists.remove(name)
            number = len(self.florists)
            self.number = number 
            self.salary = 15.5 * number *80
    
    def operation(self):
        '''simulate one-month's operation'''        
        selling_price = np.array([18.5,17.5,32.5]) # 1x3        
        earning = np.dot(self.target,selling_price.reshape(3,1))       
        self.income = earning
        print(f'Get Income Calculation Done!\n Income is {self.income[0]}')
    
    def check(self,time_cons,expenditure):
        '''
        Check if the target can be achieved
        labor constraint, money constraint
        '''
        
        q = self.target
        q = np.array(q.values)
        Total_time = q * np.array(time_cons.values)
        Time_check = (Total_time>len(self.florists)*80)
        Money_check = self.balance>expenditure
        assert not Time_check and not Money_check, f'Time_check{Time_check}, Budget{Money_check}'
        pass


class bouquet:
    '''
    
    '''
    import numpy as np
    def __init__(self, quantity,demand=[175,100,250]):        
        if any(q > d for q, d in zip(quantity, demand)):
            print('warning: your target is greater than the market demand')
        else:
            print('target check finished!')
        print('-------------------')
        self.quantity = np.array(list(quantity))

    def labour_consumption(self,time_cons):
        if self.type in time_cons.keys():
            self.labour_consump += time_cons[self.type] *self.quantity
        else:
            print('type errors')

    def bouquet_quan(self):
        '''
        This function calculate the minimun quantity of supplies and supplies fee
        when satisfying the target.这个函数计算出在满足每月销售目标的条件下，每种花的最低进货量以及最低成本
        '''       
        # setting
        price = np.array([1.6,1.2,0.95])
        making_time = np.array([1/3,1/2,3/4])
        composition=np.array([[4,0,2],[2,1,3],[2,4,2]])
        total_time = np.dot(making_time,self.quantity)
        self.total_making_time = total_time
        quant = np.dot(self.quantity,composition) # 1x3 矩阵       
        price = price.reshape(3,1)
        fees = np.dot(quant,price)
        self.flower_fee = fees # cash_flow
        self.quant = quant # [rose,daises,greenery]consume

    def repleinishment(self):
        depreciation_rate = np.array([0.4,0.15,0.5]) # rose, daises and greenery
        capacity = np.array([200,250,400])
        # remains<0 demonstrating that current target exceeds supplies
        remains = capacity-self.quant #余量 1x3 
        greenhouse_cost = np.array([1.5,0.8,0.2])
        greenhouse_cost = greenhouse_cost.reshape(3,1)
        total_greenhouse_cost = np.dot(remains,greenhouse_cost)
        self.greenhouse_cost = total_greenhouse_cost # 3x1
        remains = remains*(1-depreciation_rate)
        #repleinishment_fee
        vendor_price = np.array([1.6,1.2,0.95]) # rose, daises and greenery
        vendor_price = vendor_price.reshape(3,1)
        repleinish_quant = capacity - remains
        replenish_cost = np.dot(repleinish_quant,vendor_price)
        self.replenish_cost = replenish_cost

        
class greenhouse:
    def __init__(self,capacity):
        capacity = np.array(capacity)
        self.capacity_limit = capacity        
    def store(self,remains):
        pass























'''
Evergreen_Essentials = {'rose':2.8,'Daisies':1.5,'Greenery':0.95}
FloraGrow_Distributors = {'rose':1.6,'Daisies':1.2,'Greenery':1.8}
vendors = {'Evergreen_Essentials':Evergreen_Essentials,'FloraGrow_Distributors':FloraGrow_Distributors}
'''