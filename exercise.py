def sum_with_while(start, end):
    """
    Calculate the sum of all numbers between start and end (inclusive) using a while loop.
    """
numbers =int(input("enter first numbers:"))



def count_vowels_in_string(input_string):
    """
    Count the number of vowels in a given string using a for loop.
    """
    pass

def filter_numbers(numbers):
    """
    Filter a list of numbers based on specific conditions using a for loop and conditionals.
    """
    pass

def fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to n terms using a while loop.
    """
    fibonacci_sequence = [0,1]
    while len(fibonacci_sequence)<n:
        next_number = fibonacci_sequence[-1]+fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
        return fibonacci_sequence
    num = int(input("Enter the number of term you want"))
    print(f"the first{n} term in fibonnaci sequence:{fibonacci_sequence(n)}")

def pascals_triangle(rows):
    """
    Generate Pascal's Triangle up to a given number of rows.
    """
    if numbers <=0:
        pascals_triangle =[]

    for i in range(numbers):
        row = [i] * (i + 1)
        for j in range(1, i):
            row[j] = pascals_triangle[i - 1][j- 1]+pascals_triangle[i - 1][j]
        pascals_triangle.append(row)

        return pascals_triangle   



    


def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi problem recursively.
    """
    if numbers == 1:
        print(f"Move disk 1 from {source} to {target}")
    tower_of_hanoi(n-1,source, auxiliary, target)
    print(f"Move disk {numbers} from {source} to {target}")

    tower_of_hanoi(n-1, auxiliary, target, source)

def find_dna_sequence(dna, sequence):
    """
    Find the first occurrence of a DNA subsequence within a larger DNA string.
    """
    if not isinstance(dna, str) or not isinstance(sequence, str):
        raise TypeError("Both dna and sequence must be strings")
    
    return dna.find(sequence)

# Example usage
dna = "ACGTACGTGACG"
sequence = "GTGA"
index = find_dna_sequence(dna, sequence)
print(f"The subsequence '{sequence}' is first found at index {index} in the DNA string.")
    

def is_palindrome(input_string):
    """
    Check if a given string is a palindrome (ignoring spaces, capitalization, and punctuation).
    """
    pass

def generate_permutations(input_string):
    """
    Return all possible permutations of a given string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    permutations = [''.join(p) for p in generate_permutations(input_string)]
    return permutations

# Example usage
perms = generate_permutations("abc")
print(perms)  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    

def is_valid_sudoku(board):
    """
    Validate a given 9x9 Sudoku board.
    """
def is_vaild_block(block):
    block = [num for num in block if num != ',']
    return len(block) == len(set(block))

def is_vaild_row(board):
    for row in board:
        if not is_valid_sudoku(row):
            return False
        return True
    
def is_vaild_column(board):
    for col in zip(*board):
        if not is_vaild_block(col):
            return False
        return True
    
def is_vaild_subgrid(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_vaild_block(subgrid):
                return False
            return False        

def solve_n_queens(n):
    """
    Find all possible solutions to the N-Queens problem.

    """
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 'Q':
            return False
        
#checking upper diagonal
    for i,j in zip(range(row, -1, -1),range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
        return False
 #checking lower diagonals
    for i, j in zip(range(row,numbers, 1), range(col, -1, -1)):
        if board[i, j ] == 'Q':
            return False
        return True
    
def solve_n_queens(board, col):
    # if col>= numbers:
    #     solve_n_queens.append([' '.join(row) for row in board])
    #     return
    
    # for i in range(numbers):
    #     if is_safe(board, i, col):
    #         board[i][col] = 'Q'
    #         solve_n_queens(board, col + 1)
    #         board[i][col] = '_'
    # solution = []
    # board = ['-'for_ in range(numbers)][for _ in range(n)]
    # solve_n_queens(board, 0)
    # return solution 
    pass 

       

def longest_common_subsequence(str1, str2):
    """
    Find the length of the longest subsequence common to both strings.
    """
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m +1):
        for j in range(1, n +1):
            if str[i - 1] == str2[j - 1]:

                #charactors match
                dp[i][j] = dp[i - 1][j - 1] + 1

        else:
            dp[i][j] = max(dp[i -1][j], dp[i][j - 1])
    return dp[m][n]        

    


    

if __name__ == "__main__":
    pass
