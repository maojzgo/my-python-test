import random, string

def rand_str(num, length=7):
    #f = open('Activation_code.txt', 'w')
    chars = string.ascii_letters + string.digits
    for i in range(num):
        s = [random.choice(chars) for i in range(length)]
        print("".join(s))
    #     f.write('{0}\n'.format(''.join(s)))
    # f.close()



if __name__ == '__main__':
    rand_str(200)
