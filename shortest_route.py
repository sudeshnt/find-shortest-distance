import math
from route_map.route_map import RouteMap
from utils.utils import Utils

class ShortestRoute:

  def _get_file_name(self):
    utils = Utils()
    return utils.get_file_name()

  def init_route_map(self):
    file_name = self._get_file_name()
    self.route_map = RouteMap(file_name)

  def get_src_dest_input(self):
    self.src = self.route_map.get_input_station('on')
    self.dest = self.route_map.get_input_station('off')

  def _initialize_helpers(self):
    distance_from_src = {}
    adjacent_node = {}
    unvisited = []

    for station in self.route_map.map:
      distance_from_src[station] = 0 if station == self.src else math.inf
      adjacent_node[station] = None
      unvisited.append(station)

    return distance_from_src, adjacent_node, unvisited
  
  def _calculate_shortest_distance_and_stops(self):
    distance_from_src, adjacent_node, unvisited = self._initialize_helpers()

    while unvisited:
      current_node = unvisited[0]
      distance_from_src_to_currently_visited = distance_from_src[current_node]
      for index in range(1, len(unvisited)):
        unvisited_station = unvisited[index]
        if distance_from_src[unvisited_station] < distance_from_src_to_currently_visited:
          current_node = unvisited_station  
          distance_from_src_to_currently_visited = distance_from_src[current_node]

      unvisited.remove(current_node)
      
      # update distance_from_src and adjacent_node with the nearest station
      distance_to_neighbours = self.route_map.map[current_node]
      for neighbour in distance_to_neighbours:
        alternate = distance_to_neighbours[neighbour] + distance_from_src[current_node]
        if alternate < distance_from_src[neighbour]:
          distance_from_src[neighbour] = alternate
          adjacent_node[neighbour] = current_node

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
