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
    """ print numbers from 1-40 that are odd, multiples of 3, and not multiples of 5 """
    for number in range(41):
        if number % 2 != 0: # continue if odd
            if number % 3 == 0: # continue if a multiple of 3
                if number % 5 != 0: # continue if not a multiple of 5
                    print(number)
                


# Task 4.a
def my_for_loop():
    """ determine if each letter in a word is a consonant or vowel """
    
    gimme = input("Give me a little word: ")
    chars = len(gimme)
    if 2 <= chars <= 5 and " " not in gimme: # continue if the correct length
        
        for chars in range(len(gimme)):
            if gimme[chars] == "a" or gimme[chars] == "e" or gimme[chars] == "i" or gimme[chars] == "o" or gimme[chars] == "u":
                print(f"{gimme[chars]} is a vowel")
            else:
                print(f"{gimme[chars]} is a consonant")
            chars = chars - 1

    else: # end if too short, too long, or has a space
        print("bad word")
        return
        
        

# Task 4.b
def my_while_loop():
    """ Add your docstring """
    choice = input("Choose option a, b, or c: ")
    if "a" in choice:
        my_while_loop()
    if "b" in choice:
        print("Goodbye")
        return
    if "c" in choice:
        sys.exit()
    elif choice != "a" or choice != "b" or choice != "c":
        print("try again")
        my_while_loop()

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
