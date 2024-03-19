import random
import pandas
from hadis import title, quotes
from smtplib import *

MY_MAIL = "abc@gmail.com"
MY_PASSWORD = "ljohisadsfs"

data = pandas.read_csv("news.csv")
friend_list = {row["name"]: row["email"] for (index, row) in data.iterrows()}
quote = str(quotes[random.randint(1, 50)])[1:-1]
hadis_number = 0
for name in friend_list:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_MAIL, MY_PASSWORD)
        with open("count.txt", "r") as count:
            new_data = count.read()
        hadis_content = str(title[int(new_data)])[1:-1]
        connection.sendmail(
            from_addr=MY_MAIL,
           to_addrs = f"{friend_list[name]}",
            msg=f"Subject: Assalamualaikum {name}\n{quote},\n\n{hadis_content}"
        )
hadis_number += 1
with open("count.txt", "w") as count:
   count.write(f"{hadis_number}")





