class florist:
    def __init__(self, florist_list=None):
        if florist_list is None:
            florist_list = []
        self.florist = florist_list

    def add_florist(self,n):
        '''add more florist'''
        if n>0:
            for i in range(n):
                name = input('Please input florist name (one at a time)')
                self.florist.append(name)
        else:
            pass

    def rem_florist(self,n):
        '''remove existed florists'''
        if n>0:
            for i in range(n):
                name = input('Please input florist name (one at a time)')
                if name in self.florist:
                    self.florist.remove(name)
                else:
                    raise ValueError("We don't have this florist")
        else:
            pass