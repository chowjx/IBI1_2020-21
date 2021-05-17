def complement_base(base):
    """Returns  the Watson-Crick complement of a base"""
    if base in 'Aa':
        return 'T'
    elif base in 'Tt':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'

def reverse_complement(seq):
    """Compute reverse complement of a sequence"""
    
    # initialise reverse complement
    rev_seq = ''

    # loop through & populate list with reverse complement
    for base in reversed(seq):
        rev_seq += complement_base(base)

    print(rev_seq)

# Example of calling the reverse complement function with sequences in uppercase
reverse_complement('CGGATTGAC')

# Example of calling the reverse complement function with sequences in lowercase
reverse_complement('cggattgac')

# Example of calling the reverse complement function with sequences in a mix of lowercase & uppercase
reverse_complement('cGGaTTgac')