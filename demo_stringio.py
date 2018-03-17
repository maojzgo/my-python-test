from io import StringIO

f=StringIO()
f.write("hello")
print(f.tell())
f.seek(0)
print(f.tell())
s=f.readline()

print(s)