import random

class warZone:
    def __init__(self, n_row, n_column):        
        self.n_row = n_row
        self.n_column = n_column
        self.ship_shape = "O"
        self.war_zone = self.init_war_zone()
        self.other_war_zone = self.init_war_zone()
    
    def init_war_zone(self):
        matrix = []
        for row in range(self.n_row):
            matrix.append(["o"]*self.n_column)
        return matrix

    def place_ships(self, ship, row_number, column_number, horizontal_vertical):
        for i in range(ship): gemi = 4
            if vertical == "vertical:"
                self.war_zone[row_number][column_number] = self.ship_shape
            else:
                self.war_zone[row_number+i][column_number = self.ship_shape]

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

war_zone = warZone(15, 15)
print(war_zone)

class warShips:
    def __init__(self, ships, war_zone):
        self.ships= ships # [3, 5, 6, 3, 4]
        self.war_zone = war_zone

    def enter_ships_coordinates(self):
        for ship in self.ships:
            row_number = None
            column_number = None
            horizontal_vertical = None
            while row_number is None or column_number is None or horizontal_vertical is None:
                try:
                    given_values = self.give_values(ship)
                    row_number, column_number, horizontal_vertical = given_values.split(" ")
                    row_number = int(row_number)
                    column_number = int(column_number)
                except:
                    print("You've entered wrong values. Please, read information again.")
                    row_number = None
                    # column_number = None
                    # horizontal_vertical = None
                else:
                    self.war_zone.place_ships(ship, row_number, column_number, horizontal_vertical)
        print(self.war_zone)
    
    def give_values(self, ship):
        given_values = input(f"""
Please enter your {ship}  size ship's coordinates with blank between them.
Given values by order: row_number (int), column_number (int), horizontal or vertical (str)
Your current warzone situation:
{self.war_zone}
""")
        return given_values

ships = [3, 4]

war_ships = warShips(ships, war_zone)
war_ships.enter_ships_coordinates()






