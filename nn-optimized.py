import numpy as np
np.random.seed(1)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_output_to_derivative(output):
    return output * (1 - output)


# inputs
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# outputs
y = np.array([[0, 0, 1, 1]]).T

W_1 = 0.01 * np.random.randn(3, 4)
W_2 = 0.01 * np.random.randn(4, 1)

alpha = 10
gamma = 0.9

momentum_layer_2 = 0
momentum_layer_1 = 0
for _ in range(100):
    
    layer_1 = sigmoid(np.dot(X, W_1))
    layer_2 = sigmoid(np.dot(layer_1, W_2))
    layer_2_error = layer_2 - y
    layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)
    layer_1_error = np.dot(layer_2_delta, W_2.T)
    layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)
    
    momentum_layer_2 = gamma*momentum_layer_2 + alpha * np.dot(layer_1.T, layer_2_delta)
    W_2 = W_2 - momentum_layer_2
    momentum_layer_1 = gamma*momentum_layer_1 + alpha * np.dot(X.T, layer_1_delta)
    W_1 = W_1 - momentum_layer_1
    
print("Loss: {}".format(np.linalg.norm(layer_2 - y)))