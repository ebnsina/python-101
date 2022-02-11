# class, object, inheritance, encapsulation, abstraction,  polymorphism

from abc import ABC


class Location():
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def __str__(self) -> str:
        return f"Latitude: {str(self.lat)}°, Longitude: {str(self.lng)}°"


dhaka = Location(23.8103, 90.4125)
print(dhaka)

mexico = Location(23.6345, 102.5528)
print(mexico)

# 23.8103° N, 90.4125° E (dhaka)
# 23.6345° N, 102.5528° W (mexico)


class Train():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def __str__(self):
        return f"Train has capacity of {self.capacity} and available seats {self.available_seats()}."

    def add_passenger(self, name):
        if not self.available_seats():
            print("No seats available.")
            return
        self.passengers.append(name)

    def available_seats(self):
        return self.capacity - len(self.passengers)


train = Train(3)
train.add_passenger('ebnsina')
train.add_passenger('adam')
train.add_passenger('Jr. adam')
train.add_passenger('Jr. adam 2')
print(train)


class Person():
    # property
    species = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name is {self.name} & age is {self.age}."

    # methods
    def walk(self):
        return f"{self.name} can walk."


# creating object from class
hamid = Person('Hamid', 60)
murad = Person('Murad', 32)


# Inheritance: subclass
class Baby(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


baby1 = Baby('baby1', 1)

print(baby1.walk())


# Encapsulation: public, private (__), protected (_)
class Product():
    def __init__(self):
        self.__sellprice = 999

    def sell(self):
        return f"Selling price: {self.__sellprice}"

    def set_sell_price(self, price):
        self.__sellprice = price


p = Product()
print(p.sell())

p.__sellprice = 2000
print(p.sell())

p.set_sell_price(2000)
print(p.sell())


# Polymorphism: means many forms. Having same function name but different signatures being used for different types.
# len being used for both string, list

# 1
class Bangladesh():
    def capital(self):
        return 'Bangladesh capital: DHAKA.'

    def language(self):
        return 'Native language: Bengali.'


class Turkey():
    def capital(self):
        return 'Turkey capital: ISTANBUL.'

    def language(self):
        return 'Native language: Turkish.'


bangladesh = Bangladesh()
turkey = Turkey()


for country in (bangladesh, turkey):
    print(country.capital())
    print(country.language())


# 2
class Magpie():
    def fly(self):
        return 'Magpie can fly.'

    def swim(self):
        return 'Magpie can not swim.'


class Peguin():
    def fly(self):
        return 'Peguin can not fly.'

    def swim(self):
        return 'Peguin can swim.'


m = Magpie()
p = Peguin()


def can_swim(obj):
    return obj.swim()


print(can_swim(m))
print(can_swim(p))


# Four Principles: Inheritance, Encapsulation, Abstraction, Polymorphism

# Inheritance: sub class, child class

# Encapsulation: public, private, protected

# Abstraction: abstract class

# Polymorphism: multiple forms


# Define a class
class Person():
    # class attribute
    job = 'developer'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        return 'hello'

    # class method
    @classmethod
    def anonymous(cls):
        return Person('Anon', 25)

    # static method
    @staticmethod
    def create_person():
        return 'Person created!'


p = Person('Jane', 23)
print(p.job)

# class methods vs. instance methods vs. static methods
# class.method(), object.method(),

# Encapsulation:  private _, protected __


class Counter():
    def __init__(self):
        self._counter = 0

    def increment(self):
        self._counter += 1

    def value(self):
        return self._counter

    def reset(self):
        self._counter = 0


c = Counter()

print(c.value())
print(c.increment())
c.counter = -11

print(c.value())


# __eq__
class Person2:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age


john = Person2('John', 'Doe', 25)
jane = Person2('Jane', 'Doe', 25)
print(john == jane)  # True

# getter, setter


class Person3:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age

    def get_age(self):
        return self._age

    #
    age = property(fget=get_age, fset=set_age)


p3 = Person3('Sarah', 25)
# p3.age = -1
# print(p3.age)


class Person4:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    @property
    def age(self):
        return self.age

    @age.setter
    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        self._age = age

    def get_age(self):
        return self.age


# p4 = Person4('Sarah', 24)
# p4.age = 90
# print(p4.age)



# Property decorator

class Car():
    def __init__(self, name, price, year):
        self.name = name
        self._price = price
        self.year = year


    @property
    def price(self):
        return self._price

    
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            print("Price cannot be zero.")
        else:
            self._price = new_price



toyota = Car('Toyota', 30000, 2000)

print(toyota.price)
toyota.price = -1000
toyota.price = 1000
print(toyota.price)


class Customer2():
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            print("Age cannot be lower than zero.")
        else:
            self._age = new_age


customer = Customer2('Hello', 100)
print(f"Customer Age: {customer.age}")
customer.age = -1
print(f"Customer Age: {customer.age}")
customer.age = 90
print(f"Customer Age: {customer.age}")
