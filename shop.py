import numpy as np
import florist as fl

class shop:
    """
    Flower shop class, manages employees and business operations.
    """
    salary_normal = 15.5
    salary_senior = 20.0 
    working_hour = 80
    
    def __init__(self):
        self.florist = []  # Employee list

    def input_florist(self):
        """
        Input employee information
        """
        while True:
            try:
                print('Current number of florists:', len(self.florist))
                add_num = int(input('How many florists do you want to add this month? '))
                # Try add/remove operations on a copy of the current florist list.
                # If any check fails, discard this modification so the original list stays unchanged.
                florist1 = fl.florist(self.florist.copy())
                florist1.add_florist(add_num)
                
                rem_num = int(input('How many florists do you want to remove this month? '))
                florist1.rem_florist(rem_num)
                # Check if there are duplicate florist names
                names = [emp['name'] for emp in florist1.florist]
                if len(names) != len(set(names)):
                    # Find all duplicate names for clearer error messages
                    from collections import Counter
                    counter = Counter(names)
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
        """
        Check if the number of employees is within valid range.
        Args:
            florist_list: Employee list to check
        """
        if florist_list is None:
            florist_list = self.florist
        number = len(florist_list)
        if number < 1:
            raise ValueError('You should have at least one florist')
        elif number > 4:
            raise ValueError("You shouldn't have more than 4 florists")
        return
    

    def process_input_florist(self):
        """
        Process employee input and calculate total salary.
        Returns:
            (employee list, total salary)
        """
        self.input_florist()
        print('Florists confirmed! 🎉')
        self.number = len(self.florist)
        
        # Calculate total salary
        total_salary = 0
        for emp in self.florist:
            if emp['salary_level'] == 'senior':
                total_salary += self.salary_senior * self.working_hour
            else:
                total_salary += self.salary_normal * self.working_hour
        
        return self.florist, total_salary

    def operation(self, target):
        """
        Simulate one month's operations and calculate income.
        If there is a senior manager, all bouquet prices increase by 50%.
        Args:
            target: [Fern-tastic, Be-Leaf in Yourself, You Rose to the Occasion]
        """
        selling_price = np.array([18.5, 17.5, 32.5])
        
        # Check if there is a senior manager, if yes increase prices by 50%
        has_senior = any(emp['salary_level'] == 'senior' for emp in self.florist)
        if has_senior:
            selling_price = selling_price * 1.5
            print('Senior manager bonus: All bouquet prices increased by 50%!')
        
        earning = np.dot(target, selling_price.reshape(3, 1))       
        self.income = earning
        print(f'Calculating total income!\n Income is {self.income[0]}')
    
