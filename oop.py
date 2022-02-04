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
            print("No available seats.")
            return
        self.passengers.append(name)

    def available_seats(self):
        return self.capacity - len(self.passengers)


train = Train(3)
train.add_passenger('ebnsina')
train.add_passenger('adam')
train.add_passenger('Jr. adam')
train.add_passenger('Jr. adam')
print(train)
