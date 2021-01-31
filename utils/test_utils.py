import unittest
from unittest import mock
from utils.utils import Utils
from argparse import Namespace

def get_input(text):
  return input(text)

class TestUtils(unittest.TestCase):

  def test_get_cmd_argument(self):
    print('get_cmd_argument should return extracted filename from command line arguments')
    self.assertEqual(Utils._get_cmd_argument(["--file", "file_name"]).file, 'file_name')
    
  @mock.patch.object(Utils, '_get_cmd_argument', return_value=Namespace(file=None))
  @mock.patch('builtins.input', return_value="file_name")
  def test_get_file_name(self, mock_input, mock_get_cmd_argument):
    print('get_file_name should return user entered filename')
    file_name = Utils.get_file_name()
    mock_get_cmd_argument.assert_called()
    self.assertEqual(file_name, 'file_name')
