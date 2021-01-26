import math
from route_map.route_map import RouteMap
from utils.utils import Utils

utils = Utils()

file_name = utils.get_file_name()
route_map = RouteMap(file_name)

map = route_map.map
src = route_map.get_input_station('on')
dest = route_map.get_input_station('off')

# src = 'C'
# dest = 'H'

# initializing helpers
path = {}
adjacent = {}
queue = []

for station in map:
  path[station] = 0 if station == src else math.inf
  adjacent[station] = None
  queue.append(station)

# 
while queue:
  # find min distance which wasn't marked as current
  key_min = queue[0]
  min_val = path[key_min]
  for index in range(1, len(queue)):
    station = queue[index]
    if path[station] < min_val:
      key_min = station  
      min_val = path[key_min]

  cur = key_min
  queue.remove(cur)
  
  # update path and adjacent with the nearest station
  for i in map[cur]:
    alternate = map[cur][i] + path[cur]
    if path[i] > alternate:
      path[i] = alternate
      adjacent[i] = cur

# finding stops from destination to source
stops = [dest]
while True:
  dest = adjacent[dest]
  if dest is None:
    break
  stops.insert(0, dest)

# printing results
number_of_stops = len(stops) - 1
destination = stops[number_of_stops]
time_taken = path[destination]
if time_taken == math.inf:
  print(f'Sorry, there is no route available from {src} to {destination}')
else:
  print(f'Your trip from {src} to {destination} includes {number_of_stops} stops and will take {time_taken} minutes')
  print(' -> '.join(stops))