#############################################################
# FILE : car.py
# WRITER : Ilan Vysokovsky, ilan.vys, 207375528
# EXERCISE : intro2cs1 ex9 2021
# DESCRIPTION: A program simulationg the Rush Hour game
# using Object Oriented Programming
#############################################################
class Car:
    """
    Car is in charge of all the Car related behavior.
    Saves the car's name, length, location and orientation.
    Can change the car's location.
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__coordinates = self.__init_car_location(location, length, orientation)
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        return self.__coordinates

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        if self.__orientation == 1:
            return {
                'l': "like Beyonce said - `to the LEFT, to the LEFT`",
                'r': "like Bibi said - `to the RIGHT, to the RIGHT`",
            }
        if self.__orientation == 0:
            return {
                'u': "You can light it UP",
                'd': "You can burn it Down",
            }
        
    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        if movekey == 'd':
            coords = self.__coordinates[len(self.__coordinates) - 1]
            return [(coords[0] + 1, coords[1])]
        if movekey == 'u':
            coords = self.__coordinates[0]
            return [(coords[0] - 1, coords[1])]
        if movekey == 'r':
            coords = self.__coordinates[len(self.__coordinates) - 1]
            return [(coords[0], coords[1] + 1)]
        if movekey == 'l':
            coords = self.__coordinates[0]
            return [(coords[0], coords[1] - 1)]
        
        return []

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if (self.__orientation == 0 and movekey in ['l', 'r']) \
            or (self.__orientation == 1 and movekey in ['d', 'u']):
                return False
            
        new_coordinate = self.movement_requirements(movekey)
        
        if new_coordinate:
            if movekey in ['d', 'r']:
                self.__coordinates = self.__coordinates[1:]
                self.__coordinates.append(new_coordinate[0])
            if movekey in ['l', 'u']:
                self.__coordinates = self.__coordinates[:-1]
                self.__coordinates.insert(0, new_coordinate[0])
                
            self.__location = self.__coordinates[0]
            return True
        else:
            return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
    
    def __init_car_location(self, location, length, orientation):
        """ 
        :param location: A tuple representing the car's head (row, col) location
        :param length: A positive int representing the car's length.
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        :return: list of tuples with the car's coordinates
        """
        car_coordinates = []
        if orientation == 1:
            for j in range(0, length):
                car_coordinates.append((location[0], location[1] + j))
        if orientation == 0:
            for i in range(0, length):
                car_coordinates.append((location[0] + i, location[1]))
        
        return car_coordinates
    