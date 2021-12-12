import numpy as np

# Get the input array from user
try:
    x: "list[float]" = list(map(float, input("Enter Input array to ANN: ").split(",")))
except ValueError:
    print("Input must be in float")
    exit()

# i should be between 0 and 3
if(len(x) < 1 or len(x) > 4):
    print("Number of input nodes should be between 1 and 4")
    exit()

# Number of internal nodes
internal_nodes = len(x) - 1
if(len(x) < 2):
    internal_nodes = 1

# Get the weights and biases from a file
raw = np.genfromtxt("weights_biases.csv", dtype = str, delimiter = ",")
weights = raw[0:-internal_nodes, 1].astype(float)
weights = np.reshape(weights, (len(x),internal_nodes))

biases = raw[-internal_nodes: len(raw), 1].astype(float)

# Calculate the weight_input matrix
weight_input = np.zeros((len(x), internal_nodes))
weight_input = []

for index, input in enumerate(x):
    weight_input.append(input * weights[index])

# This is the array with the weights multiplied with input values
weight_input = np.array(weight_input)

# Transpose the matrix so that each weight_input comes in one row
weight_input = weight_input.transpose()

# Sum all weights-input combos and add biases
output = []
for index, row in enumerate(weight_input):
    output.append(np.sum(row) + biases[index])

print("Output values: " + str(output))
