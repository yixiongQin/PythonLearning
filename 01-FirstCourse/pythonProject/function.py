def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("John", "X")
greet_user(last_name="Doe", first_name="Jane")


# calc_cost(total=50, shipping=5, discount=0.2)
print("End")


def square(number):
    return number * number

print(square(10))


def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)" : "😊",
        ":(" : "😭"
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input("Enter your message: ")
print(emoji_converter(message))

