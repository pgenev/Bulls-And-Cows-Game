
class Game(object):

	def __init__(self):
		self.secret_number = 0

	def check_if_number_has_correct_length(self, number):
		if len(str(number)) == 4:
			return True
		print ("The length of the number is not 4 digits!")
		return False

	def check_if_number_has_different_digits(self, number):
		digits_list = []
		for digit in str(number):
			if digit not in digits_list:
				digits_list.append(digit)
		if len(digits_list) == 4:
			return True
		print("The number should have different digits!")
		return False

	def take_number(self):
		is_valid = False
		while(is_valid == False):
			try:
				number = int(raw_input("Please enter the secret number: "))
				if self.check_if_number_has_correct_length(number) == False or self.check_if_number_has_different_digits(number) == False:
					continue
				is_valid = True
				self.secret_number = number
				return number
			except ValueError as e:
				print ("Error: %s" % e)
				print ("Please enter a valid number!")

	def check_if_is_bull_or_cow(self, secret_number, player_choice):
			secret_number_list = list(str(secret_number))
			player_choice_list = list(str(player_choice))
			text = ""
			bulls = 0
			cows = 0
			for iterator in range(4):
				if secret_number_list[iterator] == player_choice_list[iterator]:
					bulls += 1
					text = str(bulls) + " Bulls and " + str(cows) + " Cows"
					continue
			for digit in player_choice_list:
				if digit in secret_number_list:
					cows += 1
					text = str(bulls) + " Bulls and " + str(cows) + " Cows"
					continue
			if bulls == 4 and cows == 4:
				print("You won the game!")
				return True
			
	def try_to_guess_the_secret_number(self, player1_choice1, player_choice2):

		pass


class Player(object):

	def __init__(self):
		pass

class SelfChoice(Game, Player):

	def __init__(self):
		Player.__init__(self)
		Game.__init__(self)
		pass

	def choice_number(self):
		is_valid = False
		while(is_valid == False):
			try:
				number = int(raw_input("please enter a number of your choice: "))
				if self.check_if_number_has_correct_length(number) == False or self.check_if_number_has_different_digits(number) == False:
					continue
				is_valid = True
				return number
			except ValueError as e:
				print ("Error: %s" % e)
				print ("Please enter a valid number!")


def main():

	game = Game()
	secret_number = game.take_number()
	print (secret_number)
	player1 = SelfChoice()
	player2 = SelfChoice()
	choice_number1 = player1.choice_number()
	print (choice_number)
	game.check_if_is_bull_or_cow(secret_number, choice_number)

if __name__ == "__main__":
	main()		