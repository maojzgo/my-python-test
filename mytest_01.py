#-*- coding: utf-8 -*-
# import keyword
# for a in keyword.kwlist:
#     print(a)


# str="abcd"
# print(str[1:-1])

# val = input("\n\npleace input:")
# print(val)

#import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# import sys
# print('================Python import mode==========================');
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path)

# ret=0
# for i in range(101):
#     ret+=i
# print(ret)

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
# print(add_end())
# print(add_end())

# L=[x*x for x in list(range(10))]
# for i in L:
#     print(i)

# L=[x * y for x in list(range(10)) for y in list(range(11,20))]
# for i in L:
#     print(i)

# def mysum(*args):
#     ret = 0
#     for i in args:
#         ret += i
#     return ret
# a=(1,2,3,4)
# print(mysum(9,1,2,3))

# def createCounter():
#     s=[0]
#     def counter():
#         s[0]+=1
#         return s[0]
#     return counter
# f1=createCounter()
# print(f1())
# print(f1())
# print(f1())

f = lambda x: x * x
print(f(5))