'''
Matrix Walk
Given a square matrix, walk along the matrix according to a specified path and return a list of elements based on the path.

Paths:

    • "L": Start from the top-left corner and traverse in an "L" shape.

    • "Z": Start from the top-left corner and traverse the matrix in a "Z" shape.

    • "O": Start from the top-left corner and traverse the matrix clockwise in an "O" shape.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition. You can define helper functions if needed, but the actual solution should be in the given function template.

Example

For matrix

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
    • L-shape: [1, 4, 7, 8, 9]

    • Z-shape: [1, 2, 3, 5, 7, 8, 9]

    • O-shape: [1, 2, 3, 6, 9, 8, 7, 4]

Note: "L" has 2 private test cases where "Z" and "O" has one private test case each
'''
def walk_matrix(M, shape):
    """
    Walk along the matrix M according to the specified shape and return the path.

    Args:
        M (list of lists): The square matrix.
        shape (str): Path shape, one of "L", "O", or "Z".

    Returns:
        list: Path along the matrix according to the shape.
    """
    path = []
    n = len(M)  # Assuming square matrix

    if shape == "L":
        # Traverse down the first column
        for i in range(n):
            path.append(M[i][0])
        # Traverse right along the bottom row
        for j in range(1, n):
            path.append(M[n-1][j])

    elif shape == "O":
        # Top row
        for j in range(n):
            path.append(M[0][j])
        # Right column (excluding corners)
        for i in range(1, n-1):
            path.append(M[i][n-1])
        # Bottom row reversed
        for j in reversed(range(n)):
            path.append(M[n-1][j])
        # Left column reversed (excluding corners)
        for i in reversed(range(1, n-1)):
            path.append(M[i][0])

    elif shape == "Z":
        # Top row
        for j in range(n):
            path.append(M[0][j])
        # Diagonal from top-right to bottom-left
        for k in range(1, n-1):
            path.append(M[k][n-1-k])
        # Bottom row
        for j in range(n):
            path.append(M[n-1][j])

    else:
        raise ValueError("Invalid shape. Must be 'L', 'O', or 'Z'.")

    return path
