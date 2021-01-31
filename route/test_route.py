import unittest
from unittest import mock
from route.route import Route
import csv

class TestRoute(unittest.TestCase):
  def setUp(self):
    self.route = Route('routes')

  def test_generate_route(self):
    with open('mock_routes.csv', 'r') as file:
      print('generate_map should generate the correct distance map')
      self.assertEqual(self.route._generate_route(file), {'A': {'B': 5}, 'B': {'A': 5}})

  @mock.patch('builtins.open')
  def test_init_route(self, mock_open):
    print('init_route should call file open')
    self.route._init_route()
    mock_open.assert_called()
