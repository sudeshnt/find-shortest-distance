import os.path

class RouteMap:

  def __init__(self, file_name):
    self.file_name = file_name
    self.init_route_map()

  def init_route_map(self):
    try:
      with open(os.path.dirname(__file__) + '/../{}.csv'.format(self.file_name), 'r') as file:
        self.map = self._generate_map(file)
    except EnvironmentError:
      self.file_name = input('File not found. Please check the file existance. If does enter the name correctly: (routes)') or 'routes'
      self.init_route_map()

  def _generate_map(self, file):
    map = {}
    for line in file:
      values = line.split(',')
      src = values[0]
      dest = values[1]
      distance = int(values[2])
      # map source -> destination distance
      if src in map.keys():
        map[src][dest] = distance
      else:
        map[src] = { dest: distance }
      # map destination -> source distance
      if dest in map.keys():
        map[dest][src] = distance
      else:
        map[dest] = { src: distance }
    return map

  def get_input_station(self, type):
    while True:
      station = input(f'What station are you getting {type} the train?')
      if station.lower() not in self.map.keys() and station.upper() not in self.map.keys():
          print('Not a valid station.')
          continue
      else:
        return station.upper()