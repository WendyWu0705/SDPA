import numpy as np
import florist as fl

class shop:
    salary = 15.5
    working_hour = 80
    def __init__(self):
        self.florist = []

    def input_florist(self):
        while True:
            try:
                print('Current number of florists:',len(self.florist))
                add_num = int(input('How many florists do you want to add this month?'))
                florist1 = fl.florist()
                florist1.add_florist(add_num)
                rem_num = int(input('How many florist do you want to remove this month?'))
                florist1.rem_florist(rem_num)
                self.florist = florist1.florist
                self.check()
                
                return 
            
            except ValueError as e:
                print(f"Warning: {e}")
                print('Please try again.\n')

    def check(self):
        number = len(self.florist)
        if number < 1:
            raise ValueError('You should have at least one florist')
        return

    def process_input_florist(self):
        self.input_florist()
        print('Florists confirmed! 🎉')
        self.number = len(self.florist)
        salary = self.number * self.salary
        return self.florist, salary

    def operation(self,target):
        '''simulate one-month's operation'''        
        selling_price = np.array([18.5,17.5,32.5]) # 1x3        
        earning = np.dot(target,selling_price.reshape(3,1))       
        self.income = earning
        print(f'Calculating total income!\n Income is {self.income[0]}')
    
