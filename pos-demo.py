class PosSystem:

    def __init__(self, a=0, r=0, receive=0, change=0, temp=0):
        print("\n\n*****WELCOME TO THE SHACK*****\n")

        self.a = a
        self.r = r
        self.receive = receive
        self.change = change
        self.temp = temp

    def foods(self):
        print("*****THE SHACK RESTAURANT MENU*****")

        print("1.Chips-->150", "\n2.Hotdog-->60", "\n3.Soda-->80", "\n4.Cashout", "\n5.Cash out")

        while (1):

            c = int(input("Choose:\n"))

            if (c == 1):
                d = int(input("Enter quantity:\n"))
                self.r = self.r + 150 * d

            elif (c == 2):
                d = int(input("Enter quantity:\n"))
                self.r = self.r + 60 * d

            elif (c == 3):
                d = int(input("Enter quantity:\n"))
                self.r = self.r + 80 * d

            elif (c == 4):
                print("total:", self.r)
                if (self.r > 0):
                    receive = int(input("Input amount you wish to spend:\n"))
                    print("Change:", receive - self.r)
                    print("*****Thank you come again*****")
                    quit()
            elif (c == 5):
                quit()
            else:
                print('Invald option')


def main():
    a = PosSystem()
     
    while(1):

        a.foods()








main()
