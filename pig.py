import random

"""This is the code implementation for the Die"""
class Die:
    def __init__(self, sides=6):
        self.sides = sides
        random.seed(0) # This is for consistent results during testing.

    def roll(self):
        return random.randint(1, self.sides)

"""Implementation of the Player class"""
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

    def __str__(self):
        return f"{self.name} has a score of {self.score}"

"""This is the implementation of the Game class and the Rules of the Game"""
class Game:
    def __init__(self):
        self.die = Die()
        self.players = [Player("Player 1"), Player("Player 2")]
        self.current_player_index = 0

    def switch_turn(self):
        self.current_player_index = (self.current_player_index + 1) % 2

    def play_turn(self):    # This is where the bulk of the code will go.
        current_player = self.players[self.current_player_index]
        turn_score = 0

        while True:
            roll = self.die.roll()
            print(f"{current_player.name} rolled a {roll}")

            if roll == 1:
                print(f"{current_player.name} has lost their points for this turn!")
                turn_score = 0
                break
            else:
                turn_score += roll
                print(f"Accumulated score this turn is: {turn_score}")

                decision = input(f"{current_player.name}, roll (r) or hold (h)? ").lower()
                if decision == 'h':
                    current_player.add_score(turn_score)
                    print(f"{current_player.name} holds. Total Score: {current_player.score}")
                    break

        self.switch_turn()

    def is_game_over(self):          # Checks if game is over, Win condition.
        for player in self.players:
            if player.score >= 100:
                print(f"{player.name} wins with {player.score} points!")
                return True
        return False

    def play_game(self):
        print("Starting Pig, The Game!")
        while not self.is_game_over():
            self.play_turn()
        print("Game Over!")

if __name__ == "__main__":
    game = Game()
    game.play_game()
    
