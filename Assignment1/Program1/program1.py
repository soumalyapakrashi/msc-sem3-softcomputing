matrix = []
transposed_matrix = []
N = 0
M = 0

# Get the matrix from input file. It is assumed that the input will be present in a file called "input.txt"
file = None

try:
    file = open("input.txt", "r")
except FileNotFoundError:
    print("Input file not present. Input matrix must be given in a file called \"input.txt\"")
    exit()

isFirstRow = True
try:
    for row in file:
        row = row.strip()  # Remove extra unwanted leading and trailing spaces
        # Get the number of rows and columns
        if(isFirstRow == True):
            N, M = map(int, row.split(" "))
            isFirstRow = False

        else:
            row_list = list(map(int, row.split(" ")))
            matrix.append(row_list)
except:
    print("Incorrect input data given")
    exit()
finally:
    file.close()

# Check whether N number of rows have been given and all the rows have M number of columns
if(len(matrix) != N):
    print("An incorrect number of rows are present in input matrix")
    exit()

for i in range(N):
    if(len(matrix[i]) != M):
        print("Every row should have specified number of elements")
        exit()

# Transpose the matrix
for i in range(M):
    row_list = []
    for j in range(N):
        row_list.append(matrix[j][i])
    transposed_matrix.append(row_list)

# Write back the transposed matrix to the output file named "output.txt"
file = open("output.txt", "w")
for i in range(M):
    string = ""
    for j in range(N):
        string += str(transposed_matrix[i][j]) + " "
    string = string.strip() + "\n"
    file.write(string)
file.close()
