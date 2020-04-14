import random
import os
from time import sleep

def refresh_screen(instance):
	os.system('cls')
	instance.displayBaord()
def coinToss(player1, player2):
	toss = ['Head', 'Tail']
	while True:
		selectedPlayer = input(f'Who will select the toss {player1} or {player2} ? ')
		if selectedPlayer.lower() in [player1.lower(), player2.lower()]:
			select = input('Select Head or Tail: ').lower()
			toss_result = random.choice(toss)
			print(toss_result)
			if toss_result.lower() == select:
				print(f'{player1} Wins the toss')
				return 1
			else:
				print(f'{player2} Wins the toss')
				return 0 
		else:
			print('Please select the correct player')

def playAgain(choice):
	if choice.lower() in ['yes','y','ye']:
		return True
	else:
		return False
		
def correctChoice(player,symbol):
	while True:
		choice_no = input(f'{player}[{symbol}] Please Choose 1 - 9 > ')
		if choice_no.isdigit() and int(choice_no) < 10 and int(choice_no) > 0:
			return choice_no
		else:
			print('Please Select a Valid Choice')
class Board:
	def __init__(self, playerX, PlayerO):
		self.cell = [" "]*10
		self.playerX = playerX
		self.playerO = playerO
	
	def displayBaord(self):
		print('\n')
		print(' Welcome to TicTocToe '.center(40, '-'))
		print(f' {self.playerX} vs {self.playerO} '.center(40, '-'))
		print('\n')
		print(" {} | {} | {} ".format(*self.cell[1:4]).center(40))
		print(" --------- ".center(40))
		print(" {} | {} | {} ".format(*self.cell[4:7]).center(40))
		print(" --------- ".center(40))
		print(" {} | {} | {} ".format(*self.cell[7:]).center(40))
		print('\n')
	def updateBoard(self, choice_no, player):
		if self.cell[choice_no] == ' ':
			self.cell[choice_no] = player
			return 	True 
		else: return False
	def isWinner(self,player):
		possiblities = [
			[1,2,3],
			[4,5,6],
			[7,8,9],
			[1,4,7],
			[2,5,8],
			[3,6,9],
			[1,5,9],
			[3,5,7]
		]
		for row in possiblities:
			result = True
			for num in row: #[1,2,3]
				if self.cell[num] != player:
					result =  False
			if result==True:
				return True
		return False
	def reset(self):
		self.cell = [" "]*10



playerX = input('Enter the Player-X name: ').title()
playerO = input('Enter the Player-O name: ').title()
board = Board(playerX, playerO)
toss_Winner = coinToss(playerX, playerO)
if toss_Winner:
	player1 = playerX
	player2 = playerO
else:
	player1 = playerO
	player2 = playerX
sleep(1)
refresh_screen(board)
i = 1 
while i<10:
	# player 1 move 
	while True:
		choice_no = correctChoice(player1,'X')
		if board.updateBoard(int(choice_no), 'X'):
			break
		else:
			print('Place is already taken')
	refresh_screen(board)
	if board.isWinner('X'):
		print(f'\n Hurray {player1} Won! \n')
		choice = input('Would you like to play again? (Y,N) ')
		if playAgain(choice):
			i = 0
			board.reset()
			continue
		else:
			exit(0)

	if i==9:		
		print(' Match Tie '.center(20,'*'))
		choice = input('Would you like to play again? (Y,N) ')
		if playAgain(choice):
			i = 0
			board.reset()
			continue
		else:
			exit(0)
	# player 2 move
	while True:
		choice_no = correctChoice(player2,'O')
		if board.updateBoard(int(choice_no), 'O'):
			break
		else:
			print('Place is already taken')
	refresh_screen(board)
	if board.isWinner('O'):
		print(f'\n Hurray {player2} Won!\n')
		choice = input('Would you like to play again? (Y,N)')
		if playAgain(choice):
			i = 0
			board.reset()
			continue
		else:
			exit(0)
	i +=2
	


	




