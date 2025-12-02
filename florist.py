class florist:
    """
    Class for managing florist employee information.
    Each employee contains: name, specialization type (0=Fern-tastic, 1=Be-Leaf in Yourself, 2=You Rose to the Occasion, None=no specialization),
    salary level ('normal'=15.5/hour, 'senior'=20/hour)
    """
    def __init__(self, florist_list=None):
        """
        Initialize the employee list.
        Args:
            florist_list: List of employees{'name': str, 'specialization': int/None, 'salary_level': str}
        """
        if florist_list is None:
            florist_list = []
        self.florist = florist_list

    def add_florist(self, n):
        """
        Add new employees.
        Args:
            n: Number of employees to add
        """
        if n > 0:
            for i in range(n):
                name = input('Please input florist name (one at a time): ')
                # specialization type
                print(f'\nSet specialization for {name} (specialization allows employees to make specific bouquets in half the time):')
                print('0 = Fern-tastic')
                print('1 = Be-Leaf in Yourself')
                print('2 = You Rose to the Occasion')
                print('Press Enter to skip = No specialization')
                spec_input = input('Please enter specialization type (0/1/2/Enter): ').strip()
                specialization = None
                if spec_input in ['0', '1', '2']:
                    specialization = int(spec_input)
                
                # salary level
                print(f'\nSet salary level for {name}:')
                print('n = Normal employee (£15.5/hour)')
                print('s = Senior manager (£20/hour, increases all bouquet prices by 50%)')
                salary_input = input('Please enter salary level (n/s, default n): ').strip().lower()
                salary_level = 'senior' if salary_input == 's' else 'normal'
                
                employee = {
                    'name': name,
                    'specialization': specialization,
                    'salary_level': salary_level
                }
                self.florist.append(employee)
        else:
            pass

    def rem_florist(self, n):
        """
        Remove existing employees.
        Args:
            n: Number of employees to remove
        """
        if n > 0:
            for i in range(n):
                name = input('Please input florist name (one at a time): ')
                # Find and remove employee
                found = False
                for emp in self.florist:
                    if emp['name'] == name:
                        self.florist.remove(emp)
                        found = True
                        break
                if not found:
                    raise ValueError("We don't have this florist")
        else:
            pass
    
    def get_names(self):
        """
        Get list of all employee names.
        Returns:
            List of employee names
        """
        return [emp['name'] for emp in self.florist]
    
    def has_senior_manager(self):
        """
        Check if there is a senior manager.
        Returns:
            bool: True if there is a senior manager, False otherwise
        """
        return any(emp['salary_level'] == 'senior' for emp in self.florist)