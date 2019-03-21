# Algorithms
This repository will contain solution for interview questions asked from the popular companies and some questions published in the internet as well.

## staircaseproblem.py has the below problem.
There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of      unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:


         1, 1, 1, 1

         2, 1, 1
         
         1, 2, 1
         
         1, 1, 2
         
         2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.

---

## ListHasNumberPair.py
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

---
## newArrayWithProductOfOtherElements.py

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division? see the methods calculateNewArray4 and calculateNewArray5

---
## ConstructPairAndReturnFirstAndLast.py

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
         
         def cons(a, b):
               def pair(f):
                  return f(a, b)
               return pair
    
         
Implement car and cdr.
