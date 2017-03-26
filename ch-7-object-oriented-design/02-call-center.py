# Design a call center.

class CallCenter():
  def __init__(self, respondents, managers, director):
    self.respondents = respondents
    self.managers = managers
    self.director = director
    self.respondent_queue = []
    self.call_queue = []
    for respondent in respondents:
      respondent.callcenter = self
      if not respondent.call:
        self.respondent_queue.append(respondent)
  
  def route_respondent(self, respondent):
    if len(self.call_queue):
      respondent.take_call(self.call_queue.pop(0))
    else:
      self.respondent_queue.append(respondent)
  
  def route_call(self, call):
    if len(self.respondent_queue):
      self.respondent_queue.pop(0).take_call(call)
    else:
      self.call_queue.append(call)

class Call():
  def __init__(self, issue):
    self.issue = issue
    self.employee = None
    
  def resolve(self, handled):
    if handled:
      self.issue = None
    self.employee.finish_call(handled)
    
  def apologize_and_hangup(self):
    # "Try calling our competitor."
    self.employee = None

class Employee(object):
  def __init__(self, name, manager):
    self.name, self.manager = name, manager
    self.call = None
  
  def take_call(self, call):
    if self.call:
      self.escalate(call)
    else:
      self.call = call
      self.call.employee = self
  
  def escalate(self, call):
    if self.manager:
      self.manager.take_call(call)
    else:
      call.apologize_and_hangup()
  
  def finish_call(self, handled=True):
    if not handled:
      if self.manager:
        self.manager.take_call(self.call)
      else:
        call.apologize_and_hangup()
    self.call = None

class Respondent(Employee):
  def finish_call(self, handled=True):
    super(Respondent, self).finish_call(handled)
    self.callcenter.route_respondent(self)
  
class Manager(Employee):
  pass

class Director(Employee):
  def __init__(self, name):
    super(Director, self).__init__(name, None)

import unittest

class Test(unittest.TestCase):
  def test_call_center(self):
    lashaun = Director("Lashaun")
    juan = Manager("Juan", lashaun)
    sally = Manager("Sally", lashaun)
    boris = Respondent("Boris", juan)
    sam = Respondent("Sam", juan)
    jordan = Respondent("Jordan", sally)
    casey = Respondent("Casey", sally)
    center = CallCenter([boris, sam, jordan, casey], [juan, lashaun], sally)
    call1 = Call("The toilet")
    call2 = Call("The webpage")
    call3 = Call("The email")
    call4 = Call("The lizard")
    call5 = Call("The cloudy weather")
    call6 = Call("The noise")
    self.assertEqual(len(center.respondent_queue), 4)
    center.route_call(call1)
    center.route_call(call2)
    self.assertEqual(len(center.respondent_queue), 2)
    center.route_call(call3)
    center.route_call(call4)
    center.route_call(call5)
    center.route_call(call6)
    self.assertEqual(center.call_queue, [call5, call6])
    call1.resolve(True)
    self.assertEqual(call1.issue, None)
    self.assertEqual(center.call_queue, [call6])
    self.assertEqual(sally.call, None)
    self.assertEqual(lashaun.call, None)
    call4.resolve(False)
    self.assertEqual(sally.call, call4)
    call4.resolve(False)
    self.assertEqual(sally.call, None)
    self.assertEqual(lashaun.call, call4)
    call4.resolve(True)
    self.assertEqual(lashaun.call, None)
    call6.resolve(True)
    self.assertEqual(center.respondent_queue, [casey])

if __name__ == "__main__":
  unittest.main()

