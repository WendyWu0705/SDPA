import numpy as np
import flower_shop as fs

class Target:
    composition=np.array([[0,2,4],[1,3,2],[4,3,2]])
    capacity =  np.array([200,250,400])
    working_hour = 80
    
    def __init__(self,num_of_florist):
        self.bouquet = None
        self.target = None
        self.num_of_florist = num_of_florist


    def input_quantity(self):
        while True:
            try:
                target_Fern = int(input('How many Fern-tastic do you want to sell today? '))
                target_Beleaf = int(input('How many Be-Leaf in Yourself do you want to sell today? '))
                target_YR = int(input('How many You Rose to the Occasion do you want to sell today? '))
                target = [target_Fern,target_Beleaf,target_YR]   
                bouquet = fs.bouquet(target)
                making_time = np.array([1/3,1/2,3/4])
                total_time = np.dot(making_time,np.array(target))
                self.total_making_time = total_time
                self.bouquet = bouquet
                self.target = target 
                return          
            
            except ValueError as e:
                print(f"Warning: {e}")
                print("Please try again.\n")

        

    def check_capacity(self):
        while True:
            try:
                quant = np.dot(self.target,self.composition)
                remains = self.capacity - quant
                if (remains >= 0).all():
                    print('Capacity check passed!\n')
                    return
                else:  
                    print('Insufficient supplies:',quant)
                    raise ValueError("Not sufficient supplies")
                
            except ValueError as e:
                print(f"Warning: {e}")
                print("Please try again.\n")
                self.input_quantity()
                
                

    def labour_check(self):
        while True:    
            try:
                if self.total_making_time<=self.num_of_florist*80:
                    print('labor check passed!\n')
                    return 
                else:
                    if self.total_making_time//80<=4:
                        print(f'you need {(self.total_making_time-self.num_of_florist*80)//80+1} more florists')
                        raise ValueError("Not enough labour capacity")
                    else:
                        print('Selling target is impossible! Please reset it.')
                        raise ValueError("Impossible Mission.")
            
            except ValueError as e:
                print(f"Warning: {e}")
                print("Please try again.\n")
                self.input_quantity()
    def process(self):
        self.input_quantity()
        self.check_capacity()
        self.labour_check()
        print("Order confirmed! 🎉")
        return self.bouquet