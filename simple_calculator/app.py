""" 
    Simple Calculator using Python

Author : Sahil Uddin Ishmam
Department : CSE
University : Metropolitan University

"""



# function definition

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    try :
        return a/b
    except Exception as error:
        return error

def modulus(a,b):
    try :
        return a % b 
    except Exception as error:
        return error


# Main function
if __name__ == '__main__':

    while(True):

        print("---------------------------------------")

        # Implementation of user input handling

        print("""\n     Select operation :\n
                 1. Addition
                 2. Subtraction
                 3. Multiplication
                 4. Division
                 5. Modulus
                 6. Quit
              """)
        
        operation = input("Enter choice(1/2/3/4/5): ")
        # some exceptional case has added
        if operation == "6":
            print("Programme Terminated!!")
            break
        elif operation not in ['1','2','3','4','5']:
            print("Please Enter a valid Operation type.")
            continue

        # Error handling for number
        a = input("\nEnter first number: ")
        try : 
            a = float(a)
        except Exception as error:
            print(error)
            continue


        # Error handling for number
        b = input("\nEnter second number: ")
        try : 
            b = float(b)
        except Exception as error:
            print(error)
            continue

        
        # conditional Logic for user to select operation

        if operation == "1": 
            result = addition(a,b)
            print(f"\n{a} + {b} = {result}\n")
            # Output formatting

        elif operation == "2":
            result = subtraction(a,b)
            print(f"\n{a} - {b} = {result}\n")
            # Output formatting

        elif operation == "3":
            result = multiplication(a,b)
            print(f"\n{a} * {b} = {result}\n")
            # Output formatting

        elif operation == "4":
            result = division(a,b)
            if str(result).isdigit():
                print(f"\n{a} / {b} = {result}\n")
                # Output formatting
            else:
                print(result)
                
        elif operation == "5":
            result = modulus(a,b)
            if str(result).isdigit():
                print(f"\n{a} % {b} = {result}\n")
                # Output formatting
            else :
                print(result)
        

        print("---------------------------------------")
