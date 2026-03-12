import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    input = np.asarray(x)
    num_dim = input.ndim
    inp_max = input.max(axis=num_dim-1, keepdims=True)
    exp_sh = np.exp(input-inp_max)
    return exp_sh/np.sum(exp_sh, axis=num_dim-1, keepdims=True)
    pass