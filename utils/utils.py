import argparse

class Utils:

  def get_file_name(self):
    args = self._get_cmd_argument()
    if args.file:
      fileName = args.file
    else:
      fileName = input('Please provide csv file name (routes): ') or 'routes'
    return fileName

  def _get_cmd_argument(self, args=[]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    args = parser.parse_args(args)
    return args
