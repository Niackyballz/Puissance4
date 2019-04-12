def BoardClean(Board):
	Board = [[0 for i in range(7)] for i in range(7)]
	return Board


def ShowBoard(Board):
	for i in range(len(Board)):
		print(Board[i])


def Play(line, col, player, Board):
	Board[6-line][col]=player
	if Win(6-line,col,Board,player):
		print ("Vainqueur joueur", player)
		ShowBoard(Board)
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
		if Board[6 - i][col] != 0:
			i += 1
		else:
			return i


def Win(x,y,board,number):
	if x + 3 < 7:
		#vainqueur haut en bas
		if board[x][y] == number and board[x+1][y] == number and board[x+2][y] == number and board[x+3][y] == number:
			return True
	if y + 3 < 7:
		#vainqueur ligne vers la droite
		if board[x][y] == number and board[x][y+1] == number and board[x][y+2] == number and board[x][y+3] == number:
			return True
	if y - 3 > -1:
		#vainqueur ligne vers la gauche
		if board[x][y] == number and board[x][y-1] == number and board[x][y-2] == number and board[x][y-3] == number:
			return True
	if y - 2 > -1 and y + 1 < 7:
		#vainqueur ligne 2 gauche 1 droite
		if board[x][y-2] == number and board[x][y-1] == number and board[x][y] == number and board[x][y+1] == number:
			return True
	if y - 1 > -1 and y + 2 < 7:
		#vainqueur ligne 1 gauche 2 droite
		if board[x][y-1] == number and board[x][y] == number and board[x][y+1] == number and board[x][y+2] == number:
			return True
	if x+3 < 7 and y+3 < 7:
		#vainqueur diagonale vers le bas droite
		if board[x][y] == number and board[x+1][y+1] == number and board[x+2][y+2] == number and board[x+3][y+3] == number:
			return True
	if x+3 < 7 and y -3 > -1:
		#vainqueur diagonale vers le bas gauche
		if board[x][y] == number and board[x+1][y-1] == number and board[x+2][y-2] == number and board[x+3][y-3] == number:
			return True
	if x-3 > -1 and y +3 < 7:
		#vainqueur diagonale vers le haut droite
		if board[x][y] == number and board[x-1][y+1] == number and board[x-2][y+2] == number and board[x-3][y+3] == number:
			return True
	if x-3 > -1 and y -3 > -1:
		#vainqueur diagonale vers le haut gauche
		if board[x][y] == number and board[x-1][y-1] == number and board[x-2][y-2] == number and board[x-3][y-3] == number:
			return True
	if x+2 < 7 and y+2 < 7 and x-1 > -1 and y-1 > -1 :
		#vainqueur diagonale vers le bas droite 1 + piece + 2
		if board[x-1][y-1] == number and board[x][y] == number and board[x+1][y+1] == number and board[x+2][y+2] == number:
			return True
	if x+1 < 7 and y+1 < 7 and x-2 > -1 and y-2 > -1 :
		#vainqueur diagonale vers le bas droite 2 + piece + 1
		if board[x-2][y-2] == number and board[x-1][y-1] == number and board[x][y] == number and board[x+1][y+1] == number:
			return True	
	if x+1 < 7 and y+2 < 7 and x-2 > -1 and y-1 > -1 :
		#vainqueur diagonale vers le bas gauche 1 + piece + 2
		if board[x+1][y-1] == number and board[x][y] == number and board[x-1][y+1] == number and board[x-2][y+2] == number:
			return True
	if x+2 < 7 and y+1 < 7 and x-1 > -1 and y-2 > -1 :
		#vainqueur diagonale vers le bas gauche 2 + piece + 1
		if board[x+2][y-2] == number and board[x+1][y-1] == number and board[x][y] == number and board[x-1][y+1] == number:
			return True		
	else:
		return False
	

###################################
terrain=0
terrain=BoardClean(terrain)
coups=0
ShowBoard(terrain)
while coups < 49:
#	if input("Quelle colonne ? joueur 1 \n") != {0:6}:
	R = input("Quelle colonne ? joueur 1 \n")
	Play(WhichLine(R,terrain),R,1,terrain)
	ShowBoard(terrain)
	W = input("Quelle colonne ? joueur 2 \n")
	Play(WhichLine(W, terrain),W, 2, terrain)
	ShowBoard(terrain)
	coups =+ 1