import math
from route_map import RouteMap
from util import Util

fileName = Util.get_file_name();
mapclass = RouteMap(fileName);

map = mapclass.map;
# src = mapclass.get_input_station('on')
# dest = mapclass.get_input_station('off')

src = 'C'
dest = 'H'

path = {}
adj_node = {}
queue = []

for station in map:
  path[station] = math.inf
  adj_node[station] = None
  queue.append(station)

path[src] = 0

while queue:
    # find min distance which wasn't marked as current
    key_min = queue[0]
    min_val = path[key_min]
    for n in range(1, len(queue)):
      x = queue[n];
      if path[queue[n]] < min_val:
        key_min = queue[n]  
        min_val = path[key_min]

    cur = key_min
    queue.remove(cur)
    
    for i in map[cur]:
      alternate = map[cur][i] + path[cur]
      if path[i] > alternate:
        path[i] = alternate
        adj_node[i] = cur

print(f'The path between {src} to {dest}')
print(dest, end = '<-')
while True:
    dest = adj_node[dest]
    if dest is None:
        print("")
        break
    print(dest, end='<-')