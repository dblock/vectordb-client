import unittest
from vectordb.client import Client

class ClientTest(unittest.TestCase):
  def setUp(self):
    self.client = Client()

  def test_instance(self):
    self.assertIsInstance(self.client, Client)
