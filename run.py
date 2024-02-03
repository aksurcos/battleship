import random

class warZone:
    def __init__(self, n_row, n_column):        
        self.n_row = n_row
        self.n_column = n_column
        self.war_zone = self.init_war_zone()
        self.other_war_zone = self.init_war_zone()
    
    def init_war_zone(self):
        matrix = []
        for row in range(self.n_row):
            matrix.append(["o"]*self.n_column)
        return matrix

    def __str__(self):
        our_war_zone = self.create_war_zone(self.war_zone)
        other_war_zone = self.create_war_zone(self.other_war_zone)

        our_war_zone_list = our_war_zone.split("\n")
        other_war_zone_list = other_war_zone.split("\n")
        more_character = len(str(self.n_column)) - 1
        other_war_zone_list[0] = other_war_zone_list[0][more_character:]
        
        war_zone_str = [(10*" ").join([me, other])
                        for me, other in zip(our_war_zone_list, other_war_zone_list)]
        return "\n".join(war_zone_str)

    def create_war_zone(self, war_zone):
        row_numbers = list(range(self.n_row))
        row_numbers = list(map(str, row_numbers))

        column_numbers = list(range(self.n_column))
        column_numbers = list(map(str, column_numbers))

        max_row = len(row_numbers[-1]) + 1
        max_column = len(column_numbers[-1])

        space_str = " " * max_row
        war_zone_str = space_str
        for column_number in column_numbers: # ["0", "1", "2", "3", ..., "10"]
            space_number = max_column - len(column_number) + 1
            space_str = " " * space_number
            war_zone_str += column_number + space_str
        war_zone_str = war_zone_str[:-len(space_str)]
        war_zone_str += "\n"

        for row_number in row_numbers: # ["0", "1", "2", "3"....]
            space_number = max_row - len(row_number)
            space_str = " " * space_number

            row = self.war_zone[int(row_number)]
            row_str = (max_column* " ").join(row)

            war_zone_str += row_number + space_str + row_str + "\n"
        return war_zone_str

create_war_zone = warZone(15, 15)
print(create_war_zone)
