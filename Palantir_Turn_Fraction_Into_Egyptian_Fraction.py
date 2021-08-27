# This problem was asked by Palantir.

# The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one.
# For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

# Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.

#Solution
#Every positive fraction can be represented as sum of unique unit fractions.
#A fraction is unit fraction if numerator is 1 and denominator is a positive integer,
#for example 1/3 is a unit fraction. Such a representation is called Egyptial Fraction as it was used by ancient Egyptians.
#Following are few examples:
#Egyptian Fraction Representation of 2/3 is 1/2 + 1/6
#Egyptian Fraction Representation of 6/14 is 1/3 + 1/11 + 1/231
#Egyptian Fraction Representation of 12/13 is 1/2 + 1/3 + 1/12 + 1/156

import math
from fractions import Fraction


def getEgyptians(fraction, prev_fracs=list()):
    if fraction.numerator == 1:
        prev_fracs.append(fraction)

        return prev_fracs

    egpyt_frac = Fraction(1, math.ceil(
        fraction.denominator / fraction.numerator))
    prev_fracs.append(egpyt_frac)

    new_frac = fraction - egpyt_frac
    return getEgyptians(new_frac, prev_fracs)
## Test code ##
assert getEgyptians(Fraction(4, 13)) == \	
            [Fraction(1, 4), Fraction(1, 18), Fraction(1, 468)]
assert getEgyptians(Fraction(6, 14)) == \
    [Fraction(1, 3), Fraction(1, 11), Fraction(1,231)]
