import time

R = [10,15,3,7];

K = 17;

"""
inital approach

"""
def findExists1(s,k):

    start = time.time()
    found = False;
    for i in range(0,len(s)- 1):
        for j in range(1, len(s)):
            if s[i] + s[j] == k:
                found = True;
    end = time.time()
    print("time for findExists1 ", end - start);
    return found;

print(findExists1(R,K));

"""
Optimised approach
"""
def findExists2(s,k):
    start = time.time()
    cache = { 0 for _ in range(s)};
    cache[0] = s[0];
    for i in range(1,len(s)):
        diff = k-s[i];
        if diff in cache:
            cache[i] = diff;
            return True;
    end = time.time()
    print("time for findExists2 ", end - start);

print(findExists1(R,K));