def show():
    return "show function"

def disp(sh):
    iResult = sh() + "Disp function"
    return iResult

def main():
    iRet = disp(show)
    print(iRet)

if __name__ == "__main__":
    main()