
# 1) Recursive multiplication using repeated addition
def multix(a, b):
    if b==0:
        return 0
    elif b>0:
        return a+multix(a,b-1)
    else:
        return -multix(a,-b)

# 2) Recursive power without using **
def power(b, e):#e=exponent
    if e == 0:
        return 1
    return b* power(b,e-1)

# 3) Countdown from n to 0
def countdown(n):
    if n<0:
        return print(n)
    countdown(n - 1)

# 4) Count up from 0 to n (modifying countdown)
def countup(n, c=0): #c=current=0
    if c>n:
        return print(c)
    countup(n,c+1)

# 5) Reverse a string recursively
def streverse(s):
    if s == "":
        return ""
    return s[-1]+streverse(s[:-1])

# 6) prime number check using recursion
def is_prime(n, d=None):#d=divisor=None
    if n <= 1:
        return False
    if d is None:
        d=n-1
    if d==1:
        return True
    if n%d==0:
        return False
    return is_prime(n,d-1)

# 7) Recursive Fibonacci with memoization
def fibmemo(n,memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibmemo(n-1,memo)+fibmemo(n-2,memo)
    return memo[n]
