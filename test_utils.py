import unittest
from unittest import mock
from utils import Utils
from argparse import Namespace

def get_input(text):
  return input(text)

class TestUtils(unittest.TestCase):
  def setUp(self):
    self.utils = Utils()

  def test_get_cmd_argument(self):
    self.assertEqual(self.utils._get_cmd_argument(["--file", "routes"]).file, 'routes')
    
  @mock.patch('builtins.input', return_value="file_name")
  @mock.patch.object(Utils, '_get_cmd_argument', return_value=Namespace(file=None))
  def test_get_file_name(self, x, y):
    self.assertEqual(self.utils.get_file_name(), 'file_name')
