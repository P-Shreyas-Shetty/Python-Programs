import numpy as np
from itertools import product, chain

'''Program to generate the binary addition (truth)table'''

def make_binary_array(num:int, bits=16)->np.array:
    '''Convert a decimal number into equivalent binary array of 
    given resolution'''
    binary = np.fromiter(
        map(lambda n:(num//2**(bits-n-1))%2, range(bits)),
        np.int, bits)
    return binary


def make_addition_table(bits=8)->np.array:
    '''Make a truth table of adder for given bits'''
    #Create a map of arguments bit vector
    #We make two of it because an iterator can be used only once
    table = map(lambda n:make_binary_array(n, bits=bits), range(2**bits))
    tablecpy = map(lambda n:make_binary_array(n, bits=bits), range(2**bits))

    #Compute cartesian product of the LHS to produce all possible combinations
    #of input bit vectors. Then flatten the produced iterable to be fed to 
    #fromiter function of numpy to make a numpy array.The iterator is chained twice
    #because the cartesian product gives 3D array. Finally numpy array is reshaped
    #back to intended shape. The loops are avoided for the sake of speed. Avoiding
    #list conversion helps remove memory errors.
    tableX = np.fromiter(
        chain.from_iterable(
            chain.from_iterable(product(table, tablecpy))
        ),
        dtype=np.int
    ).reshape(2**(2*bits), 2, bits)
    tableY = np.fromiter(chain.from_iterable(
        map(lambda X:make_binary_array(X[0]+X[1],bits=bits+1), product(range(2**bits), range(2**bits)))
    ), np.int).reshape(2**(2*bits), bits+1)
    return tableX, tableY


    
x,y = make_addition_table(bits=10)
print(x)
