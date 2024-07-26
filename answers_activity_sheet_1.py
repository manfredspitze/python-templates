# starter program lesson 1

name = "Billy"
print("We want to know if you like progammming!")
print()
print("Do you like programming " + name + "?")
answer = input()
print("Great! You said " + answer + "!")
print("Let's learn some Python today")


##1.	Change the program so that it uses your name instead of Billy.

name = "Amjad"
print("We want to know if you like progammming!")
print()
print("Do you like programming " + name + "?")
answer = input()
print("Great! You said " + answer + "!")
print("Let's learn some Python today")
##
##2.	Change the program so that it lets you type in your answer
##      on the same line as the question.

name = "Billy"
print("We want to know if you like progammming!")
print()
answer = input("Do you like programming " + name + "? ")
print("Great! You said " + answer + "!")
print("Let's learn some Python today")
##
##3.	Change the program so that it asks the user what their
##      name is at the beginning of the program

name = input("What is your name? ")
print("We want to know if you like progammming!")
print()
answer = input("Do you like programming " + name + "? ")
print("Great! You said " + answer + "!")
print("Let's learn some Python today")
print()
print()
# leave some space
##4.	Ask the user three questions, and each time give a suitable response:
##
##•	What their name is
##•	What they had for breakfast
##•	What their favourite colour is
##Then ask another person to test your program
##
print()
print()
# leave some space
name = input("What is your name? ")
print("Hello " + name)
print()
answer = input("What did you have for breakfast? " + name + "? ")
print("Great! "+ answer + " sounds delicious. ")
answer = input("What is your favourite colour " + name + "? ")
print("My favourite colour is "+ answer + " too!")
##Extension
##Ask the user how old they are and then tell them how old they will be on their next birthday. HINT: You will need to use int(input(“How old are you?”)) as int() changes the answer from the keyboard into a number.
##
print()
print()
# leave some space
name = input("What is your name? ")

age = int(input("How old are you " + name + "? "))
newage = age + 1
print("Thank you - that means you will be " + str(newage) + " next birthday")
print()


## Bug Finder

##name = "Billy"
##print("We want to know if you like progammming!)
##print()
##print("Do you like programming " + Name + "?")
##answer = input(
##Print("Great! You said " + anwer + "!")
##print("Let's learn some Python today")

