

from pprint import pprint


def printboardrow(ro):
	'''print a row of the board'''
	print('|', end='')
	for indx in range(len(ro)):
		print(ro[indx], end='')
		if indx<len(ro)-1: print(' ', end='')
	print('|')

def printtopbottom(n):
	'''print a row for either the top or bottom of the board'''
	for slot in range(2*n+1):
		print('-', end='')
	print()

def printseprow(n):
	'''print a decorator row separating content rows'''
	print('|', end='')
	for slot in range(2*n-1):
		print(' ', end='')
	print('|')

def draw_board(board):
	printtopbottom(len(board))
	for row_indx in board: printboardrow(row_indx)
	printtopbottom(len(board))

def extract_column(board, colnum):
	''' extract a board column for comparison'''
	n = len(board)
	col = [' '] * n

	if colnum > n:
		print('this column index is not valid')
		return -1
	else:
		for i in range(n):
			if board[i][colnum] != ' ': col[i] = board[i][colnum]
		return col

def compare_boards(board1, board2):
	''' compare two boards '''
	# primary length checks
	n1 = len(board1)
	m1 = len(board1[0])
	n2 = len(board2)
	m2 = len(board2[0])
	if n1 != n2 or m1 != m2:
		print('not valid boards for comparison')
		return -1
	
	# compare the two boards
	else:
		for row_indx in range(n1):
			for col_indx in range(m1):
				if board1[row_indx][col_indx] != board2[row_indx][col_indx]:
					print(f'The boards differ at position {row_indx}, {col_indx}')
					return False
		return True


def iterate(in_board):
	''' iterate across the board and  '''
	board = in_board
	# Set up iteration
	n = len(board)

	#iterate through rows of the board
	for row_indx in range(n):

		ro = board[row_indx]
		# check for left-right sandwiches
		for indx in range(n)[1:-1]:
			if ro[indx-1] == 'b' and ro[indx+1] == 'b': ro[indx] = 'r'
			if ro[indx-1] == 'r' and ro[indx+1] == 'r': ro[indx] = 'b'
		
		# check for doubles to the right
		for indx in range(n)[:-2]:
			if ro[indx+1] == 'b' and ro[indx+2] == 'b': ro[indx] = 'r'
			if ro[indx+1] == 'r' and ro[indx+2] == 'r': ro[indx] = 'b'

		# check for doubles to the left
		for indx in range(n)[2:]:
			if ro[indx-1] == 'b' and ro[indx-2] == 'b': ro[indx] = 'r'
			if ro[indx-1] == 'r' and ro[indx-2] == 'r': ro[indx] = 'b'
	
	# iterate through columns of the board
	for col_indx in range(n):
		# check for top-bottom sandwiches
		for indx in range(n)[1:-1]:
			if board[indx-1][col_indx] == 'b' and board[indx+1][col_indx] == 'b': board[indx][col_indx] = 'r'
			if board[indx-1][col_indx] == 'r' and board[indx+1][col_indx] == 'r': board[indx][col_indx] = 'b'
	return board



if __name__ == '__main__':

	# Intro: set board size
	board_size = 6
	board = [[' '] * board_size for _ in range(board_size)]
	# ro = ['x','x',' ','x','o','x']
	board[0][1] = 'b'
	#board[0][3] = 'b' #added for troubleshooting
	board[1][2] = 'r'
	board[1][5] = 'r'
	board[2][3] = 'r'
	board[2][5] = 'r'
	board[3][2] = 'r'
	board[3][3] = 'r'
	board[4][5] = 'r'

	old_board=board


	draw_board(old_board)
	iterate(board)
	draw_board(old_board)
	draw_board(board)

#	for i in range(8): print(i, end='')
#	for i in range(8)[:-2]: print(i, end='')