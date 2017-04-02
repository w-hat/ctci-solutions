# How can the philosophers successfully eat with their chopsticks?

import time
import threading

class Chopstick(object):
  def __init__(self, priority):
    self.priority = priority
    self.lock = threading.Lock()
  
  def pick_up(self):
    self.lock.acquire()
  
  def set_down(self):
    self.lock.release()

class Philosopher(threading.Thread):
  def __init__(self, table, number, left_chopstick, right_chopstick):
    super(Philosopher, self).__init__()
    self.table = table
    self.number = number
    self.left_chopstick = left_chopstick
    self.right_chopstick = right_chopstick
  
  def run(self):
    #for x in xrange(5):
    #  print("I'm philosopher {}".format(self.number))
    if self.left_chopstick.priority < self.right_chopstick.priority:
      first_chopstick  = self.left_chopstick
      second_chopstick = self.right_chopstick
    else:
      first_chopstick  = self.right_chopstick
      second_chopstick = self.left_chopstick
    first_chopstick.pick_up()
    time.sleep(0.1)
    second_chopstick.pick_up()
    self.eat_food()
    first_chopstick.set_down()
    second_chopstick.set_down()
  
  def eat_food(self):
    self.table.finish_eating(self)

class Table(object):
  def __init__(self):
    self.lock = threading.Lock()
    self.count = 0
  
  def finish_eating(self, philosopher):
    self.lock.acquire()
    self.count += 1
    #print("Philosopher {} has eaten.".format(philosopher.number))
    #print("Count: {}".format(self.count))
    self.lock.release()
  
  def get_count(self):
    self.lock.acquire()
    count = self.count
    self.lock.release()
    return count

import unittest

class Test(unittest.TestCase):
  def test_dining_philosophers(self):
    n = 10
    t = Table()
    chops = [Chopstick(i) for i in xrange(n)]
    philosophers = [Philosopher(t,i,chops[i],chops[(i+1)%n]) for i in xrange(n)]
    for philosopher in philosophers:
      philosopher.start()
    time.sleep(0.5)
    self.assertEqual(t.get_count(), n)

if __name__ == "__main__":
  unittest.main()

