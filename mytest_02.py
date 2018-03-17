import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print('2015-3-25')
#
# print(now.__name__)

max2=functools.partial(max,10)
m=max2(1,2,3)
print(m)