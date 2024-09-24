Gryffindor_point = 0
Ravenclaw_point = 0
Hufflepuff_point = 0
Slytherin_point = 0
# Question 1
print("Q1 Do you like Dawn or Dusk")
print("   1) Dawn")
print("   2) Dusk")
answer = int(input("Enter your answer (1-2): "))
if answer == 1:
  Gryffindor_point += 1
  Ravenclaw_point += 1
elif answer == 2:
  Hufflepuff_point += 1 
  Ravenclaw_point += 1
else:
  print("Wrong input")
# Question 2
print("Q2) When I'm dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
answer = int(input("Enter your answer (1-4): "))
if answer == 1:
  Hufflepuff_point += 2
elif answer == 2:
  Slytherin_point += 2
elif answer == 3:
  Ravenclaw_point += 2
elif answer == 4:
  Gryffindor_point += 2
else:
  print("Wrong input.")
# Question 3
print("Q3) Which kind of instrument most pleases your ear? ")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
answer = int(input("Enter your answer (1-4): "))
if answer == 1:
  Slytherin_point += 4
elif answer == 2:
  Hufflepuff_point += 4
elif answer == 3:
  Gryffindor_point += 4
else:
  print("Wrong input")
# max_points
points = {
    "Gryffindor": Gryffindor_point,
    "Ravenclaw": Ravenclaw_point,
    "Hufflepuff": Hufflepuff_point,
    "Slytherin": Slytherin_point,
}
max_points = max(points.values())
top_houses = [house for house, point in points.items() if points == max_points]
print("Results:")
for house, point in points.items():
  print(f"{house}: {point} points")
print("House(s) with the most points:", ", ".join(top_houses))