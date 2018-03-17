from collections import Counter

list=['a', 'b', 'c', 'd', 'a']

a=Counter(list)
print(a['a'])
print(type(Counter(list)))