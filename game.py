#############################################################
# FILE : game.py
# WRITER : Ilan Vysokovsky, ilan.vys, 207375528
# EXERCISE : intro2cs1 ex9 2021
# DESCRIPTION: A program simulationg the Rush Hour game
# using Object Oriented Programming
#############################################################
import sys
from board import Board
from car import Car
from helper import load_json

CAR_LENGTH = [2, 3, 4]
CAR_NAMES = ["Y", "B", "O", "G", "W", "R"]

class Game:
    """
    Game manages the Rush Hour game. It is in charge of handling
    the game, playing turns, and validatig inputs.
    """
    
    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

    def __single_turn(self, move):
        """
        Runs a single turn in the game
        :param move: the move to perform
        :return: True if game is complete, None otherwise
        """
        move = move.split(',')
        color = move[0].upper()
        direction = move[1]
        
        self.board.move_car(color, direction)

        if self.board.cell_content(self.board.target_location()):
            return True
        
    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        game_ended = False
        invalid_input_flag = False
        
        if self.board.cell_content(self.board.target_location()):
            game_ended = True
        
        while not game_ended:
            print(self.board)
            
            if invalid_input_flag:
                print("Invalid input!")
                invalid_input_flag = False
                
            print("For help, type `hint`")
            move = input("Enter move: ")
            
            if move == '!':
                break
            
            if move == 'hint':
                print(self.board.possible_moves())
                move = input("Enter move: ")
                if move == '!':
                    break
            
            if self.__valid_input(move):
                game_ended = self.__single_turn(move)
            else:
                invalid_input_flag = True
        
        if game_ended:
            print(self.board)
            print("You win!")
    
    def __valid_input(self, user_input):
        """
        Checks if the input is valid and the move is possible to make
        :return: True if move is valid, False otherwise
        """
        if not ',' in user_input:
            return False
        
        user_input = user_input.split(',')
        if len(user_input) != 2:
            return False
        
        possible_moves = self.board.possible_moves()
        for move in possible_moves:
            if move[0] == user_input[0] and move[1] == user_input[1]:
                return True
        
        return False

def valid_car(car_name, car):
    length = car[0]
    orientation = car[2]
        
    if not car_name in CAR_NAMES:
        return False
    if not length in CAR_LENGTH:
        return False
    if not orientation in [1,0]:
        return False
    
    return True

if __name__== "__main__":
    board = Board()
    try:
        path_to_json = sys.argv[1]
    except:
        path_to_json = "car_config.json"
    finally:
        car_config = load_json(path_to_json)
        for car in car_config:
            if valid_car(car, car_config[car]):
                car_config[car]
                board.add_car(Car(
                    car, 
                    car_config[car][0],
                    (car_config[car][1][0],
                    car_config[car][1][1]),
                    car_config[car][2]))    
                
        game = Game(board)
        game.play()
        