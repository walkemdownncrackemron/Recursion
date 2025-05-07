
# 1) Recursive multiplication using repeated addition
# (a*b = a + a + ... + a (b times))
# (a*b = a + a + ... + a (-b times) if b<0)
def multix(a, b):
    if b==0:
        return 0
    elif b>0:
        return a+multix(a,b-1)
    else:
        return -multix(a,-b)

for i in range(1, 10): #loop through 1 to 9
    # Test multiplication function
    for j in range(1, 10):
        print(f"{i}*{j}={multix(i,j)}")
    print("===")

# 2) Recursive power without using **
# (b^e = b*b*b...*b (e times))
# (b^e = 1/b^(-e) if e<0)
def power(b, e):#e=exponent
    if e == 0:
        return 1
    return b* power(b,e-1)

if __name__ == "__main__":
    # Test power function
    b = float(input("Base: "))
    e = int(input("Exponent: "))
    print(f"{b}^{e} = {power(b, e)}")

# 3) Countdown from n to 0
# (n,n-1,n-2,...,0)
# (n<0, print n and return)
def countdown(n):
    if n<0:
        return print(n)
    countdown(n - 1)
    return print(n)

for i in range(10):
    countdown(i)
    print("===")

# 4) Count up from 0 to n (modifying countdown)
# (0,1,2,...,n)
# (n<0, print n and return)
def countup(n, c=0): #c=current=0
    if c>n:
        return print(c)
    countup(n,c+1)
    return print(c)

for i in range(10):
    countup(i)
    print("===")

# 5) Reverse a string recursively
# (s="abcde" => "edcba")
# (s="", return "")
def streverse(s):
    if s == "":
        return ""
    return s[-1]+streverse(s[:-1])

if __name__=="__main__":
    s = input("Enter string: ")
    print(f"Reversed string: {streverse(s)}")

# 6) prime number check using recursion
# (n=7, d=6, d-1, d-2,...,1)
# (n<=1, return False)
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

for i in range(1, 101):
    if is_prime(i):
        print(f"{i} is prime")
    else:
        print(f"{i} not prime")

# 7) Recursive Fibonacci with memoization
# (fib(0)=0, fib(1)=1, fib(2)=fib(1)+fib(0), fib(3)=fib(2)+fib(1),...)
# (fib(n)=fib(n-1)+fib(n-2))
#memoization: store previously computed values in a dictionary to avoid recomputation
def fibmemo(n,memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibmemo(n-1,memo)+fibmemo(n-2,memo)
    return memo[n]

for i in range(1001):
    print(f"fibmemo({i})={fibmemo(i)}")
