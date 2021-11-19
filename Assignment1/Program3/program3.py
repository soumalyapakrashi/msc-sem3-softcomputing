N = 0
A = []
B = []

# Gets input from a file named "input.txt"
def getInput():
    global N, A, B

    try:
        with open("input.txt", "r") as file:
            row_number = 1
            for row in file:
                row = row.strip()
                # Get the value of N
                if(row_number == 1):
                    N = int(row)
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
        print("Input must be provided in a file named \"input.txt\"")
        exit()
    except:
        print("Invalid input")
        exit()


# Write matrix along with info to "output.txt"
def writeOutput(file, text, matrix):
    file.write(text + "\n")
    for i in range(N):
        string = ""
        for j in range(N):
            string += str(matrix[i][j]) + " "
        string = string.strip() + "\n"
        file.write(string)
    file.write("\n")


# Calculates dot product (normal multiplication) of 2 matrices and returns result
def calculateDotProduct() -> list:
    product = []

    for i in range(N):
        row_list = []
        for j in range(N):
            prod = 0
            for k in range(N):
                prod += A[i][k] * B[k][j]
            row_list.append(prod)
        product.append(row_list)
    
    return product


if(__name__ == "__main__"):
    getInput()

    with open("output.txt", "w") as file:
        matrix = calculateDotProduct()
        writeOutput(file, "Dot Product", matrix)    
