import unittest
import math
from unittest import mock
from shortest_route import ShortestRoute
from utils.utils import Utils
from route_map.route_map import RouteMap

class TestShortestRoute(unittest.TestCase):
  
  @mock.patch.object(Utils, 'get_file_name', return_value='routes')
  def setUp(self, mock_get_file_name):
    self.shortest_route = ShortestRoute()
    self.shortest_route.init_route_map()

  @mock.patch.object(Utils, 'get_file_name', return_value='routes')
  def test_get_file_name(self, mock_get_file_name):
    print('_get_file should call get_file_name in Utils')
    file_name = self.shortest_route._get_file_name()
    mock_get_file_name.assert_called()
    self.assertEqual(file_name, 'routes')

  @mock.patch.object(ShortestRoute, '_get_file_name', return_value='routes')
  def test_init_route_map(self, mock_get_file_name):
    print('init_route_map should call _get_file_name')
    self.shortest_route.init_route_map()
    mock_get_file_name.assert_called()
    self.assertIsInstance(self.shortest_route.route_map, RouteMap)
    self.assertEqual(self.shortest_route.route_map.file_name, 'routes')

  @mock.patch.object(RouteMap, 'get_input_station', return_value='on')
  def test_get_src_dest_input(self, mock_get_input_station):
    print('get_src_dest_input should ask for user input and initialize src & dest')
    self.shortest_route.get_src_dest_input()
    self.assertEqual(self.shortest_route.src, 'on')
    self.assertEqual(self.shortest_route.src, 'on')

  def test_initialize_helpers(self):
    print('_initialize_helpers should return the correct helpers')
    self.shortest_route.src = 'A'
    self.shortest_route.route_map.map = { 'A': { 'B': 5 }, 'B': { 'A': 5 }}
    dist, adj, queue = self.shortest_route._initialize_helpers()
    self.assertEqual(dist, {'A': 0, 'B': math.inf})
    self.assertEqual(adj, {'A': None, 'B': None})
    self.assertEqual(queue, ['A', 'B'])

  def test_calculate_shortest_distance_and_stops(self):
    print('_calculate_shortest_distance_and_stops should return stops and distance map')
    self.shortest_route.src = 'A'
    self.shortest_route.dest = 'B'
    self.shortest_route.route_map.map = { 'A': { 'B': 5 }, 'B': { 'A': 5 }}
    stops, distance = self.shortest_route._calculate_shortest_distance_and_stops()
    self.assertEqual(stops, ['A', 'B'])
    self.assertEqual(distance, {'A': 0, 'B': 5})

  @mock.patch.object(ShortestRoute, '_calculate_shortest_distance_and_stops', return_value=[['A', 'B'], {'A': 0, 'B': 5}])
  @mock.patch('builtins.print')
  def test_get_shortest_route(self, mock_print, mock_calculate_shortest_distance_and_stops):
    self.shortest_route.src = 'A'
    self.shortest_route.get_shortest_route()
    mock_print.assert_called_with('A -> B')
