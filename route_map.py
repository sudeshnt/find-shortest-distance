class RouteMap:

  def __init__(self, fileName):
    self.init_route_map(fileName)

  def init_route_map(self, fileName):
    try:
      with open('{}.csv'.format(fileName), 'r') as file:
        self.map = self.__generate_map(file)
    except EnvironmentError:
      fileName = input('File not found. Enter a valid file name: ')
      self.init_route_map(fileName)

  def __generate_map(self, file):
    map = {}
    for line in file:
      values = line.split(',')
      src = values[0]
      dest = values[1]
      distance = int(values[2])
      if src in map.keys():
        map[src][dest] = distance
      else:
        map[src] = {dest: distance}
    return map

  def get_input_station(self, type):
    while True:
      src = input(f'What station are you getting {type} the train?')
      if src not in self.map.keys():
          print('Not a valid station.')
      else:
        return src