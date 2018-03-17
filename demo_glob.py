import glob

a=glob.glob('./*')
print(a)

for i in sorted(glob.glob('c:/*')):
    print(i)