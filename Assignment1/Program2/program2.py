A = []
B = []
N = 0
M = 0

def getInput():
    # If this is not given, during assignment, python assumes new variables with the same names are being made
    global A, B, N, M
    # Input is given in a file called "input.txt"
    try:
        with open("input.txt", "r") as file:
            row_number = 1
            for row in file:
                row = row.strip()
                # Get the number of rows and columns in the matrices
                if(row_number == 1):
                    N, M = map(int, row.split(" "))
                # Get matrix A
                elif(row_number <= N + 1):
                    row_list = list(map(int, row.split(" ")))
                    A.append(row_list)
                # Get matrix B
                else:
                    row_list = list(map(int, row.split(" ")))
                    B.append(row_list)
                
                row_number += 1
            
    except FileNotFoundError:
        print("Input must be given in a file named \"input.txt\"")
        exit()


# Iterate over all the elements in each of the matrices and perform addition
def addMatrices() -> list:
    sum_matrix = []
    for i in range(N):
        row_matrix = []
        for j in range(M):
            sum = A[i][j] + B[i][j]
            row_matrix.append(sum)
        sum_matrix.append(row_matrix)
    return sum_matrix


# Iterate over all the elements in each of the matrices and perform subtraction
def subtractMatrices() -> list:
    diff_matrix = []
    for i in range(N):
        row_matrix = []
        for j in range(M):
            row_matrix.append(A[i][j] - B[i][j])
        diff_matrix.append(row_matrix)
    return diff_matrix


# Iterate over all the elements in each of the matrices and perform multiplication
def multiplyMatrices() -> list:
    product_matrix = []
    for i in range(N):
        row_matrix = []
        for j in range(M):
            row_matrix.append(A[i][j] * B[i][j])
        product_matrix.append(row_matrix)
    return product_matrix


# Iterate over all the elements in each of the matrices and perform division
def divideMatrices() -> list:
    divide_matrix = []
    for i in range(N):
        row_matrix = []
        for j in range(M):
            row_matrix.append(round(A[i][j] / B[i][j], 2))
        divide_matrix.append(row_matrix)
    return divide_matrix


# Iterate over all the elements in each of the matrices and perform modulus
def modMatrices() -> list:
    mod_matrix = []
    for i in range(N):
        row_matrix = []
        for j in range(M):
            row_matrix.append(A[i][j] % B[i][j])
        mod_matrix.append(row_matrix)
    return mod_matrix


# Write matrix along with info to "output.txt"
def writeOutput(file, text, matrix):
    file.write(text + "\n")
    for i in range(N):
        string = ""
        for j in range(M):
            string += str(matrix[i][j]) + " "
        string = string.strip() + "\n"
        file.write(string)
    file.write("\n")


if(__name__ == "__main__"):
    getInput()
    
    with open("output.txt", "w") as file:
        matrix = addMatrices()
        writeOutput(file, "Add", matrix)
        matrix = subtractMatrices()
        writeOutput(file, "Subtract", matrix)
        matrix = multiplyMatrices()
        writeOutput(file, "Multiply", matrix)
        matrix = divideMatrices()
        writeOutput(file, "Divide", matrix)
        matrix = modMatrices()
        writeOutput(file, "Mod", matrix)
