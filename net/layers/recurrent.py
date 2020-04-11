import numpy as np
from net.layers.layer import Layer

class Recurrent(Layer):
    def __init__(self, input_size, output_size):
        super().__init__((1, input_size), (1, output_size))
        self.weights = np.random.randn(input_size, output_size) / np.sqrt(input_size + output_size)
        self.weights2 = np.random.randn(1, output_size) / np.sqrt(input_size + output_size)
        self.bias = np.random.randn(1, output_size) / np.sqrt(input_size + output_size)
        self.output = np.zeros((1, output_size))
        self.last_output = None

    def forward(self, input):
        self.input = input
        self.last_output = self.output
        self.output = np.dot(input, self.weights) + (self.last_output * self.weights2) + self.bias
        return self.output

    def backward(self, output_error):
        return np.dot(output_error, self.weights.T), [
            np.dot(self.input.T, output_error),
            output_error * self.last_output,
            output_error
        ]

    def update(self, updates):
        self.weights += updates[0]
        self.weights2 += updates[1]
        self.bias += updates[2]
