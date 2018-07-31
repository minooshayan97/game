from random import randint
from consts import *


class Game(object):
    def __init__(self, length=GAME_LENGTH):
        self.length = length
        self.initial_state = self.new_game
        self.turns = 0
        self.max_turns = 4
        print(self.initial_state)

    @property
    def new_game(self):
        initial = []
        while len(initial) < self.length:
            color = COLORS[str(randint(MIN_COLORS, MAX_COLORS))]
            if color not in initial:
                initial.append(color)
        return initial

    def turn(self):
        white = 0
        black = 0
        guess = input().split(',')
        for item in guess:
            if item in self.initial_state:
                white += 1
        for j in range(0, self.length):
            if guess[j] == self.initial_state[j]:
                black += 1
        self.turns += 1
        return black, white

    def check_game_over(self, black, white):
        if self.is_won(black):
            self.win_message()
            return True
        elif self.is_lose(black):
            self.lose_message()
            return True
        else:
            self.state_of_game(black, white)
            return False

    def is_won(self, black):
        return black == self.length

    def is_lose(self, black):
        return self.turns == self.max_turns and not self.is_won(black)

    def play(self):
        while self.turns < self.max_turns:
            black, white = self.turn()
            if self.check_game_over(black, white):
                break

    def state_of_game(self, black, white):
        print("black:{}\t white:{}".format(black, white))
        print("you have {} attempts left.".format(self.max_turns - self.turns))

    def win_message(self):
        print("you won!")

    def lose_message(self):
        print("you lose!")


g = Game()
g.play()


