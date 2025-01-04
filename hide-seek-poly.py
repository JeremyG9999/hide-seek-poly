import random
import os
import time
class Guesses:
    def guess(self):
        pass
class Normal(Guesses):
    def guess(self):
        return [random.randint(1, 8)]
class Advanced(Guesses):
    def guess(self):
        guesses = []
        while len(guesses) < 2:
            guess = random.randint(1, 8)
            if guess not in guesses:
                guesses.append(guess)
        return guesses
class Insane(Guesses):
    def guess(self):
        guesses = []
        while len(guesses) < 3:
            guess = random.randint(1, 8)
            if guess not in guesses:
                guesses.append(guess)
        return guesses
class Hide_And_Seek:
    def __init__(self):
        self.reset_game()
        self.game_mode = None #new
    def reset_game(self):
        self.choice = None
        self.room_guess = None
        self.p1 = self.p2 = self.p3 = self.p4 = False
        self.choice1 = self.choice2 = self.choice3 = self.choice4 = None
        self.game_active = True
        self.round = 1
        self.survivors = []
        self.losers = []
    def setup_game(self):
        self.reset_game()
        valid_choices = ["2", "3", "4"]
        while self.game_active:
            self.choice = input("How many people playing, pick 2-4: ")
            if self.choice in valid_choices:
                num_players = int(self.choice)
                self.survivors = list(range(1, num_players + 1))
                if num_players >= 1: self.p1 = True
                if num_players >= 2: self.p2 = True
                if num_players >= 3: self.p3 = True
                if num_players >= 4: self.p4 = True
                print(f"We are playing with {self.choice} players")
                self.cls()
                self.players()
            else:
                self.cls()
                print("\nPick a valid number of players")
    def players(self):
        self.cls()
        print(f"Beginning of round {self.round}!")
        if self.round == 8:
            print("\nTHIS IS THE FINAL ROUND\n")
        if self.p1:
            self.player_round(1)
        if self.p2:
            self.player_round(2)
        if self.p3:
            self.player_round(3)
        if self.p4:
            self.player_round(4)
        self.player_results()
    def player_round(self, player_num):
        while self.game_active:
            try:
                choice = int(input(f"Player {player_num}, pick a hiding spot 1-8: "))
                if 1 <= choice <= 8:
                    if choice in [self.choice1, self.choice2, self.choice3, self.choice4]:
                        print(f"Room {choice} is already taken, please pick another room.")
                    else:
                        if player_num == 1:
                            self.choice1 = choice
                        elif player_num == 2:
                            self.choice2 = choice
                        elif player_num == 3:
                            self.choice3 = choice
                        elif player_num == 4:
                            self.choice4 = choice
                        break
                else:
                    print(f"Player {player_num}, please pick a valid choice between 1 and 8.")
            except ValueError:
                print("Please enter a valid number between 1 and 8.")
    def player_results(self):
        self.room_guess = self.game_mode.guess() #new
        self.cls()
        self.player_summary(1, self.p1, self.choice1)
        self.player_summary(2, self.p2, self.choice2)
        self.player_summary(3, self.p3, self.choice3)
        self.player_summary(4, self.p4, self.choice4)
        self.round_summary()
    def player_summary(self, number, is_active, choice):
        if is_active:
            if choice in self.room_guess: #different because
                if number == 1: #we made it a list
                    self.p1 = False
                elif number == 2:
                    self.p2 = False
                elif number == 3:
                    self.p3 = False
                elif number == 4:
                    self.p4 = False
                if number in self.survivors:
                    self.survivors.remove(number)
                self.losers.append(number)
                print(f"Player {number} is eliminated!")
            else:
                print(f"Player {number} is safe")
    def round_summary(self):
        print(f"\nEnd of round {self.round} summary!\n")
        print(f"There are currently {len(self.survivors)} player(s) left")
        print(f"The Hunter went to room number: {self.room_guess}\n")
        print("The hunter returned home!\n")
        self.choice1 = self.choice2 = self.choice3 = self.choice4 = None
        self.round += 1
        if not self.survivors:
            print("The hunter has won!")
            input("Press Enter to return to main menu: ")
            self.game_active = False
        elif self.round == 8:
            print("FINAL ROUND!!!\n")
            input("Press enter to go to the next round: ")
            self.players()
        elif self.round == 9:
            print("Game Over!\n")
            if not self.survivors:
                print("The hunter has won!")
            else:
                print(f"The survivors are player(s) {self.survivors}.")
                print(f"The losers are player(s) {self.losers}")
            input("Press Enter to return to main menu: ")
            self.game_active = False
        else:
            input(f"Press enter to go to round {self.round}: ")
            self.players()
    def cls(self):
        os.system('cls')
        time.sleep(0.1)
    def main_menu(self):
        self.reset_game()
        while True:
            self.cls()
            print("\nWelcome to the Main Menu")
            print("1. Play Normal Mode")
            print("2. Play Advanced Mode")
            print("3. Play Insane Mode")
            print("4. Exit")
            self.choice = input("Pick An Option via Number: ")
            if self.choice == "1":
                self.game_mode = Normal()
                self.setup_game()
            elif self.choice == "2":
                self.game_mode = Advanced()
                self.setup_game()
            elif self.choice == "3":
                self.game_mode = Insane()
                self.setup_game()
            elif self.choice == "4":
                print("\nGoodbye....")
                break
            else:
                print("Please Select the Correct Number")
def main():
    run = Hide_And_Seek()
    run.main_menu()
main()