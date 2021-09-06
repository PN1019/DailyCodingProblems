#This problem was asked by Google.

#The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other.
#For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

#Given two strings, compute the edit distance between them.


#solution 1: By recursion
ins_cost = 1
del_cost = 1
sub_cost = 2
def edit_distance_recurse(seq1, seq2, operations=[]):
    """Returns the Edit Distance between the provided two sequences."""
    
    if len(seq2) == 0:
        operations = operations + ([f"Delete `{seq1}` from sequence1."] if len(seq1) else [])
        return len(seq1), operations
    
    if len(seq1) == 0:
        operations = operations + ([f"Insert `{seq2}` into sequence1."] if len(seq2) else [])
        return len(seq2), operations
    
    if seq1[0] == seq2[0]:
        operations = operations + [f"Make no change for character `{seq1[0]}`."]
        return edit_distance_recurse(seq1[1: ], seq2[1: ], operations)
    
    # calculate cost if insertion was made
    ins_operations = operations + [f"Insert `{seq2[0]}` in sequence1."]
    insertion, ins_operations = edit_distance_recurse(seq1, seq2[1: ], ins_operations)
    
    # calculate cost if deletion was done
    del_operations = operations + [f"Delete `{seq1[0]}` from sequence1."]
    deletion, del_operations = edit_distance_recurse(seq1[1: ], seq2, del_operations)
    
    # calculate cost if substitution was done
    sub_operations = operations + [f"Replace `{seq1[0]}` in sequence1 with `{seq2[0]}`."]
    substitution, sub_operations = edit_distance_recurse(seq1[1: ], seq2[1: ], sub_operations)
    
    # calculate minimum cost
    min_cost = min(insertion + ins_cost, deletion + del_cost, substitution + sub_cost)
    
    if min_cost == (substitution + sub_cost):
        return min_cost, sub_operations
    elif min_cost == deletion + del_cost:
        return min_cost, del_operations
    else:
        return min_cost, ins_operations
seq1 = "kitten"
seq2 = "sitting"
score, operations = edit_distance_recurse(seq1, seq2)
print(f"Edit Distance between `{seq1}` & `{seq2}` is: {score}")
print("\nOperations performed are:\n")
for operation in operations:
    print(operation)
#Edit Distance between `kitten` & `sitting` is: 5

#Operations performed are:

#Replace `k` in sequence1 with `s`.
#Make no change for character `i`.
#Make no change for character `t`.
#Make no change for character `t`.
#Replace `e` in sequence1 with `i`.
#Make no change for character `n`.
#Insert `g` into sequence1.

# - - - - - -
#Solution2 by DP:
import numpy as np
ins_cost = 1
del_cost = 1
sub_cost = 2
def min_cost_path(cost, operations):
    
    # operation at the last cell
    path = [operations[cost.shape[0]-1][cost.shape[1]-1]]
    
    # cost at the last cell
    min_cost = cost[cost.shape[0]-1][cost.shape[1]-1]
    
    row = cost.shape[0]-1
    col = cost.shape[1]-1
    
    while row >0 and col > 0:
            
        if cost[row-1][col-1] <= cost[row-1][col] and cost[row-1][col-1] <= cost[row][col-1]:
            path.append(operations[row-1][col-1])
            row -= 1
            col -= 1
        elif cost[row-1][col] <= cost[row-1][col-1] and cost[row-1][col] <= cost[row][col-1]:
            path.append(operations[row-1][col])
            row -= 1
        else:
            path.append(operations[row][col-1])
            col -= 1
                    
    return "".join(path[::-1][1:])

def edit_distance_dp(seq1, seq2):
    
    # create an empty 2D matrix to store cost
    cost = np.zeros((len(seq1)+1, len(seq2)+1))
    
    # fill the first row
    cost[0] = [i for i in range(len(seq2)+1)]
    
    # fill the first column
    cost[:, 0] = [i for i in range(len(seq1)+1)]
    
    # to store the operations made
    operations = np.asarray([['-' for j in range(len(seq2)+1)] \
                                 for i in range(len(seq1)+1)])
    
    # fill the first row by insertion 
    operations[0] = ['I' for i in range(len(seq2)+1)]
    
    # fill the first column by insertion operation (D)
    operations[:, 0] = ['D' for i in range(len(seq1)+1)]
    
    operations[0, 0] = '-'
    
    # now, iterate over earch row and column
    for row in range(1, len(seq1)+1):
        
        for col in range(1, len(seq2)+1):
            
            # if both the characters are same then the cost will be same as 
            # the cost of the previous sub-sequence
            if seq1[row-1] == seq2[col-1]:
                cost[row][col] = cost[row-1][col-1]
            else:
                
                insertion_cost = cost[row][col-1] + ins_cost
                deletion_cost = cost[row-1][col] + del_cost
                substitution_cost = cost[row-1][col-1] + sub_cost
                
                # calculate the minimum cost
                cost[row][col] = min(insertion_cost, deletion_cost, substitution_cost)
                
                # get the operation
                if cost[row][col] == substitution_cost:
                    operations[row][col] = 'S'
                    
                elif cost[row][col] == ins_cost:
                    operations[row][col] = 'I'
                else:
                    operations[row][col] = 'D'
                
    return cost[len(seq1), len(seq2)], min_cost_path(cost, operations)
seq1 = "kitten"
seq2 = "sitting"
score, operations = edit_distance_dp("kitten", "sitting")
print(f"Edit Distance between `{seq1}` & `{seq2}` is: {score}")
print("\nOperations performed are:\n")
for operation in operations:
    if operation == '-':
        print('No Change.')
    elif operation == 'I':
        print('Insertion')
    elif operation == 'D':
        print('Deletion')
    else:
        print('Substitution')
#Edit Distance between `kitten` & `sitting` is: 5.0

#Operations performed are:

#Substitution
#No Change.
#No Change.
#No Change.
#Substitution
#No Change.
#Deletion
    
    
