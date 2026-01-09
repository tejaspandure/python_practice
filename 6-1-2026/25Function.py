#Default arguments

def show(name, age=34):
    print(f"name { name}, age { age}")

def main():
    show(name="Ram",age=33)

if __name__=="__main__":
    main()