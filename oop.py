# class, object, inheritance, encapsulation, abstraction,  polymorphism

class Location():
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def __str__(self) -> str:
        return f"Latitude: {str(self.lat)}°, Longitude: {str(self.lng)}°"


dhaka = Location(23.8103, 90.4125)
# print(dhaka)

mexico = Location(23.6345, 102.5528)
# print(mexico)

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


# Four Principles:

# Inheritance: sub class, child class

# Encapsulation: public, private, protected

# Abstraction

# Polymorphism


class CoffeeMaker():
    def brew(self):
        return 'Brewing the coffee.'


c = CoffeeMaker()
print(c.brew())


class SpecialCoffeeMaker(CoffeeMaker):
    def brewLatte(self):
        return 'Brewing a latte'


sc = SpecialCoffeeMaker()
print(sc.brew())
print(sc.brewLatte())
