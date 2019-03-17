X = {1, 3, 5};
n = 5;

"""
optimised problem wit DP
"""
def staircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n];


print (staircase(n,X));
print (staircase(4,{1,2}));

"""
Initial problem design
"""
def staircase(n):

    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

print(staircase(4));