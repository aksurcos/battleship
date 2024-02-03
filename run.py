import random

def colored_print(print_str, color):
    colors = {"red": 31, "green": 32, "yellow": 33}
    color_code = colors[color]
    return f"\033[1;{color_code}m{print_str}\033[0m"


class warZone:
    def __init__(self, n_row, n_column):        
        self.n_row = n_row
        self.n_column = n_column
        self.ship_shape = "O"
        self.warzone = self.init_warzone()
        self.other_warzone = self.init_warzone()
        self.total_ship_points = 0
        self.warzones = {
            "your": self.warzone,
            "other": self.other_warzone
        }
        self.update_codes = {
            "missed": colored_print("X", "yellow"),
            "hit": colored_print("+", "green"),
            "damaged": colored_print("X","red")
        }
    
    def init_warzone(self):
        matrix = []
        for row in range(self.n_row):
            matrix.append(["-"]*self.n_column)
        return matrix


    def place_ships(self, ship, row_number, column_number, horizontal_vertical):
        for i in range(ship): # ship = 4
            if horizontal_vertical == "horizontal":
                self.warzone[row_number][column_number+i] = self.ship_shape
            else:
                self.warzone[row_number+i][column_number] = self.ship_shape
        self.total_ship_points += ship

    def is_coordinate_ok(self, ship, row_number, column_number, horizontal_vertical):
        location = column_number if horizontal_vertical == "horizontal" else row_number
        edge = self.n_column if horizontal_vertical == "horizontal" else self.n_row
        is_zone_enough = self.is_zone_enough(ship, location, edge)

        if not is_zone_enough:
            raise RuntimeError

        is_position_ok = self.is_position_ok(ship, row_number, column_number, horizontal_vertical)
        
        if not is_position_ok:
            raise RuntimeError

        def is_zone_enough(self, ship, location, edge):
            if ship + location >= edge:
                return False
            return True
        
        def is_position_ok (self, ship, row_number, column_number, horizontal_vertical):
            for i in range(ship):
                if horizontal_vertical == "horizontal":
                    symbol = self.warzone[row_number][column_number+i]
                else:
                    symbol = self.warzone[row_number+i][column_number]
                if symbol == self.ship_shape:
                    return False
            return True

        def is_target_ok(self, row_number, column_number):
            if not (0 <= row_number and row_number < self.n_row):
                return False

            if not (0 <= column_number and column_number < self.n_column):
                return False

            green_x = self.update_codes["hit"]
            yellow_x = self.update_codes["missed"]
            if self.other_warzone[row_number][column_number] in [green_x, yellow_x]:
                return False
            
            return True
    
    def update(self, row_number, column_number, comp_warzone):
        if comp_warzone.warzone[row_number][column_number] == self.ship_shape:
            self._update("other", row_number, column_number, "hit")
            self.total_ship_points -= 1
            comp_warzone._update("your", row_number, column_number, "damaged")
        else:
            self._update("other", row_number, column_number, "missed")
            comp_warzone._update("your", row_number, column_number, "missed")

    def _update(self, which, row_number, column_number, result):
        self.warzones[which][row_number][column_number] = self.update_codes[result]
                

    def __str__(self):
        your_warzone = self.create_warzone(self.warzone)
        other_warzone = self.create_warzone(self.other_warzone)

        your_warzone_list = your_warzone.split("\n")
        other_warzone_list = other_warzone.split("\n")
        more_character = len(str(self.n_column)) - 1
        other_warzone_list[0] = other_warzone_list[0][more_character:]
        
        warzone_str = [(10*" ").join([your, other])
                        for your, other in zip(your_warzone_list, other_warzone_list)]
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

    def enter_ships_coordinates(self, random:False, comp=False):
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
                    self.warzone.is_coordinate_ok(ship, row_number,
                                                                    column_number, horizontal_vertical)
                except RuntimeError:
                    if not random:
                        print("You've entered wrong values. Please, read information again.")
                    row_number = None
                    # column_number = None
                    # horizontal_vertical = None
                else:
                    self.warzone.place_ships(ship, row_number, column_number, horizontal_vertical)
        if not comp:
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
    
        self.ships = self.create_ship(n-ship)        
        
        player_war_ships = warships(self.ships, player_warzone)
        comp_war_ships = warships(self.ships, comp_warzone)

        self.player = Player(player_warzone, player_war_ships, False)
        self.comp = Player(comp_warzone, player_war_ships, True)
    
    def start(self):
        is_random = self.random_or_manuel()
        self.player.warships.take_ships_coordinates(random=is_random, comp=False)
        self.comp.warships.take_ships_coordinates(random=True, comp=True)

        while True:
            player_won = self.player.play(self.comp)

            if player_won:
                print("CONGRATULATONS! You win.")
                break
            
            comp_won = self.comp.play(self.player)
            
            if comp_won:
                print("SORRY! You lost.")
                break
    
    @staticmethod
    def create_ship(n_ship):
        ships = []
        max_ship_size = 5
        for ship in range(n_ship):
            ships.append(random.randint(1, max_ship_size))
        return ships

    def random_or_manuel(self):
        is_random = None
        while is_random is None:
            is_random = input("Do you want to place your ships randomly or manually? If randomly, type True. If not type False." )
            if is_random not in ["True", "False"]:
                is_random = None
            else:
                bool_is_random = is_random == "True"
        return bool_is_random












