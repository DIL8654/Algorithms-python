import time;
from functools import reduce;
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


"""

Optimized without Divition   and with upper boud product and lowerbound product

complexity is O(n) here space complexity is O(n)

"""

def calculateNewArray4(x):

    start = time.time();

    upperboundProduct = [1 for _ in range(len(x))];
    lowerboundProduct = [1 for _ in range(len(x))];
    finalProduct = [1 for _ in range(len(x))];
    temp = 1;
    for i in range(len(x)):
        upperboundProduct[i] *= temp;
        temp*=x[i];

    temp = 1;

    for j in reversed(range(len(x))):
        lowerboundProduct[j] *= temp;
        temp *= x[j];


    for p in range(len(x)):
        finalProduct[p] = lowerboundProduct[p]*upperboundProduct[p];

    end = time.time()
    print("time for calculateNewArray4 in milliseconds ", (end - start) * 1000);

    return finalProduct;

print(calculateNewArray4(X));


"""

Optimized without Divition and space complexity   and with upper boud product and lowerbound product

complexity is O(n) here space complexity is O(1)

"""

def calculateNewArray5(x):

    start = time.time();

    upperboundProduct = [1 for _ in range(len(x))];
    finalProduct = [1 for _ in range(len(x))];
    temp = 1;
    for i in range(len(x)):
        upperboundProduct[i] *= temp;
        temp*=x[i];

    temp = 1;

    for j in reversed(range(len(x))):
        upperboundProduct[j] *= temp;
        temp *= x[j];

    end = time.time()
    print("time for calculateNewArray5 in milliseconds ", (end - start) * 1000);

    return upperboundProduct;

print(calculateNewArray5(X));