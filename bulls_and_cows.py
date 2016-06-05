
class Game(object):

	def __init__(self):
		self.secret_number = 0
		

	def check_if_number_has_correct_length(self, number):
		if len(number) == 4:
			return True
		print ("The length of the number is not 4 digits!")
		return False

	def check_if_number_has_different_digits(self, number):
		digits_list = []
		for digit in number:
			if digit not in digits_list:
				digits_list.append(digit)
		if len(digits_list) == 4:
			return True
		print("The number should have different digits!")
		return False

	def check_if_is_a_number(self, number):
		try:
			try_parse_to_int = int(number)
			return True
		except ValueError as e:
			print ("Please enter a valid number!")
			return False

	def get_secret_number(self):
		is_valid = False
		while(is_valid == False):
			number = input("Please enter the secret number: ")
			if self.check_if_number_has_correct_length(number) == False or self.check_if_number_has_different_digits(number) == False \
				or self.check_if_is_a_number(number) == False:
				continue
			self.secret_number = number
			return number
			
	def check_if_is_bull_or_cow(self, secret_number, player_choice):
			secret_number_list = list(str(secret_number))
			player_choice_list = list(str(player_choice))
			text = ""
			bulls = 0
			cows = 0
			for iterator in range(4):
				if secret_number_list[iterator] == player_choice_list[iterator]:
					secret_number_list[iterator] = "bull"
					bulls += 1
					text = str(bulls) + " Bulls and " + str(cows) + " Cows"
					continue
			for digit in player_choice_list:
				if digit in secret_number_list:
					cows += 1
					text = str(bulls) + " Bulls and " + str(cows) + " Cows"
					continue
			print (text)
	
	def manage_the_game(self, number_of_players):
		for num in range(int(number_of_players)):
			print (num)

	def start_game(self):
		end_of_the_game = False
		while(end_of_the_game != True):
			print("\n<---Welcome to our game 'Bulls and Cows--->\n")
			number_of_players = input("Enter the number of the players: ")
			if self.check_if_is_a_number(number_of_players) == False:
				continue
			if int(number_of_players) < 1 or int(number_of_players) > 2:
				print("\nPlease choice 1 or 2 players!")
				continue
			end_of_the_game = True
			self.manage_the_game(number_of_players)




class Player(object):

	def __init__(self):
		pass

class SelfChoice(Game, Player):

	def __init__(self):
		Player.__init__(self)
		Game.__init__(self)
		pass

	def select_number(self):
		is_valid = False
		while(is_valid == False):
				number = raw_input("Please enter a number of your choice: ")
				if self.check_if_number_has_correct_length(number) == False or self.check_if_number_has_different_digits(number) == False or self.check_if_is_a_number(number) == False:
					continue
				is_valid = True
				return number
			


def main():

	game = Game()
	#secret_number = game.get_secret_number()
	#player1 = SelfChoice()
	#player2 = SelfChoice()
	#choice1 = player1.select_number()
	#game.check_if_is_bull_or_cow(secret_number, choice1)
	game.start_game()

if __name__ == "__main__":
	main()		