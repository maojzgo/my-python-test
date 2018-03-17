#map reduce使用

from functools import reduce
def f(x):
    return x*x

m = map(f,[1,2,3,4,5,6,7,8,9])

a = list(m)

#print(a)


def g(a,b):
    return a*10 + b

r=reduce(g,[1,2,3,4,5,6])

print(type(r))

