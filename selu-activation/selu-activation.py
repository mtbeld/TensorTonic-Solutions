import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    input = np.asarray(x)
    cond_list = [input > 0 , input <= 0]
    choice_list = [lam * input, lam * alpha * (np.exp(input)-1)]
    return np.select(cond_list, choice_list)
    pass
