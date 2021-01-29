import unittest
from unittest import mock
from route_map.route_map import RouteMap
import csv

class TestRouteMap(unittest.TestCase):
  def setUp(self):
    self.route_map = RouteMap('routes')

  def test_generate_map(self):
    with open('mock_routes.csv', 'r') as file:
      print('generate_map should generate the correct distance map')
      self.assertEqual(self.route_map._generate_map(file), {'A': {'B': 5}, 'B': {'A': 5}})

  @mock.patch('builtins.open')
  def test_init_route_map(self, mock_open):
    print('init_route_map should call file open')
    self.route_map._init_route_map()
    mock_open.assert_called()
