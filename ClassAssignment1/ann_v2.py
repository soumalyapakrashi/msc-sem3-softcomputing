import numpy as np

# Get the input array from user
x = np.genfromtxt("input.txt", dtype = float, delimiter = ",")

# All input values should be valid float values.
# This is required because if a non-float value is present in the input, the above
# function, instead of throwing an error, puts NaN in its place!
if(np.isnan(np.sum(x))):
    print("Input values should be in float")
    exit()
    
# Number of inputs should be between 1 and 4
if(len(x) < 1 or len(x) > 4):
    print("Number of input nodes should be between 1 and 4")
    exit()

# Number of internal nodes
internal_nodes = 1 if (len(x) < 2) else (len(x) - 1)
    
# Get the weights and biases from a file
raw = np.genfromtxt("weights_biases.csv", dtype = str, delimiter = ",")[:,1].astype(float)
weights = np.reshape(raw[0:-internal_nodes], (len(x), internal_nodes))
biases = raw[-internal_nodes: len(raw)]

output = np.dot(x, weights) + biases

print(f"Input values: {str(x)}\nOutput values: {str(output)}")
