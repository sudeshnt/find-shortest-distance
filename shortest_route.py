import math
from routes.routes import Routes
from utils.utils import Utils

class ShortestRoute(Routes):
  def __init__(self):
    file_name = Utils.get_file_name()
    Routes.__init__(self, file_name)

  def _get_input_station(self, type):
    while True:
      station = input(f'What station are you getting {type} the train?')
      if station.lower() not in self._map.keys() and station.upper() not in self._map.keys():
          print('Not a valid station.')
          continue
      else:
        return station.upper()
  
  def get_src_dest_input(self):
    self.src = self._get_input_station('on')
    self.dest = self._get_input_station('off')

  def _initialize_helpers(self):
    distance_from_src = {}
    adjacent_node = {}
    unvisited = []

    for station in self._map:
      distance_from_src[station] = 0 if station == self.src else math.inf
      adjacent_node[station] = None
      unvisited.append(station)

    return distance_from_src, adjacent_node, unvisited
  
  def _calculate_shortest_distance_and_stops(self):
    distance_from_src, adjacent_node, unvisited = self._initialize_helpers()

    while unvisited:
      current_node = None
      for node in unvisited:
        if (current_node == None or distance_from_src[node] < distance_from_src[current_node]):
          current_node = node

      unvisited.remove(current_node)
      
      # update distance_from_src and adjacent_node with the nearest station
      distances_from_current = self._map[current_node]
      for neighbor in distances_from_current:
        alternate = distance_from_src[current_node] + distances_from_current[neighbor]
        if alternate < distance_from_src[neighbor]:
          distance_from_src[neighbor] = alternate
          adjacent_node[neighbor] = current_node

    # finding stops from destination to source
    dest = self.dest
    stops = [dest]
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
