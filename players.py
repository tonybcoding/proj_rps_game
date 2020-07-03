import random

class Player():
	#
	# all subclasses to execute setting of name
	def __init__(self, entered_name):
		self.name = self.setName(entered_name)
	#
	def setName(self, entered_name):
		#
		# if entered_name is blank,
		# create a name from 4 to 12 characters long using random
		# ASCII characters
		name = ""
		if entered_name == "":
			for n in range(random.randint(4, 12)):
				name += chr(random.randint(97, 122))
		else:
			name = entered_name
		return name.capitalize()


class RandomPlayer(Player):
	pass


class RefelctPlayer(Player):
	pass


class CyclePlayer(Player):
	pass


class SmartPlayer(Player):
	pass


class HumanPlayer(Player):
	pass
