'''
Code Name : keywords.py
Purpose   : Check for the list of keywords in Python
Initial Version : 11-November-2017
Created By      : Avantika Joshi
'''

import keyword
def check_keyword(word):
    if keyword.iskeyword(word):
        print (word + " is a keyword in Python library")
    else:
        print (word + " is not a keyword")

def main():
    choice = 1
    while choice == 1:
        word = input("Enter the word you want to check ")
        check_keyword(word)
        choice = input('''Press 1 if you want to check for any other word.
        Press 2 if you want to see all the keywords. Else, press anything''')
        try:
            if int(choice) == 2:
                print ("The list of all the keywords is \n")
                print (keyword.kwlist)
            if int(choice) != 1:
                print ("Thank you. We hope the program helped you \n")
        except ValueError:
            print ("Please enter a numeric value. Thank you. We hope the code helped you")
            continue
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print ("Thank you. We hope the program helped you \n")
    except EOFError:
        print("Thank you. We hope the program helped you \n")
