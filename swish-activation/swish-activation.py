import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    input = np.asarray(x)
    sig = 1/(1+np.exp(-input))
    return input * sig
    pass