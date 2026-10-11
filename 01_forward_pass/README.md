# Forward Pass in a Neural Network

This experiment explores how a simple feedforward neural network processes input values through two layers of neurons using Python.

## What I Implemented

- Defined inputs, weights, and biases manually.
- Calculated weighted sums for individual neurons.
- Applied the ReLU activation function.
- Passed the outputs of the first layer to the second layer.
- Changed an input value and plotted the outputs of selected neurons using Matplotlib.

## How It Works

Each neuron calculates a weighted sum of its inputs and adds a bias:

[
z = ∑(w(i)*x(i)) + b
]

The ReLU activation function is then applied:

[
{ReLU}(z) = max(0,z)
]

The output is passed to the next layer, which performs its own calculations.

## Experiment

I varied one input value while keeping the other inputs, weights, and biases fixed. I then plotted the outputs of selected neurons to observe how their values changed.

This helped me understand the relationship between inputs, weights, biases, and activation functions.

## Technologies Used

- Python
- NumPy
- Matplotlib

## Current Limitations

The weights and biases are manually assigned. The network performs a forward pass but does not train itself or update its weights based on data.

## What I Learned

This experiment helped me understand how neurons calculate outputs, how information flows between layers, and how ReLU affects the results.

