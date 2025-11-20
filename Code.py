# a shop has a balance, a production
import numpy as np

class shop:
    '''
    period means the number of months to run the simulation
    balance = default balance - costs
    productivity = {type of bouquets: quantity}
    '''
    def __init__(self,target):
        self.employee = len(self.flourists)
        self.target = target
        self.flourists = ['Jack']

    def add_flourist(self, name):
        '''add more flourist'''
        self.flourists.append(name)

    def rem_flourists(self,name):
        '''remove existed flourists'''
        if name in self.flourists:
            self.flourists.remove(name)
    
    def operation(self, selling_price, target,supplies_cost,rent=800):
        '''simulate one-month's operation'''
        earning = target * selling_price
        salary = len(self.flourists)*15.5*80
        expenditure = rent + salary + supplies_cost
        money_flow = earning - expenditure
        self.balance += money_flow
    
    def check(self,time_cons,expenditure):
        '''
        Check if the target can be achieved
        labor constraint, money constraint
        '''
        
        q = self.target
        q = np.array(q.values)
        Total_time = q * np.array(time_cons.values)
        Time_check = (Total_time>len(self.flourists)*80)
        Money_check = self.balance>expenditure
        assert not Time_check and not Money_check, f'Time_check{Time_check}, Budget{Money_check}'
        pass


class bouquet:
    '''
    
    '''
    import numpy as np
    def __init__(self, type, quantity):
        self.quantity = quantity
        self.type = type
        self.labour_consump=0
        self.supplies_consump = {'rose':0,'Daisies':0,'Greenery':0}
        self.quantity = quantity


    def labour_consumption(self,time_cons):
        if self.type in time_cons.keys():
            self.labour_consump += time_cons[self.type] *self.quantity
        else:
            print('type errors')


    def supplies_consumption(self,price):
        '''
        This function calculate the minimun quantity of supplies and supplies fee
        when satisfying the target.这个函数计算出在满足每月销售目标的条件下，每种花的最低进货量以及最低成本
        '''
        if self.type == 'Fern-tastic':
            self.supplies_consump = [self.quantity * 0,self.quantity * 2,self.quantity * 4]

        elif self.type == 'Be-Leaf in Yourself':
            self.supplies_consump = [self.quantity * 1,self.quantity * 3,self.quantity * 2]

        elif self.type == 'You Rose to the Occasion':
            self.supplies_consump = [self.quantity * 4, self.quantity * 2, self.quantity * 2]

        else:
            print('type errors')

        self.supplies_fee = self.supplies_consump * price #


    def bouquet_cost(self):
        self.supplies_consumption=0



'''
class supplies:
    def __init__(self, type, vendor,quantity):
        self.type = type
        self.vendor = vendor
        self.cost = 0
        self.quantity = quantity
    def cost(self):
        self.cost += vendors[self.vendor][self.type] * self.quantity
    #def price(self):
'''
        























'''
Evergreen_Essentials = {'rose':2.8,'Daisies':1.5,'Greenery':0.95}
FloraGrow_Distributors = {'rose':1.6,'Daisies':1.2,'Greenery':1.8}
vendors = {'Evergreen_Essentials':Evergreen_Essentials,'FloraGrow_Distributors':FloraGrow_Distributors}
'''