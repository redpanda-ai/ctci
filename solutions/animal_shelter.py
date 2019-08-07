"""
Title:
    Animal Shelter
Question:
    An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.  People must adopt either the "oldest" (based on arrival time) of all animals in the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).  They cannot select which specific animal they would like.  Create the data structures to maintain this system and implement options such as enqueue, dequeAny, dequeueDog, and dequeueCat.  You may use the built-in LinkedList data structure.
"""

from collections import deque


class Shelter:
    def __init__(self):
        self.dogs = deque([])
        self.cats = deque([])
        self.id = 0

    def __repr__(self):
        return f"dogs: {self.dogs}\ncats: {self.cats}"

    def enqueue(self, animal):
        if animal == "cat":
            self.cats.append(Cat(self.id))
        else:
            self.dogs.append(Dog(self.id))
        self.id += 1

    def dequeueDog(self):
        return self.dogs.popleft()

    def dequeueCat(self):
        return self.cats.popleft()

    def dequeueAny(self):
        c, d = None, None
        if self.dogs:
            d = self.dogs[0]
        if self.cats:
            c = self.cats[0]

        if not c and not d:
            raise Exception("No dogs or cats, sorry!")
        if c and not d:
            return self.cats.popleft()
        elif d and not c:
            return self.dogs.popleft()
        elif d.id_num < c.id_num:
            return self.dogs.popleft()
        else:
            return self.cats.popleft()


class Dog:
    def __init__(self, id_num):
        self.id_num = id_num

    def __repr__(self):
        return f"dog({self.id_num})"


class Cat:
    def __init__(self, id_num):
        self.id_num = id_num

    def __repr__(self):
        return f"cat({self.id_num})"


s = Shelter()
print(s)
s.enqueue("cat")
s.enqueue("dog")
s.enqueue("cat")
print(s)
print(s.dequeueCat())
# print(s.dequeueDog())
print(s)
print(s.dequeueAny())
print(s.dequeueAny())
print(s.dequeueAny())