import random

class warZone:
    def __init__(self, n_row, n_column):        
        self.n_row = row
        self.n_column = n_column
        self.war_zone = self.init_war_zone()
        self.other_war_zone = self.init_war_zone()
    
    def init_war_zone(self):
        matrix = []
        for row in range(self.n_row):
            matrix.append(["-"]*self.n_column)
        return matrix
    
