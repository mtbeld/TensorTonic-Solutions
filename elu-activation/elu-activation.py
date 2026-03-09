import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    input = np.asarray(x)
    return np.where(input>0, input, alpha * (np.exp(input)-1)).tolist()
        