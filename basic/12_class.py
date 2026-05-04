# Defining a simple class
class MyClass:
  x = 5

# Creating an object (Instance)
p1 = MyClass()
print(p1.x)


class Person:
    pass

p1 = Person()
p1.name = "John"
p1.age = 36
print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age=10):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Car:
  def __init__(mysillyobject, brand, model):
    mysillyobject.brand = brand
    mysillyobject.model = model

  def drive(abc):
    print("The " + abc.model + " is driving!")

c1 = Car("Toyota", "Corolla")
c1.drive()


class Dog:
    species = "Canis familiaris" # Class Property

    def __init__(self, name, age):
        self.name = name         # Instance Property
        self.age = age           # Instance Property

buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print(buddy.species) # "Canis familiaris"
print(miles.species) # "Canis familiaris"

# TODO: check
buddy.species = "random"
print(buddy.species)
print(miles.species)


import random
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

  def get_random_song(self):
    if len(self.songs) == 0:
      return ""

    idx = random.randint(0, len(self.songs)-1)
    print(idx)
    return self.songs[idx]

my_playlist = Playlist("Favorites")
print(my_playlist.get_random_song())
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()
print(my_playlist.get_random_song())



