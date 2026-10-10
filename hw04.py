# ------------------------------------------------------
#        Name: Ash Rulifson
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "cupcake"

# Task 1
def check_text():
    """ ask for a sentence, determine if it has cupcake or dog in it """
    sent = input("Give me a sentence: ")
    if secret_word in sent:
        print("You used the secret word!")    
    elif "dog" not in sent:
        print("Try again.")
        check_text()
    if "dog" in sent:
        print('''You used the word \"dog\" or the word \"Dog\"!''')



# Task 2
def check_greater():
    """ compare magnitude of two integers """
    num1 = int(input("Give me a number: "))
    num2 = int(input("Give me another number: "))
    if num1 < num2:
        print("Second is Greater.")
    elif num1 > num2:
        print("First is Greater.")
    else: # nums are equal
        print("Try again.")
        check_greater()



# Task 3
def get_special_numbers():
    """ Add your docstring """
    for number in range(41):
        if number % 2 != 0: # continue if odd
            if number % 3 == 0: # continue if a multiple of 3
                if number % 5 != 0: # continue if not a multiple of 5
                    print(number)
                


# Task 4.a
def my_for_loop():
    """ Add your docstring """
    pass

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    pass

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
