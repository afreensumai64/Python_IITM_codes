'''
Format Tic-Tac-Toe Board
You are given a tic-tac-toe board of size m x n containing characters:

'X' for player X
'O' for player O
' ' (space) for empty cells
Your task is to print this board with borders using the characters +, -, and |.
The border format must be as follows:

Each row is wrapped in | separators for each column.
Horizontal lines made of + and - separate each row, including the top and bottom.
NOTE: This is an I/O type problem. You must write the complete code for taking input and printing the output.

Input Format

The first line contains two integers, m and n, denoting the number of rows and columns of the board.
The next m lines each contain a string of n characters from 'X', 'O', or ' '(space).
Output Format

The board printed with borders using +, -, and |.
Example

Input

3 4
O XO
XO
O  X

Output

+-+-+-+-+
|O| |X|O|
+-+-+-+-+
|X|O| | |
+-+-+-+-+
|O| |X| |
+-+-+-+-+
'''

# Read board dimensions
m, n = map(int, input().split())

# Read the board rows
board = []
for _ in range(m):
    row = input()
    # If the input row is shorter than n, pad with spaces
    row = row.ljust(n)
    board.append(list(row))

# Build horizontal border
horizontal = '+' + '+'.join(['-' for _ in range(n)]) + '+'

# Print the board with borders
for i in range(m):
    print(horizontal)
    row_str = '|'.join(board[i])
    print('|' + row_str + '|')
print(horizontal)
