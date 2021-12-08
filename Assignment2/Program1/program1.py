class Matrix:

    @staticmethod
    def __validateMatrix(matrix: "list[list]") -> bool:
        # It has been mentioned that the size of the matrix will be 3x3. We validate that here
        rows = len(matrix)
        if(rows != 3):
            return False
        for row in matrix:
            if(len(row) != rows):
                return False
        return True
    

    @staticmethod
    def __getSize(matrix: "list[list]") -> int:
        return len(matrix)
    
    @staticmethod
    def __swap(nos1: int, nos2: int) -> tuple:
        temp = nos1
        nos1 = nos2
        nos2 = temp
        return (nos1, nos2)

    

    @staticmethod
    def transpose(matrix: "list[list]") -> "list[list]":
        if(Matrix.__validateMatrix(matrix) == False):
            raise AssertionError("The given matrix is not valid")
        
        # Create a new matrix of the same size as the input matrix
        transpose = []
        for i in range(Matrix.__getSize(matrix)):
            temp = []
            for j in range(Matrix.__getSize(matrix)):
                temp.append(0)
            transpose.append(temp)

        # Perform the transpose
        for i in range(Matrix.__getSize(matrix)):
            for j in range(Matrix.__getSize(matrix)):
                transpose[j][i] = matrix[i][j]
        
        return transpose
    

    @staticmethod
    def determinant(matrix: "list[list]") -> int:
        if(Matrix.__validateMatrix(matrix) == False):
            raise AssertionError("The given matrix is not valid")
        
        # As 3x3 matrix has been specified, do it in easy way!! :)
        determinant = (matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1]))) - \
            (matrix[0][1] * ((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0]))) + \
            (matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0])))
        
        return determinant


    @staticmethod
    def adjoint(matrix: "list[list]") -> "list[list]":
        if(Matrix.__validateMatrix(matrix) == False):
            raise AssertionError("The given matrix is not valid")
        
        rows = Matrix.__getSize(matrix)
        columns = rows
        
        # Create a new matrix equal to the dimension of the transpose of the input matrix
        adjoint = []
        for i in range(columns):
            temp = []
            for j in range(rows):
                temp.append(0)
            adjoint.append(temp)
        
        # Generate the adjoint of the input matrix
        for i in range(rows):
            for j in range(columns):
                # Find the cofactor of matrix[i][j]
                cofactor_i1 = (i + 1) % 3
                cofactor_j1 = (j + 1) % 3
                cofactor_i2 = (i + 2) % 3
                cofactor_j2 = (j + 2) % 3

                # It may happen that the rows (or columns) may get interchanged. For example, when working
                # with middle row, the two rows of the cofactor matrix becomes interchanged. So we swap them.
                if(cofactor_i2 < cofactor_i1):
                    cofactor_i1, cofactor_i2 = Matrix.__swap(cofactor_i1, cofactor_i2)
                if(cofactor_j2 < cofactor_j1):
                    cofactor_j1, cofactor_j2 = Matrix.__swap(cofactor_j1, cofactor_j2)
                
                # Calculate the cofactor
                cofactor = (matrix[cofactor_i1][cofactor_j1] * matrix[cofactor_i2][cofactor_j2]) - (matrix[cofactor_i1][cofactor_j2] * matrix[cofactor_i2][cofactor_j1])

                value = cofactor * ((-1) ** (i + j))

                adjoint[j][i] = value
        
        return adjoint
    

    @staticmethod
    def inverse(matrix: "list[list]") -> "list[list]":
        if(Matrix.__validateMatrix(matrix) == False):
            raise AssertionError("The given matrix is not valid")
        
        determinant = Matrix.determinant(matrix)
        adjoint = Matrix.adjoint(matrix)

        # A matrix having determinant = 0 have no inverse
        if(determinant == 0):
            raise AssertionError("The given matrix has determinant = 0")

        inverse = []
        # Inverse can only be calculated for square matrices
        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix)):
                temp.append(0)
            inverse.append(temp)
        
        # Calculate inverse
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                inverse[i][j] = adjoint[i][j] / determinant
        
        return inverse
               

if(__name__ == "__main__"):
    matrix = []

    try:
        with open("input.txt", "r") as file:
            for row in file:
                temp = list(map(int, row.split(" ")))
                matrix.append(temp)
    except FileNotFoundError:
        print("File not found. Input file should be named 'input.txt'")
    
    with open("output.txt", "w") as file:
        # Calculate transpose
        file.write("Transpose:\n")
        output = Matrix.transpose(matrix)
        for row in output:
            temp = ""
            for element in row:
                temp += str(element) + " "
            file.write(temp + "\n")

        # Calculate determinant
        file.write("\nDeterminant: ")
        output = Matrix.determinant(matrix)
        file.write(str(output) + "\n\n")

        # Calculate adjoint
        file.write("Adjoint:\n")
        output = Matrix.adjoint(matrix)
        for row in output:
            temp = ""
            for element in row:
                temp += str(element) + " "
            file.write(temp + "\n")

        # Calculate inverse
        file.write("\nInverse:\n")
        output = Matrix.inverse(matrix)
        for row in output:
            temp = ""
            for element in row:
                temp += str(element) + " "
            file.write(temp + "\n")
