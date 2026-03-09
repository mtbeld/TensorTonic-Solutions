import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    input = np.asarray(x, dtype=float)
    return (np.exp(input)-np.exp(-input))/(np.exp(input)+np.exp(-input))
    pass