# Design a parking lot.

class ParkingLot(object):
  def __init__(self):
    self.cars = {}
  
  def park_car(self, car):
    self.cars[car] = True
  
  def unpark_car(self, car):
    del self.cars[car]

class Car(object): pass

import unittest

class Test(unittest.TestCase):
  def test_parking_lot(self):
    lot = ParkingLot()
    car1 = Car()
    car2 = Car()
    lot.park_car(car1)
    lot.park_car(car2)
    lot.unpark_car(car1)
    self.assertEqual(len(lot.cars), 1)

if __name__ == "__main__":
  unittest.main()

