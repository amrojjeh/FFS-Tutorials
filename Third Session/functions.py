import time

# Some basics:
# return value substitues the calling function with the evaluated expression
# So, if I call fib_recursive(0),
# the code will `return 0` as instructed by the if statement.
# That means, the call fib_recursive(0) BECOMES 0
# That is why print(fib_recursive(0)) prints 0, because
# it's the same as print(0). TL;DR:
# print(fib_recursive(0) + 1) = print( 0 + 1) = print(1): prints 1


# index: 0, fib: 0
# index: 1, fib: 1
# index: 2, fib: 1
# index: 3, fib: 2
# index: 4, fib: 3
def fib_linear(index):
    prev = 1
    prev_prev = 0
    current = 1
    for i in range(1, index):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
    return current

def fib_recursive(index):
    if index <= 0:
        return 0
    if index == 1:
        return 1
    # index is guaranteed to be 2 at this point
    return fib_recursive(index - 1) + fib_recursive(index - 2)

# Understanding the "normal" version (with index=5)
# With any determinsitic recursive function, you should work top to bottom:
# fib(5) = fib(4) + fib(3)
# fib(4) = fib(3) + fib(2)
# fib(3) = fib(2) + fib(1)
# fib(2) = fib(1) + fib(0)
# fib(1) = 1
# fib(0) = 0
# Now we work bottom up, by substituting values:
# fib(5) = fib(4) + fib(3) = 3 + 2 = 5
# fib(4) = fib(3) + fib(2) = 2 + 1 = 3
# fib(3) = fib(2) + fib(1) = 1 + 1 = 2
# fib(2) = fib(1) + fib(0) = 1 + 0 = 1
# fib(1) = 1
# fib(0) = 0

# Going through the process of writing it should make it much easier to understand

def fib_recursive_optimized(index, a=0, b=1):
    if index <= 0:
        return a
    if index == 1:
        return b
    return fib_recursive_optimized(index - 1, b, a + b)

# Understanding the optimized version (with index=5):
# fib(5, 0, 1) = fib(4, 1, 1) = 5 |  0, 1, 1, 2, 3, 5
#                                   ^a  ^b
# fib(4, 1, 1) = fib(3, 1, 2) = 5 | 0, 1, 1, 2, 3, 5
#                                     ^a  ^b
# fib(3, 1, 2) = fib(2, 2, 3) = 5 | 0, 1, 1, 2, 3, 5
#                                         ^a ^b
# fib(2, 2, 3) = fib(1, 3, 5) = 5 | 0, 1, 1, 2, 3, 5
#                                            ^a ^b
# fib(1, 3, 5) = 5 | 0, 1, 2, 3, 5
#                             ^a ^b

# The optimized function solves the sequence in its arugments!



index = int(input("Enter an index for the fibonacci sequence: "))

start = time.time()
result = fib_linear(index)
duration = time.time() - start
string = "The function %s took %.2f"
# function.__name__ is the name of the function
print(string % (fib_linear.__name__, duration))

result = fib_recursive_optimized(index)
duration = time.time() - start
print(string % (fib_recursive_optimized.__name__, duration))

# I placed fib_recursive at the last since it takes the longest to run.
# Perhaps you can figure out why? (I go over it in the video)
result = fib_recursive(index)
duration = time.time() - start
print(string % (fib_recursive.__name__, duration))


