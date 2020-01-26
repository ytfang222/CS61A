HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############
def num_sevens(n):
    """Returns the number of times 7 appears as a digit of n.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_sevens',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    elif n % 10 != 7:
        return num_sevens(n // 10)
    elif n % 10 == 7:
        return 1 + num_sevens(n // 10)
    #return len([a for a in list(str(n)) if a=='7'])
    
        
#%%
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def ping(index, value):
        if index == n:
            return value
        elif index % 7 == 0 or num_sevens(index) > 0:
            return pong(index+1, value-1)
        else:
            return ping(index+1, value+1)
 
    def pong(index, value):
        if index == n:
            return value
        elif index % 7 == 0 or num_sevens(index) > 0:
            return ping(index+1, value+1)
        else:
            return pong(index+1, value-1)

    return ping(index=1, value=1)

#%%
def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for i in range(amount+ 1):
        for j in range(amount//2 + 1):
            for k in range(amount//4 + 1):
                for l in range(amount//8 +1 ) :
                    for m in range(amount//16 + 1):
                        if i + j * 2 + k * 4 + l * 8 + m * 16 == amount:
                            count = count +1
                            #print(count)
    return count


def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x # Ensure x is not mutated
    [1, [2, 3], 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> x
    [[1, [1, 1]], 1, [1, 1]]
    """
    "*** YOUR CODE HERE ***" 
    #面向实用编程 :)
    b = str(lst).replace('[', '').replace(']', '').replace(' ', '')
    c = [eval(i) for i in b.split(',') if i != '']
    return(c)

#method 2 只能解决2层嵌套 
import numpy as np
x = [1, [1, [1]], 1, 1, 1]
x = np.hstack(x).tolist()
x = np.hstack(x).tolist()
print(x)

#method3  适用于一切iterable
from collections import Iterable
def flatten2(lst):
    for item in lst:
        if isinstance(item, Iterable) and not isinstance(item,(str,bytes)):
            yield from flatten2(item)
        else:
            yield item
            
a = [1, [2, [3, [4]]], [5]]
print(list(flatten2(a)))

items = [1, 2, [3, 4], (5, 6, 7), 8]
print(list(flatten2(items)))

items = [1, 2, 3, {'a':4, 'b':5}, 6, 7]
print(list(flatten2(items)))

###################
# Extra Questions #
###################

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

from operator import sub, mul

fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))
fact(5)

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda n: f(f, n))(lambda f, n: 1 if n == 1 else mul(n, f(f, sub(n, 1)))) 

