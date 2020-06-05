# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle is base class
class Vehicle:
  pass

# GroundVehicle inherits Vehicle
class GroundVehicle(Vehicle):
  pass

# Car inherits GroundVehicle
class Car(GroundVehicle):
  pass

# Motorcycle inherits GroundVehicle
class Motorcycle(GroundVehicle):
  pass

# FlightVehicle inherits Vehicle
class FlightVehicle(Vehicle):
  pass

# Airplane inherits FlightVehicle
class Airplane(FlightVehicle):
  pass

# Starship inherits FlightVehicle
class Starship(FlightVehicle):
  pass