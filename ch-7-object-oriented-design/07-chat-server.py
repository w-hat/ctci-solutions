# Design a chat server.

class ChatServer(object):
  def __init__(self):
    self.participants = set()
    self.messages = []
  
  def join(self, participant):
    self.participants.add(participant)
    for message in self.messages[-8:]:
      participant.send(message)
  
  def leave(self, participant):
    if participant in self.participants:
      self.participants.remove(participant)
      participant.clear_history()
  
  def send_all(self, participant, text):
    message = (participant.name, text)
    self.messages.append(message)
    for p in self.participants:
      p.send(message)

class Participant(object):
  def __init__(self, name):
    self.name = name
    self.history = []
    
  def send(self, message):
    self.history.append(message)

  def clear_history(self):
    self.history = []

import unittest

class Test(unittest.TestCase):
  def test_chat_server(self):
    server = ChatServer()
    albert = Participant("Albert")
    jordi = Participant("Jordi")
    martha = Participant("Martha")
    kat = Participant("Kat")
    self.assertEqual(server.participants, set())
    server.join(albert)
    for i in xrange(12):
      server.send_all(albert, i)
    server.join(jordi)
    server.leave(jordi)
    server.join(martha)
    self.assertEqual(server.participants, {albert, martha})
    self.assertEqual(albert.history, [('Albert', i) for i in xrange(12)])
    self.assertEqual(martha.history, [('Albert', i) for i in xrange(4, 12)])
    self.assertEqual(jordi.history, [])
    server.send_all(martha, "AlphaGo's victory was surprising!")
    server.join(kat)
    server.send_all(kat, "It's too bad Arimaa didn't outlast Go.")
    self.assertEqual(kat.history[-1], albert.history[-1])

if __name__ == "__main__":
  unittest.main()

