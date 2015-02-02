
def strip_ptms(sequence):
    """
    Removes all post-translation modifications (i.e. phosphorylation,
    glycosylation, etc) from a sequence.

    Parameters
    ----------
    sequence : str

    Returns
    -------
    str
    """
    return sequence.upper()
