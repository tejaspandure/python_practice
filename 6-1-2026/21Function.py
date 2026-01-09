
def disp():
    def show():
        return "Show function"
    result = show() + "Disp Function"
    return result

def main():
    iRet = disp()
    print(iRet)


if __name__ == "__main__":
    main()