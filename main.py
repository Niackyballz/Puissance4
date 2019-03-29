def BoardClean(Board):
	Board = [[0 for i in range(7)] for i in range(7)]
	return Board


def ShowBoard(Board):
	for i in range(len(Board)):
		print(Board[i])


def Play(line, col, player, Board):
	Board[6-line][col]=player
	if Win(6-line,col,Board,player):
		print "Vainqueur joueur", player
		exit(1)
	return Board


def ColAvailable(col,Board):
	Collumn = True
	i = 0
	while not Collumn or i < 7:
		if Board[6-i][col] != 0:
			i += 1
		else:
			return True
	return False


def WhichLine(col,Board):
	Line = False
	i = 0
	while not Line:
		if Board[6-i][col] != 0:
			i += 1
		else:
			return i

def Win(x,y,board,number):
	if x+3 < 7:
		if board[x][y] == number and board[x+1][y] == number and board[x+2][y] == number and board[x+3][y] == number:
			return True
	elif x-3 < -1:
		if board[x][y] == number and board[x-1][y] == number and board[x-2][y] == number and board[x-3][y] == number:
			return True
	elif y+3 < 7:
		if board[x][y] == number and board[x][y+1] == number and board[x][y+2] == number and board[x][y+3] == number:
			return True
	elif y-3 < -1:
		if board[x][y] == number and board[x][y-1] == number and board[x][y-2] == number and board[x][y-3] == number:
			return True
	else:
		return False
	

###################################

terrain=0
coups=1
terrain=BoardClean(terrain)
ShowBoard(terrain)
while coups < 50:
	#R = -1
	#while R = input("Quelle colonne ? joueur 1 \n") < 0 or R > 6 or R not int:
	R = input("Quelle colonne ? joueur 1 \n")
	
	Play(WhichLine(R,terrain),R,1,terrain)
	ShowBoard(terrain)
	W = input("Quelle colonne ? joueur 2 \n")
	Play(WhichLine(W, terrain),W, 2, terrain)
	ShowBoard(terrain)
	coups =+ 1
