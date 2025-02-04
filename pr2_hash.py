class Hashing:
    def __init__(self):
        self.size=int(input("Enter no of phonebook users: "))
        self.table=list(None for i in range(self.size))
        self.counter=0
        self.comparison=0
        

    def isfull(self):
        if self.counter==self.size:
            return True
        return False
    

    def insert(self):
        n=0
        while(n<self.size):
            element=int(input("Enter element: "))
            position=element%self.size
            if self.isfull():
                print("Table is full ")

            else:
                if self.table[position] is None:
                    self.table[position]=element
                    self.counter+=1
                    self.comparison+=1

                else:
                    print("collision occured, finding new position")
                    while self.table[position] is not None:
                        position+=1
                        if position>=self.size:
                            position=0

                    self.table[position]=element
                    self.counter+=1
                    self.comparison+=1

            print(self.table[position],"appended")
            n+=1


    def display(self):
        print("Hash Table")
        for i in range(self.size):
            print(f"{i} {self.table[i]}")

    def search(self):
            element=int(input("Enter element to search: "))
            position=element%self.size

            if self.table[position]==element:
                print(f"Found at position {position}")

            else:
                while self.table[position]!=element:
                        position+=1
                        if position>=self.size:
                            position=0

                if self.table[position]==element:
                    print(f"Found at position {position}")


h1=Hashing()
choice=-1
while(choice!=0):
    print("Enter 1 to insert")
    print("Enter 2 to display hash table")
    print("Enter 3 to search an element")
    print("0:  Exit")
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        h1.insert()

    elif choice==2:
        h1.display()

    elif choice==3:
        h1.search()

    elif choice==0:
        break
    else:
        print("Enter correct choice")










        
