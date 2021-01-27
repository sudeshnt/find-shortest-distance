import math
from route_map.route_map import RouteMap
from utils.utils import Utils

class ShortestRoute:
  
  def __init__(self):
    self._init_route_map()
    
  def _init_route_map(self):
    utils = Utils()
    file_name = utils.get_file_name()
    self.route_map = RouteMap(file_name)

  def get_src_dest_input(self):
    self.src = 'C'
    self.dest = 'H'
    # self.src = self.route_map.get_input_station('on')
    # self.dest = self.route_map.get_input_station('off')

  def _initialize_helpers(self):
    distance_from_src = {}
    adjacent_node = {}
    queue = []

    for station in self.route_map.map:
      distance_from_src[station] = 0 if station == self.src else math.inf
      adjacent_node[station] = None
      queue.append(station)

    return distance_from_src, adjacent_node, queue
  
  def _calculate_shortest_distance_and_stops(self):
    distance_from_src, adjacent_node, queue = self._initialize_helpers()

    while queue:
      key_min = queue[0]
      min_val = distance_from_src[key_min]
      for index in range(1, len(queue)):
        station = queue[index]
        if distance_from_src[station] < min_val:
          key_min = station  
          min_val = distance_from_src[key_min]

      cur = key_min
      queue.remove(cur)
      
      # update distance_from_src and adjacent_node with the nearest station
      for i in self.route_map.map[cur]:
        alternate = self.route_map.map[cur][i] + distance_from_src[cur]
        if distance_from_src[i] > alternate:
          distance_from_src[i] = alternate
          adjacent_node[i] = cur

    # finding stops from destination to source
    stops = [self.dest]
    dest = self.dest
    while True:
      dest = adjacent_node[dest]
      if dest is None:
        break
      stops.insert(0, dest)
    
    return stops, distance_from_src

  def get_shortest_route(self):
    stops, distance_from_src = self._calculate_shortest_distance_and_stops()

    number_of_stops = len(stops) - 1
    destination = stops[number_of_stops]
    time_taken = distance_from_src[destination]

    if time_taken == math.inf:
      print(f'Sorry, there is no route available from {self.src} to {destination}')
    else:
      print(f'Your trip from {self.src} to {destination} includes {number_of_stops} stops and will take {time_taken} minutes')
      print(' -> '.join(stops))
