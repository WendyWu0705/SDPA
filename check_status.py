import numpy as np
import flower_shop as fs

class Target:
    """
    Class for managing order targets and checks.
    Supports specialization: specialized employees take half the time to make their specialized bouquets.
    """
    composition = np.array([[0,2,4],[1,3,2],[4,3,2]])
    capacity = np.array([200,250,400])
    working_hour = 80
    
    def __init__(self, num_of_florist, florist_list=None):
        """
        Initialize the Target class.
        Args:
            num_of_florist: Number of florists
            florist_list: List of florists, each is a dictionary containing specialization information
        """
        self.bouquet = None
        self.target = None
        self.num_of_florist = num_of_florist
        self.florist_list = florist_list if florist_list is not None else []

    def calculate_making_time(self, target):
        """
        Calculate the total time required to make bouquets, considering specialization.
        If an employee specializes in a bouquet type, they take half the time to make that bouquet.
        
        For each bouquet type, prioritize specialized employees, with remaining work
        completed by all employees (including specialized ones).
        Args:
            target: Target bouquet quantities [Fern-tastic, Be-Leaf in Yourself, You Rose to the Occasion]
        Returns:
            float: Total making time (hours)
        """
        making_time_base = np.array([1/3, 1/2, 3/4])  # Base making time (hours per bouquet)
        target_array = np.array(target)
        
        # Count specialized employees for each bouquet type
        specialized_count = [0, 0, 0]  # [Fern-tastic specialized, Be-Leaf specialized, You Rose specialized]
        for emp in self.florist_list:
            if emp.get('specialization') is not None:
                spec = emp['specialization']
                if 0 <= spec <= 2:
                    specialized_count[spec] += 1
        
        # Calculate time needed for each bouquet type
        times_per_bouquet_type = []
        
        for bouquet_type in range(3):  # 0=Fern, 1=Be-Leaf, 2=You Rose
            quantity = target_array[bouquet_type]
            if quantity == 0:
                continue
                
            base_time_per_bouquet = making_time_base[bouquet_type]
            specialized_workers = specialized_count[bouquet_type]
            total_workers = self.num_of_florist
                      
            # Capacity of specialized workers per hour (time is halved)
            specialized_capacity_per_hour = specialized_workers * (2.0 / base_time_per_bouquet)
            
            # Capacity of non-specialized workers per hour
            normal_workers = total_workers - specialized_workers
            normal_capacity_per_hour = normal_workers * (1.0 / base_time_per_bouquet)
            
            # Total capacity
            total_capacity_per_hour = specialized_capacity_per_hour + normal_capacity_per_hour
            

            time_needed = quantity / total_capacity_per_hour
            times_per_bouquet_type.append(time_needed)


        return max(times_per_bouquet_type)

    def input_quantity(self):
        """
        Input bouquet sales quantities and calculate making time.
        """
        while True:
            try:
                target_Fern = int(input('How many Fern-tastic do you want to sell today? '))
                target_Beleaf = int(input('How many Be-Leaf in Yourself do you want to sell today? '))
                target_YR = int(input('How many You Rose to the Occasion do you want to sell today? '))
                target = [target_Fern, target_Beleaf, target_YR]   
                bouquet = fs.bouquet(target)
                
                # Use new calculation method which takes specialization into account
                total_time = self.calculate_making_time(target)
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
                total_available_hours = self.num_of_florist * self.working_hour
                if self.total_making_time <= total_available_hours:
                    print('labor check passed!\n')
                    return 
                else:
                    # Calculate how many more employees are needed
                    additional_hours_needed = self.total_making_time - total_available_hours
                    additional_workers_needed = int(np.ceil(additional_hours_needed / self.working_hour))
                    
                    if self.num_of_florist + additional_workers_needed <= 4:
                        print(f'you need {additional_workers_needed} more florist(s)')
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