# This problem was asked by Pinterest.[MEDIUM]

#The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its order is an array representing whether each number is larger or smaller than the last.
#Given this information, reconstruct an array that is consistent with it. For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4].
#Solution by Greedy Approach :

from typing import List, Optional


def reconstruct_array(sym_arr: List[Optional[str]]) -> List[int]:
    sym_length = len(sym_arr)
    sum_count = sym_arr.count("+")
    first_num = sym_length - 1 - sum_count
    larger_num, smaller_num = first_num + 1, first_num - 1

    num_result = [first_num]
    for elem in sym_arr[1:]:
        if elem == "+":
            num_result.append(larger_num)
            larger_num += 1
        else:
           num_result.append(smaller_num)
           smaller_num -= 1
    return num_result
assert reconstruct_array([None, '+', '+', '-', '+']) == [1, 2, 3, 0, 4]
assert reconstruct_array([None, '-', '-', '-', '+']) == [3, 2, 1, 0, 4]
assert reconstruct_array([None, '+', '+', '+', '+']) == [0, 1, 2, 3, 4]
assert reconstruct_array([None, '-', '-', '-', '-']) == [4, 3, 2, 1, 0]
assert reconstruct_array([None, '+','-', '+','+', '-']) == [2,3, 1, 4, 5, 0]    

