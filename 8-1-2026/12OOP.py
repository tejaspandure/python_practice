class Mobile:
    def __init__(self,m):
        self.model = m

    def Model(self):
        print("Model:", self.model)
          

def main():
        mobj = Mobile("Nokia")
        mobj.Model()

if __name__ == "__main__":
    main()
