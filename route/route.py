import os.path

class Route:

  def __init__(self, file_name):
    self._file_name = file_name
    self._init_route()

  def _init_route(self):
    try:
      with open(os.path.dirname(__file__) + '/../{}.csv'.format(self._file_name), 'r') as file:
        self._map = self._generate_route(file)
    except EnvironmentError:
      self._file_name = input('File not found. Please check the file existence. If does enter the name correctly: (routes)') or 'routes'
      self._init_route()

  def _generate_route(self, file):
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

  def get_map(self):
    return self._map