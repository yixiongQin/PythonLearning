i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")

# output
# *
# **
# ***
# ****
# *****
# Done

#  ---- guess game --- #
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break # terminate the loop
else:
    print("Sorry, You lost!")

#---- exercise ----#

is_quite_game = False
is_started = False
is_stopped = False

while not is_quite_game:
    action = input("> ").lower()
    if action == "start":
        if is_started:
            print("You have already started the game!")
        else:
            print("Car started ... Ready to go!")
            is_started = True
            is_stopped = False
        continue
    elif action == "stop":
        if is_stopped:
            print("You have already stopped the game!")
        else:
            print("Car stopped...")
            is_started = False
            is_stopped = True
        continue
    elif action == "quit":
        is_quite_game = True
        break
    elif action == "help":
        print("Available actions:")
        print("""
> start - Guess a number
> stop - Guess a number
> quit - Quit
        """)
    else:
        print("Sorry, I don't understand that action.")
        continue

print("Thanks for playing!")


