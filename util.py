import argparse

class Util:
  @staticmethod
  def get_file_name():
    parser = argparse.ArgumentParser();
    parser.add_argument("--file");
    args = parser.parse_args()
    if args.file:
      fileName = args.file
    else:
      fileName = 'routes'
      # fileName = input('Please provide csv file name: ')
    return fileName
