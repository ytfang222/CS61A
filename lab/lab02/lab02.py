"""Lab 2: Lambda Expressions and Higher Order Functions"""

# Lambda Functions
lambda x: x
a = lambda x: x
a(5)
(lambda: 3)()

b = lambda x: lambda: x
c = b(88)
c() # b(88)()

d = lambda f:f(4)

d = lambda f: lambda x: f(x) 
def square(x):
    return x * x
d(square)(4)

z = 3
e = lambda x: lambda y: lambda: x + y + z
e(0)(1)()

f = lambda x: x + z
f(3)

higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
higher_order_lambda(2)(g)
higher_order_lambda(g)(2)

call_thrice = lambda f: lambda x: f(f(f(x)))
call_thrice(lambda y: y + 1)(0)

print_lambda = lambda z: print(z)
print_lambda

one_thousand = print_lambda(1000)
one_thousand

# f(|x|)
def even(f):
    def odd(x):
        if x < 0:
            return f(-x)
        return f(x)
    return odd
steven = lambda x:x
stewart = even(steven)
stewart
stewart(61)
stewart(-4)
#%%
def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie
chocolate = cake()
chocolate 
chocolate()
more_chocolate, more_cake = chocolate(), cake
more_chocolate

def snake(x,y):
    if cake == more_cake:
        return lambda: x + y
    else:
        return x + y
snake(10,20)
snake(10,20)()

cake = 'cake'
snake(10,20)

#%%

def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    "*** YOUR CODE HERE ***"    
    # higher_order_lambda = lambda f: lambda x: f(x)
    # g = lambda x: x * x
    # higher_order_lambda(g)(2)
    return lambda x: lambda y: func(x, y)

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def counter(n):
        i, count = 1, 0
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count
    return counter