import numpy as np
from itertools import chain



'''
Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all
cells of the grid with digits from 1 to 9,so that each column, each row, and
each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9. 
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true
'''
nums = set(range(1, 10))
def validSolution(board):
    a = np.array(board)
    r = range(0, 9, 3)
    return all(set(v.flatten()) == nums for v in chain(a, a.T, (a[i:i+3, j:j+3] for i in r for j in r)))

'''
Create a function taking a positive integer as its parameter and returning a string containing 
the Roman Numeral representation of that integer.Modern Roman numerals are written by expressing 
each digit separately starting with the left most digit and skipping any digit with a value of zero. 
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM,
 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:
'''
def solution(n):
    roman=[['','I','II','III','IV','V','VI','VII','VIII','IX'],
       ['','X','XX','XXX','XL','L','LX','lXX','LXXX','XC'],
       ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'] ]
    r=[]
    m, n = divmod(n, 1000)
    r.append('M'*m)
    for i in range(2, -1, -1):
        m, n = divmod(n, 10 ** i)
        if m:
            r.append(roman[i][m])
    return  ''.join(r)

'''
This is a very simply formulated task. Let's call an integer number N 'green' if N² ends with all
of the digits of N. Some examples:
5 is green, because 5² = 25 and 25 ends with 5.
11 is not green, because 11² = 121 and 121 does not end with 11.
376 is green, because 376² = 141376 and 141376 ends with 376.
Your task is to write a function green that returns nth green number, starting with 1 - green (1) == 1
'''
GREEN = [0, 1]
p, f, s = 1, 5, 6
def green(n):
    global p, f, s
    while n >= len(GREEN):
        q = 10 * p
        f, s = f**2 % q, (1 - (s-1)**2) % q
        print(f,s,p,q)
        if s < 0: s += q
        GREEN.extend(sorted(n for n in (f, s) if n > p))
        p = q
    return GREEN[n]

''''
Complete the function/method (depending on the language) to return true/True when
its argument is an array that has the same nesting structure as the first array.
# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
'''
def same_structure_as(original,other):
    lst=[len(i) if isinstance(i,list) else 1 for i in original]
    lst1 = [len(i) if isinstance(i,list) else 1 for i in other]
    for i in range(0,len(lst)):
        if lst[i] is not lst1[i]:
            return False
    return True

