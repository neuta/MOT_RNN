import mayavi.mlab as mlab
import numpy as np
import torch
import pandas as pd

import argparse
import glob
from pathlib import Path

import common_utils as utl

from visual_utils import visualize_utils_3D as V


def parse_config():

	parser = argparse.ArgumentParser(description='arg parser')
	parser.add_argument('--data_path', type=str, default='demo_data', help='specify the point cloud data file or directory')

	args = parser.parse_args()

	return args


def main():
	args = parse_config()
	print('Start'.center(100,'-'))
    

	print('Visualization done.'.center(100,'-'))







    #print('Visualization done.')




if __name__ == '__main__':
    main()
