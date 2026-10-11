layer1_history = []
layer2_history = []

for x in range(11):
    inputs = [x, 2.2, 3.3]

    
    weights1 = [[0.2, 0.8, -0.5],
            [2, 2, 0],
            [2, 2, 2]]
    bias1 = [0 , 0 , 1]

    weights2 = [
        [0.5, -0.2, 0.1],
        [0.3, 0.4, -0.5],
    ]

    biases2 = [2, 1]

    layer_outputs = []

    layer2_outputs = []

    for neuron_weights, neuron_bias in zip(weights1, bias1):
        neuron_output = 0

        for n_input, weight in zip(inputs, neuron_weights):
            neuron_output += n_input*weight
        neuron_output += neuron_bias
        neuron_output = max(0, neuron_output)
        layer_outputs.append(neuron_output)


    for neuron_weights, neuron_bias in zip(weights2, biases2):
        neuron_output = 0

        for n_input, weight in zip(layer_outputs, neuron_weights):
            neuron_output += n_input*weight
        neuron_output += neuron_bias
        neuron_output = max(0, neuron_output)
        layer2_outputs.append(neuron_output)

    layer1_history.append(layer_outputs)
    layer2_history.append(layer2_outputs)

    print(layer2_outputs)

layer1_neuron1 = [outputs[0] for outputs in layer1_history]
layer2_neuron1 = [outputs[0] for outputs in layer2_history]

import matplotlib.pyplot as plt

x_values = list(range(11))

plt.plot(x_values, layer1_neuron1, label="Layer 1 - Neuron 1")
plt.plot(x_values, layer2_neuron1, label= "Layer 2 - Neuron 1")

plt.xlabel("First input value")
plt.ylabel("Neuron output")
plt.title("Neural Network: Output vs Input")
plt.legend()
plt.grid(True)
plt.show()