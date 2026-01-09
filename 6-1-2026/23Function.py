def show():
    return "show function"

def disp(show): #(formal argument)
    
    print("disp function")
    return show()

def main():
    iRet = disp(show) #(Actual argument)
    print(iRet)

if __name__ == "__main__":
    main()