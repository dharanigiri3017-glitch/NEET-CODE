class Vehicle:
    def getType(self):
        return "Vehicle"


class Car(Vehicle):
    def getType(self):
        return "Car"


class Truck(Vehicle):
    def getType(self):
        return "Truck"


class Bike(Vehicle):
    def getType(self):
        return "Bike"


class VehicleFactory:
    def createVehicle(self):
        pass


class CarFactory(VehicleFactory):
    def createVehicle(self):
        return Car()


class TruckFactory(VehicleFactory):
    def createVehicle(self):
        return Truck()


class BikeFactory(VehicleFactory):
    def createVehicle(self):
        return Bike()
