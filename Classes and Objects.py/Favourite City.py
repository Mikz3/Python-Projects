class City:
  def __init__(self, name, country, population, landmarks,):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
london = City("London", "England", 898200000, ["Big Ben", "london bridge"])
print(vars(london))