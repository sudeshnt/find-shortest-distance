import argparse

class Utils:

  @staticmethod
  def get_file_name():
    args = Utils._get_cmd_argument()
    if args.file:
      fileName = args.file
    else:
      fileName = input('Please provide csv file name (routes): ') or 'routes'
    return fileName

  @staticmethod
  def _get_cmd_argument(args=[]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    args = parser.parse_args(args)
    return args
