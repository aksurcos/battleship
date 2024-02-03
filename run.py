import random

class warZone:
    def __init__(self, n_row, n_column):        
        self.n_row = n_row
        self.n_column = n_column
        self.ship_shape = "O"
        self.warzone = self.init_warzone()
        self.other_warzone = self.init_warzone()
    
    def init_warzone(self):
        matrix = []
        for row in range(self.n_row):
            matrix.append(["+"]*self.n_column)
        return matrix

    def place_ships(self, ship, row_number, column_number, horizontal_vertical):
        for i in range(ship): # ship = 4
            if horizontal_vertical == "horizontal":
                self.warzone[row_number][column_number+i] = self.ship_shape
            else:
                self.warzone[row_number+i][column_number] = self.ship_shape

    def __str__(self):
        our_warzone = self.create_warzone(self.warzone)
        other_warzone = self.create_warzone(self.other_warzone)

        our_warzone_list = our_warzone.split("\n")
        other_warzone_list = other_warzone.split("\n")
        more_character = len(str(self.n_column)) - 1
        other_warzone_list[0] = other_warzone_list[0][more_character:]
        
        warzone_str = [(10*" ").join([me, other])
                        for me, other in zip(our_warzone_list, other_warzone_list)]
        return "\n".join(warzone_str)

    def create_warzone(self, warzone):
        row_numbers = list(range(self.n_row))
        row_numbers = list(map(str, row_numbers))

        column_numbers = list(range(self.n_column))
        column_numbers = list(map(str, column_numbers))

        max_row = len(row_numbers[-1]) + 1
        max_column = len(column_numbers[-1])

        space_str = " " * max_row
        warzone_str = space_str
        for column_number in column_numbers: # ["0", "1", "2", "3", ..., "10"]
            space_number = max_column - len(column_number) + 1
            space_str = " " * space_number
            warzone_str += column_number + space_str
        warzone_str = warzone_str[:-len(space_str)]
        warzone_str += "\n"

        for row_number in row_numbers: # ["0", "1", "2", "3"....]
            space_number = max_row - len(row_number)
            space_str = " " * space_number

            row = self.warzone[int(row_number)]
            row_str = (max_column* " ").join(row)

            warzone_str += row_number + space_str + row_str + "\n"
        return warzone_str


class warShips:
    def __init__(self, ships, warzone):
        self.ships= ships # [3, 5, 6, 3, 4]
        self.warzone = warzone

    def enter_ships_coordinates(self, random:False, computer=False):
        for ship in self.ships:
            row_number = None
            column_number = None
            horizontal_vertical = None
            while row_number is None or column_number is None or horizontal_vertical is None:
                try:
                    if random:
                        given_values = self.create_random_location()
                    else:
                        given_values = self.take_given_values(ship)
                    row_number, column_number, horizontal_vertical = given_values.split(" ")
                    if horizontal_vertical not in ["horizontal", "vertical"]:
                        raise RuntimeError
                    row_number = int(row_number)
                    column_number = int(column_number)
                    self.warzone.is_coordinates_ok(ship, row_number,
                                                                    column_number, horizontal_vertical)
                except RuntimeError:
                    if not random:
                        print("You've entered wrong values. Please, read information again.")
                    row_number = None
                    # column_number = None
                    # horizontal_vertical = None
                else:
                    self.warzone.place_ships(ship, row_number, column_number, horizontal_vertical)
        if not computer:
            print(self.warzone)
    
    def take_given_values(self, ship):
        given_values = input(f"""
Please enter your {ship}  size ship's coordinates with blank between them.
Given values by order: row_number (int), column_number (int), horizontal or vertical (str)
Your current warzone situation:
{self.warzone}
""")
        return given_values

    def create_random_location(self):
        row_number = random.randint(0, self.warzone.n_row-1)
        column_number = random.randint(0, self.warzone.n_column-1)
        horizontal_vertical = random.choice(["horizontal", "vertical"])
        given_values = f"{row_number} {column_number} {horizontal_vertical}"
        return given_values

    def are_all_ships_sinked(self):
        return self.warzone.total_ship_points == 0

class Player:
    def __init__(self, warzone, war_ships, is_comp):
        self.warzone = warzone
        self.warships = warships
        self.is_comp = is_comp
    
    def play(self, comp):
        if not self.is_comp:
            print(self.warzone)
        for i in range(3):
            row_number = None
            column_number = None
            while row_number is None or column_number is None:
                try:
                    if self.is_comp:
                        given_values = self.create_random_location()
                    else:
                        given_values = self.take_given_values()
                    row_number, column_number = given_values.split(" ")
                    row_number = int(row_number)
                    column_number = int(column_number)
                    is_ok = self.warzone.is_target_ok(row_number, column_number)
                    if not is_ok:
                        raise RuntimeError
                
                except RuntimeError:
                    if not self.is_comp:
                        print("You've enter wrong values. Please, read information carefully.")
                    row_number = None
                else:
                    self.warzone.update(row_number, column_number, comp.warzone)
                    if not self.is_comp:
                        print(self.warzone)
                    are_ships_sinked = self.warships.are_all_ships_sinked()
                    if are_ships_sinked:
                        return True
        return False

    def take_given_values(self):
        given_values = input(f"Please enter the coordinates that you want to attack.")
        return given_values
    
    def create_random_location(self):
        row_number = random.randint(0, self.warzone.n_row-1)
        column_number = random.randint(0, self.warzone.n_column-1)
        given_number = f"{row_number} {column_number}"
        return given_values

class battleShip:
    def __init__(self, n_row, n_column, n_ship):
        player_warzone = warZone(n_row, n_column)
        comp_warzone = warZone(n_row, n_column)
    
        self.ships = []

        player_war_ships = WarShips(self.ships, player_warzone)
        comp_war_ships = WarShips(self.ships, comp_warzone)

        self.player = Player(player_warzone, player_war_ships, False)
        self.comp = Player(comp_warzone, player_war_ships, True)

n_column = 10
n_row = 10 
n_ship = 4

battle_ship = battleShip(n_row, n_column, n_ship)
battle_ship.start()










