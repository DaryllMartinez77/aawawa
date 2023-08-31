class person:
    def __init__(self, name):
      self.name = name

    def say_hi(self):
        print("hello, my name is", self.name)

person1 = person ("Rizky")
person1.say_hi()

#str function
class person:
  def __init__(self,name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = person ("Rizky", 16)
print(p1)
