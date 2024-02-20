from .die import Die
from .utils import i_just_throw_an_exception
import sys
import ipdb

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()


    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self, dice_value):
        total = 0
        for die in dice_value:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        start_index = 0

        while True:
            runner = cls()
            
            runner.round = start_index
            runner.wins = c
            runner.loses = runner.round-runner.wins

            print("Round {}\n".format(runner.round+1))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer(runner.dice):
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is:", runner.answer(runner.dice))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                c = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == "Y" or prompt == '':
                start_index += 1
                continue
            else:
                print("Goodbye")
                sys.exit()
            #else:
            #    i_just_throw_an_exception()
