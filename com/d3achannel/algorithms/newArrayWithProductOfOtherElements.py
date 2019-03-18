import  time;
from functools import reduce ;
import numpy;
X = [1,2,3,4,5];


"""

initial implementation with O(n^2)

"""
def calculateNewArray(x):
    start = time.time();

    n = [1 for _ in range(len(X))];
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j:
                n[i] *= x[j];
    end = time.time()
    print("time for calculateNewArray in milliseconds ", (end - start)*1000);
    return n;

print(calculateNewArray(X));

"""

Optimized with Divition  and using numpy
complexity is O(n)

"""
def calculateNewArray2(x):

    start = time.time();

    n = [1 for _ in range(len(x))];
    sumvalue  = numpy.prod(x);

    for i in range(len(x)):
        n[i] = sumvalue/x[i];

    end = time.time()
    print("time for calculateNewArray2 in milliseconds ", (end - start) * 1000);

    return n;

print(calculateNewArray2(X));

"""

Optimized with Divition  and using reduce((lambda x, y: x * y), list1) 

complexity is O(n)

"""

def calculateNewArray3(x):

    start = time.time();

    n = [1 for _ in range(len(x))];
    sumvalue  = reduce((lambda x, y: x * y), x)

    for i in range(len(x)):
        n[i] = sumvalue/x[i];

    end = time.time()
    print("time for calculateNewArray3 in milliseconds ", (end - start) * 1000);

    return n;

print(calculateNewArray3(X));