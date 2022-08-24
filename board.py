#############################################################
# FILE : board.py
# WRITER : Ilan Vysokovsky, ilan.vys, 207375528
# EXERCISE : intro2cs1 ex9 2021
# DESCRIPTION: A program simulationg the Rush Hour game
# using Object Oriented Programming
#############################################################
class Board:
    """
    Board is in charge the game board. It holds the board's state and
    a list of cars the are in the game. It can reach all the cars in
    the game and return info about the cells in the borad.
    """
    SIZE = 7
    
    def __init__(self):
        """
        The constructor initializes an empty board with the integer `0`
        marking an empty space, with a border to the right of the board 
        marked by `*`, and the exit marked by `E`.
        """
        self.__board = []
        self.__cars = []
        
        for i in range(0, self.SIZE):
            self.__board.append([0] * self.SIZE)
            if i == 3:
                self.__board[i].append(0)
            else:
                self.__board[i].append('*')
                
    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        clear = "\n" * 100
        print(clear)
        
        str_to_print = ""
        for i in range(0, self.SIZE):
            for j in range(0, self.SIZE + 1):
                content = self.cell_content((i, j))
                
                if content:
                    str_to_print += content + "   "
                else:
                    str_to_print += "_   "
            
            str_to_print += "\n\n"
        
        return str_to_print

    def cell_list(self):
        """ 
        This function returns the all coordinates of cells in this board,
        and the target cell.
        :return: list of coordinates
        """
        cells = []
        target = self.target_location()
        for i in range(0, self.SIZE):
            for j in range(0, self.SIZE):
                cells.append((i, j))
        
        cells.append(self.target_location())
        
        return cells
        

    def possible_moves(self):
        """ 
        This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        moves_lst = []
        for car in self.__cars:
            possible_moves = car.possible_moves()
            for move in possible_moves:
                cell = car.movement_requirements(move)[0]
                
                if cell == self.target_location():
                    moves_lst.append((car.get_name(), move, possible_moves[move]))
                    continue
                
                if cell[0] < 0 or cell[0] >= self.SIZE \
                    or cell[1] < 0 or cell[1] > self.SIZE:
                        continue
                    
                if self.cell_content(cell):
                    continue
                
                moves_lst.append((car.get_name(), move, possible_moves[move]))
        
        return moves_lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return (3, 7)

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name of the car in coordinate, None if empty,
                 `E` for target cell and `*` for the border
        """
        for car in self.__cars:
            for car_coordinate in car.car_coordinates():
                if coordinate == car_coordinate:
                    return car.get_name()
                
        if self.__board[coordinate[0]][coordinate[1]] != 0:
            return self.__board[coordinate[0]][coordinate[1]]
        
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        for car_in_game in self.__cars:
            if car.get_name() == car_in_game.get_name():
                return False
            
        for coordinate in car.car_coordinates():
            if coordinate[0] < 0 or coordinate[0] >= self.SIZE \
                or coordinate[1] < 0 or coordinate[1] > self.SIZE:
                    return False
                
            cell_content = self.cell_content(coordinate)
            if cell_content:
                return False
            
        self.__cars.append(car)
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for car in self.__cars:
            if car.get_name() == name:
                if not car.movement_requirements(movekey):
                    return False
                
                new_coord = car.movement_requirements(movekey)[0]
                
                if not movekey in car.possible_moves():
                    return False
                
                if new_coord[0] < 0 or new_coord[0] >= self.SIZE \
                    or new_coord[1] < 0 or new_coord[1] > self.SIZE:
                        return False
                    
                if self.cell_content(new_coord):
                    return False
                
                return car.move(movekey)
            
        return False
