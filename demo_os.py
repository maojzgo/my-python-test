import os

print(os.path.abspath("."))

a=os.path.splitext("/path/abc.txt")

#os.rename("abc","def")

b = os.path.dirname('.')
print(b)