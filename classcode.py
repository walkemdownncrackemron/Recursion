#fib series using recursion
def fib1(n):
    if n==2:
        return 1
    if n==1:
        return 1
    elif n>2:
        return fib1(n-1)+fib1(n-2)

for num in range(500):
    print(f"{num}: {fib1(num)}")

#fib series using memoization
def fib2(n, memo={}):
    if n in memo:
        return memo[n]
    if n==2:
        return 1
    if n==1:
        return 1
    elif n>2:
        memo[n]=fib2(n-1,memo)+fib2(n-2,memo)
        return memo[n]

for num in range(1001):
    print(f"{num}: {fib2(num)}")

#fib series using lru_cache
from functools import lru_cache
@lru_cache(maxsize=None)
def fib3(k):
    if k==2:
        return 1
    if k==1:
        return 1
    elif k>2:
        return fib3(k-1)+fib3(k-2)

for num in range(1001):
    print(f"{num}: {fib3(num)}")

#Tower of Hanoi
def TowerOfHanoi(n, source, destination_rod, auxiliary_rod): 
    #n=num of disks, source=source rod, destination_rod=destination rod, auxiliary_rod=auxiliary rod
    if n == 1:
        print("Move disk 1 from source ", source, " to destination ", destination_rod)
        return #base case- directly move disk 1 from source to destination when n==1
    TowerOfHanoi(n - 1, source, auxiliary_rod, destination_rod)#recursive case1- move n-1 disks from source to auxiliary rod w destination as temp rod
    print("Move disk ", n, " from source ", source, " to destination ", destination_rod)# move nth disk from source to destination rod direct
    TowerOfHanoi(n - 1, auxiliary_rod, destination_rod, source)#recursive case2- move n-1 disks from auxiliary rod to destination rod w source as temp rod

n = 4
TowerOfHanoi(n, 'A', 'B', 'C')# #A,B,C are names of rods