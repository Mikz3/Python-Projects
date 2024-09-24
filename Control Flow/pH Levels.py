pH = int(input("Enter a pH value (0-14):"))
if pH > 7:
  print("Basic")
elif pH < 7:
  print("Acidic")
else:
  print("Neutral")