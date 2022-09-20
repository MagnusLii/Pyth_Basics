class Animal:

    alive = True                                    # Common attributes.

    def eat(self):
        print("This animal is eating.")

    def sleep(self):
        print("This animal is sleeping.")

class Rabbit(Animal):                               # 'Rabbit' is the child class and 'Animal' is the parent class.
    def run(self):                                  # Unique attributes.
        print("This rabbit is running.")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming.")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying.")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
rabbit.run()
fish.swim()