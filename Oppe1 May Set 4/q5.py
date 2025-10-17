'''
Print Pieces Moved from Chess Notation string.
Write a program that reads chess moves in standard algebraic notation and prints out the names of the chess pieces that have been moved. For castling moves, both the king and rook should be printed.

NOTE: This is an I/O type question. You need to write the complete code to read the input and print the output.

Input Format
The input will be a string of chess moves in format "{move_number} {white_move} {black_move}, where each move is given in standard algebraic notation.
Output Format
Print the names of the pieces moved in each move. The output should be each piece's name in separate lines. For castling, print "King" and "Rook".
Chess Notation Details
Pieces are represented by their initials:
K - King
Q - Queen
R - Rook
B - Bishop
N - Knight
Pawn (no initial, just represented by move)
Castling is represented with:
O-O (kingside castling)
O-O-O (queenside castling)
Example

Input

1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. O-O Qc7
Output

Pawn
Pawn
Knight
Knight
Bishop
Pawn
King
Rook
Queen
Input for Castling

1. e4 e5 2. O-O O-O-O
Output

Pawn
Pawn
King
Rook
King
Rook
'''
# Mapping from notation to piece names
piece_map = {'K': 'King', 'Q': 'Queen', 'R': 'Rook', 'B': 'Bishop', 'N': 'Knight'}

# Read input moves as a single line
game = input()

# Split the input into tokens
tokens = game.split()

for token in tokens:
    # Skip move numbers ending with '.'
    if token.endswith('.'):
        continue
    # Castling
    elif token in ["O-O", "O-O-O"]:
        print("King")
        print("Rook")
    else:
        # If first character is a piece letter, use mapping
        if token[0] in piece_map:
            print(piece_map[token[0]])
        else:
            # Pawn move (no initial)
            print("Pawn")
