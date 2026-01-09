#keyword variable length arguments

def add(x, **num):
    z = x + num['a'] + num['b'] + num['c']
    return z

def main():
    iRet = add(5, a=5,b=3,c=5)
    print("Addition is:  %d" %iRet)


if __name__ == "__main__":
    main()