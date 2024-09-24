import random
bday_messages = ['Hope you have a very Happy Birthday! 🎈',
"It's your special day – get out there and celebrate! 🎉",
'You were born and the world got better – everybody wins! 🥳',
'Have lots of fun on your special day! 🎂',
'Another year of you going around the sun! 🌞']
random_message = random.choice(bday_messages)
import datetime, bday_messages
today = datetime.date.today()
my_next_birthday = datetime.date(2024, 8, 29)
days_away = my_next_birthday - today
if my_next_birthday == today:
  print(bday_messages.random_message)
else:
  print(f"My next birthday is {days_away} days away!")