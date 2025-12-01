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
                # Try add/remove operations on a copy of the current florist list.
                # If any check fails, discard this modification so the original list stays unchanged.
                florist1 = fl.florist(self.florist.copy())
                florist1.add_florist(add_num)
                
                rem_num = int(input('How many florists do you want to remove this month?'))
                florist1.rem_florist(rem_num)
                # Check if there are duplicate florist names
                if len(florist1.florist) != len(set(florist1.florist)):
                    # Find all duplicate names for clearer error messages
                    from collections import Counter
                    counter = Counter(florist1.florist)
                    dup = {name for name, cnt in counter.items() if cnt > 1}
                    raise ValueError(f"Florist name already exists: {dup}")

                # First check upper and lower bounds on the "candidate" list
                self.check(florist1.florist)

                # Only after all checks pass, update the shop's florist list
                self.florist = florist1.florist
                # At this point len(self.florist) is the latest number of florists
                return 
            
            except ValueError as e:
                print(f"Warning: {e}")
                print('Please try again.\n')

    def check(self, florist_list=None):
        if florist_list is None:
            florist_list = self.florist
        number = len(florist_list)
        if number < 1:
            raise ValueError('You should have at least one florist')
        elif number >4:
            raise ValueError("You shouldn't have more than 4 florists")
        return
    

    def process_input_florist(self):
        self.input_florist()
        print('Florists confirmed! 🎉')
        self.number = len(self.florist)
        salary = self.number * self.salary * self.working_hour
        return self.florist, salary

    def operation(self,target):
        '''simulate one-month's operation'''        
        selling_price = np.array([18.5,17.5,32.5]) # 1x3        
        earning = np.dot(target,selling_price.reshape(3,1))       
        self.income = earning
        print(f'Calculating total income!\n Income is {self.income[0]}')
    
