# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd

count = 0  # total number of operations executed in f(n)


def f(n):
    """f(n) = f(n-1)+f(n-2)"""
    global count
    x = 0  # correction from 1 to 0
    y = 1
    z = n
    count = 0
    # Given x, y, z

    for i in range(2, n + 1):  # xxx correction from n to n+1
        z = x + y
        x = y
        y = z
        count += 1

    return z


n = 30

d = {"index": [], "count_A": [], "fib_A": [], }
# that is the list of colummn

for i in range(n):
    x = f(i)

    d["index"].append(i)
    # "index" col assigns i sequence to dataframe

    d["count_A"].append(count)
    # "count_A" col assigns count sequence to dataframe

    d["fib_A"].append(x)
    # "fib_A" col assigns x sequence to dataframe

df1 = pd.DataFrame(d)
# Assign data frame(data lists) for d

d = df1["count_A"].plot(title="Algorithm A: Linear Time Coplexity", legend=True)
# draw graph

df1

count = 0
def g(n):
    """g(n) = g(n-1)+g(n-2)"""
    global count
    if n <2:
        return n
    count += 1
    return g(n-1)+g(n-2)

n=30



d = [ [1,2,3], [4,5,6], [7,8,9]]
df = pd.DataFrame(d)

w = df.loc [2 ]
x = df.loc[ [2] ]
y = df [ 2 ]
z = df [ [2] ]

d = {"index_B": [], "count_B": [], "fib_B": []}
for i in range(n):
    count = 0
    x = g(i)

    d["index_B"].append(i)
    d["fib_B"].append(x)
    d["count_B"].append(count)

df2 = pd.DataFrame(d)
d = df2["count_B"].plot(title="Algorithm B: Exponentail Time Coplexity", legend=True)
# count_B using g(i) shows as graph
df2

d = [ [1,1], [1,0] ]
q = pd.DataFrame (d)

count = 0
def h(q,n):
    global count
    if n <=1:
        return q
    r = h(q,n//2)             # r= (q**n//2)
    r = r@r; count += 1       # q**n = r*r
    if n%2==1:
        r = r@q; count += 1   # q**n = r*r*q. if n%2==1
    return r

n=30

d = {"index":[], "count_C":[],"fib_C":[]}

for i in range(n):
        count = 0
        x= h(q,i)
        d["index"].append(i)
        d["fib_C"].append(x[0][1])
        d["count_C"].append(count)


df3 = pd.DataFrame(d)
d = df3["count_C"].plot(title = "Algorithm C: Logarithmic Time Coplexity",legend = True)
#count_C using h(q,i) shows graph
df3


df1["count_A"].plot(title = "Runtime Comparison of Algorithm A and C",legend = True)
df3["count_C"].plot(title = "Runtime Comparison of Algorithm A and C",legend = True)
#Show count_A and count_C(count_A and count_C in Q1 and Q3).

df1
df3


df1["count_A"].plot(title = "Runtime Comparison of Algorithm A,B and C",legend = True)
df2["count_B"].plot(title = "Runtime Comparison of Algorithm A,B and C",legend = True)
df3["count_C"].plot(title = "Runtime Comparison of Algorithm A,B and C",legend = True)
"""count_A, count_B, count_C shows graph but count_A and count_C are too little value, 
    so the line is showing like horizontal straight line"""

