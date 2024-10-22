class NumberFactorization:

    def get_factors(self, initial_number):
        output = []
        for i in range(1, initial_number+1):
            
            if initial_number % i == 0:
                output.append(i)
        return output
    
def main(): 
    while True:
        print("Number Factorization")
        print("Type 1 to start\nType 2 to exit\nType 3 for credits\n")
        program = input()  # Take input from the user
        if program == "1":
            number = int(input("Enter a number: "))
            print(NumberFactorization().get_factors(number))
        elif program == "2":
            exit()
            break
        elif program == "3":
            print("Credits: Made by You!")
            
main()