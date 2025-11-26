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
    def __init__(self):
        self.florists = []
        self.salary = 15.5 # only one florist hired by default
        self.max_working = 80

    def add_florist(self, a, name):
        '''add more florist'''
        self.florists.append(name)
        number = len(self.florists)
        self.number = number
        self.salary = 15.5 * number
        self.max_working = 80 * number

    def rem_florist(self,name):
        '''remove existed florists'''
        if name in self.florists:
            self.florists.remove(name)
            number = len(self.florists)
            self.number = number 
            self.salary = 15.5 * number *80
    
    def florist(self,a):
        if a<0:
            names = [input('which florist do you want to remove') for i in range(-a)]
            for name in names:
                self.rem_florist(name)

        elif a==0:
            return

    def operation(self,target):
        '''simulate one-month's operation'''        
        selling_price = np.array([18.5,17.5,32.5]) # 1x3        
        earning = np.dot(target,selling_price.reshape(3,1))       
        self.income = earning
        print(f'Calculating total income!\n Income is {self.income[0]}')
    
    def procee(self):
        '''
        working as a pipeline and mornitoring the whole class
        '''
        ans = input('Add or not?')
        name1 = input('')
        self.add_florist()
        name2 = input()
        self.rem_florists()
        
class vendor:
    Evergreen = [2.8,1.5,0.95]
    FloraGrow = [1.6,1.2,1.8]
    vendor_price = [Evergreen,FloraGrow]
    def price(self,type1,type2,type3):
        rose_price = self.vendor_price[type1][0]
        daisies_price = self.vendor_price[type2][1]
        greenery_price = self.vendor_price[type3][2]
        return [rose_price,daisies_price,greenery_price]

    
    def choose_vendor(self):
        rose = input('Do you want to purchase roses from Evergreen Essentials (0), or FloraGrow Distributors (1)?')
        daisies= input('Do you want to purchase daisies from Evergreen Essentials (0), or FloraGrow Distributors (1)?')
        greenery = input('Do you want to purchase roses from Evergreen Essentials (0), or FloraGrow Distributors (1)?')
        return rose,daisies,greenery

    def vendor_price(self):
        rose,daisies,greenery = self.choose_vendor()
        return self.price(rose,daisies,greenery)
            
class bouquet:
    price = np.array([1.6,1.2,0.95]).reshape(3,1)
    making_time = np.array([1/3,1/2,3/4])
    composition=np.array([[0,2,4],[1,3,2],[4,3,2]])
    capacity = np.array([200,250,400])
    depreciation_rate = np.array([0.4,0.15,0.5]) # rose, daises and greenery
    greenhouse_cost = np.array([1.5,0.8,0.2]).reshape(3,1)

    def __init__(self, quantity,demand=[175,100,250]):        
        if any(q > d for q, d in zip(quantity, demand)):
            raise ValueError("Your target is greater than the market demand")
        else:
            print('\n target check finished!\n')
        self.quantity = np.array(list(quantity))

    def compute_fee(self):
        quant = np.dot(self.quantity,self.composition)
        remains = self.capacity-quant
        total_greenhouse_cost = np.dot(remains,self.greenhouse_cost)
        self.greenhouse_cost = total_greenhouse_cost
        remains = remains*(1-self.depreciation_rate)

        return
            
    def operation(self):
        '''
        This function calculate the minimun quantity of supplies and supplies fee
        when satisfying the target.这个函数计算出在满足每月销售目标的条件下，每种花的最低进货量以及最低成本
        '''       
        # setting
        price = np.array([1.6,1.2,0.95])
        making_time = np.array([1/3,1/2,3/4])
        composition=np.array([[0,2,4],[1,3,2],[4,3,2]])
        total_time = np.dot(making_time,self.quantity)
        self.total_making_time = total_time
        quant = np.dot(self.quantity,composition) # 1x3 矩阵       
        price = price.reshape(3,1)
        fees = np.dot(quant,price)
        self.flower_fee = fees # cash_flow
        self.quant = quant # [rose,daises,greenery]consume

    def repleinishment(self,vendor_price):
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
        vendor_price = vendor_price # rose, daises and greenery
        vendor_price = vendor_price.reshape(3,1)
        repleinish_quant = capacity - remains
        replenish_cost = np.dot(repleinish_quant,vendor_price)
        self.replenish_cost = replenish_cost
