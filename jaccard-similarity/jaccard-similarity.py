def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    a = set(set_a)
    b = set(set_b)

    a_u_b = len(a | b)
    a_n_b = len(a & b)

    if a_u_b > 0:
        return a_n_b/a_u_b  
    else: 
        return 0.0
    