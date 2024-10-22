class AnyPower: 
    def calculate(initial_number, power):
        new_number = 1
        if initial_number == 0:
            new_number = 0
        elif power == 0:
            new_number = 1
        else:
            for i in range(1, power+1):
                new_number = new_number * initial_number
        return new_number
def main():
    while True:
        try:
            
            answer = int(input('\n\n\n\nType 1 to start \nType 2 to exit\nType 3 for credits\n'))
            if answer == 1:
                initial_number = int(input("Enter the initial number: \n"))
                power = int(input("Enter the power: \n"))
                print("\n\n\nYour answer is: \n\n\n" )
                print(AnyPower.calculate(initial_number, power))
                input("press enter to continue")
            elif answer == 2:
                break
            elif answer == 3:
                print("Credits: Made by You!")
        except ValueError:
            print("Write a number")
        
main()
print("Thank you")
    