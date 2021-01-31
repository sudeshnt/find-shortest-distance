import unittest
from unittest import mock
from routes.routes import Routes
import csv

class TestRoutes(unittest.TestCase):
  def setUp(self):
    self.routes = Routes('routes')

  def test_generate_map(self):
    with open('mock_routes.csv', 'r') as file:
      print('generate_map should generate the correct distance map')
      self.assertEqual(self.routes._generate_map(file), {'A': {'B': 5}, 'B': {'A': 5}})

  @mock.patch('builtins.open')
  def test_init_map_from_file(self, mock_open):
    print('init_route should call file open')
    self.routes._init_map_from_file()
    mock_open.assert_called()
