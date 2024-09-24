guess = 0
tries = 0
while guess != 6 and tries < 5:
 guess = int(input("Guess the number:  "))
 if guess != 6:
  print("Wrong guess. You have {4 - tries} tries left.")
  tries += 1