# Importing stuff

import pandas
import datetime as dt
import random
import smtplib

# Creating date vars

now = dt.datetime.now()
month = now.month
day = now.day

# Other vars

my_email = "youremail"
app_password = "yourpassword"
birthday_cards = []
PLACEHOLDER = "[NAME]"

# Creating csv file

# name_dict = {
#    "name": ["Sandor", "Jeanette", "Tomi"],
#    "email": ["arthurmalone13@yahoo.com", "arthurmalone13@yahoo.com", "arthurmalone13@yahoo.com"],
#    "year": [1963, 1994, 1991],
#    "month": [9, 9, 5],
#    "day": [16, 9, 25]
# }

# data = pandas.DataFrame(name_dict)
# print(data)
# data.to_csv("birthday.csv")

# Reading txt files.

with open("letter_1.txt") as letter_one:
    l_one = letter_one.read()
    birthday_cards.append(l_one)
    # print(l_one)

with open("letter_2.txt") as letter_two:
    l_two = letter_two.read()
    birthday_cards.append(l_two)
    # print(l_two)

with open("letter_1.txt") as letter_three:
    l_three = letter_three.read()
    birthday_cards.append(l_three)
    # print(l_three)
# print(birthday_cards)

# Reading csv file

with open("birthday.csv") as data_file:
    random_card = random.choice(birthday_cards)
    # print(random_card)
    data = pandas.read_csv(data_file)
    for index, row in data.iterrows():
        if row['month'] == month and row['day'] == day:
            # print(f"{row['name']} has a birthday today.")
            new_letter = random_card.replace(PLACEHOLDER, row['name'])
            # print(new_letter)
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=app_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=f"{row['email']}",
                    msg=f"Subject:Happy Birthday {row['name']}\n\n{new_letter}"
                )
