def display(ff):
        output = "{"
        for i in range(len(ff)):
            output += str(ff[i])
            if i < len(ff) - 1:
                output += ", "
        output += "}"
        print(output)

class SET:
    def __init__(self):
        self.a=[]
        self.b=[]

  

        self.sizeA=int(input("enter the size of Set A "))
        self.sizeB = int(input("enter the size of Set B "))
        for i in range(self.sizeA):
            c=int(input("enter the elements of set A "))
            self.a.append(c)
        for i in range(self.sizeB):
            d = int(input("enter the elements of set B "))
            self.b.append(d)
        print(self.a)
        print(self.b)


    def uni(self):
        uni=[]
        for element in self.a:
            if element not in uni:
                uni.append(element)
        for element in self.b:
            if element not in uni:
                uni.append(element)

        display(uni)


    def ins(self):
        ins=[]
        for element in self.a:
            for e in self.b:
                if element==e:
                    ins.append(e)
                    pass

        display(ins)
        

    def diff(self):
        while True:
            print("\nDifference \n"
                  "1.A-B\n"
                  "2.B-A\n"
                  "3.Previous Menu")
            ch=int(input("enter your choice "))
            if ch==1:
                diff=[]
                for element in self.a:
                    if element not in self.b:
                        diff.append(element)
                display(diff)

            elif ch==2:
                diff=[]
                for element in self.b:
                    if element not in self.a:
                        diff.append(element)
                display(diff)

            elif ch==3:
                break
            else:
                print("Choose valid choice ")


    def subset(self):
        sub=[]
        for element in self.a:
            if element  in self.b:
                sub.append(element)
        display(sub)

    

s1=SET()
while True:
    print("\nMenu\n"
          "1.Union\n"
          "2.Intersection\n"
          "3.Difference\n"
          "4.Subset\n"
          "5.Exit")
    ch=int(input("Enter your choice "))
    if ch==1:
        s1.uni()
    elif ch==2:
        s1.ins()
    elif ch==3:
        s1.diff()
    elif ch==4:
        s1.subset()
    elif ch==5:
        break
    else:
        print("Enter valid choice ")