__author__ = 'sjames'
__copyright__ = 'Copyright (C) 2014 Steven James'
__license__ = "Public Domain"
__version__ = "0.1"
__email__ = "sjames@ctiengr.com"
__status__ = "Beta"

from distutils.core import setup
import py2exe

from glob import glob

setup(console=["sharpimportcsv.py"],
      data_files=data_files)