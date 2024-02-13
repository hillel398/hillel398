def display_menu():
    print("1. Algorithm")
    print("2. Variable")
    print("3. Variable Type (data type)")
    print("4. Array")
    print("5. If statement")
    print("6. Loop")
    print("7. Function")
    print("8. Class")
    print("9. Object")
    print("10. Method")
    print("11. Programming Language")
    print("12. Control Structure")
    print("")

def main():
    while True:
        display_menu()
        choice = input("Enter the number of the term to see its definition (or 'exit' to quit): ")

        if choice == 'exit':
            print("Goodbye!")
            break

        elif choice == '1':
            print("Algorithm - is a set of instructions that are followed to solve a problem.\n")

        elif choice == '2':
            print("Variable - container that holds a single number, word, or other information that you can use throughout a program.\n")

        elif choice == '3':
            print("Variable Type (data type) - Basic variable types include: string (words and phrases), char (short for 'character;' a single letter or symbol you can type), int (short for 'integer;' for whole numbers), double or float (for decimal numbers), and bool (short for 'boolean;' for true or false values.\n")

        elif choice == '4':
            print("Array - containers that hold variables of the same data type.\n")

        elif choice == '5':
            print("If statement - runs a block of code based on whether or not a condition is true.\n")

        elif choice == '6':
            print("Loop - check a condition and then run a code block. The loop will continue to check and run until a specified condition is reached.\n")

        elif choice == '7':
            print("Function - block of code that can be referenced by name to run the code it contains.\n")

        elif choice == '8':
            print("Class - template definition of the methods and variables in a particular kind of object.\n")

        elif choice == '9':
            print("Object - data type that has unique attributes and behavior.\n")

        elif choice == '10':
            print("Method - programmed procedure that is defined as part of a class and is available to any object instantiated from that class.\n")

        elif choice == '11':
            print("Programming Language - system of notation for writing computer programs. Python is an example.\n")

        elif choice == '12':
            print("Control Structure - basic blocks for decision making processes in computing.\n")

        else:
            print("<Error> Error! Not a valid choice.\n")

if __name__ == "__main__":
    main()
