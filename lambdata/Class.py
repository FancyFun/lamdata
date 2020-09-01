class Dog:
  def __init__(self, name, age, mood):
    self.age = age
    self.mood = mood
    self.name = name

  def get_name(self):
    return self.name
  
  def age(self):
    return self.age

  def mood(self):
    return self.mood



  def bark(self):
    print("Bark Bark Bark")
  
  def is_happy(self):
    print("wags tail") 
  
  def is_tired(self):
    print("sleeping Zzz")
