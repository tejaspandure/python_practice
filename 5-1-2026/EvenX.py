

def Calculateday(iNo):

    if iNo == "Monday":
        print("Today is monday")

    elif iNo == "Tuesday":
        print("today is tuesday")

    elif iNo == "Wednesday":
        print("Today is wednessay")

    elif iNo == "Thurday":
        print("Today is Tursday")

    else:
        print("Today is holiday")

def main():
    iValue1 = input("Enter the day: ")
    Calculateday(iValue1)



if __name__ == "__main__":
    main()