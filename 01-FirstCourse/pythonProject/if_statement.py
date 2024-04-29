is_hot = True
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("War warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your life")


# ----exercise---- #

price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = price * 0.1
    print("It's a good credit point")
    # print("You are going to put down $" + str(down_payment))
    print(f"Down payment is ${down_payment:.2f}")
else:
    down_payment = price * 0.20
    # print("Your down payment is $" + str(down_payment))
    print(f"Down payment is ${down_payment:.2f}")

# ---- logic ---- #
# or, and, not

has_high_income = False
has_criminal_record = False
if not has_criminal_record or has_good_credit: # attention: `not` before statement
    print("Eligible for loan")
else:
    print("Not eligible for loan")

