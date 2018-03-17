# try:
#     f=open("D:\\mydemo.log")
#     print(f.read())
#
# except IOError as e:
#     print(e)
# finally:
#     f.close()

with open("D:/mydemo.log") as f:
    print(f.read())