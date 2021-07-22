from scipy.integrate import simps    
from numpy import trapz

import numpy as np
import pandas as pd

import argparse

class Integral:

    def __init__(self, file=None, y=1, x=0, cmd=False) -> None:
        if cmd:
            self.prs = argparse.ArgumentParser(description='Integrate Module - For calculating the area under the curve.')
            
            # set all the arguments
            self.prs.add_argument('-f', '--files', nargs='+', type=str, required=True, help='Path to the data file.')
            self.prs.add_argument('-y', '--yAxis', nargs='+', type=int, default=[1], help='Index for the y axis. (Index starting in 0).')
            self.prs.add_argument('-x', '--xAxis', type=int, default=0, help='Index for the x axis.')
            # parse
            args = self.prs.parse_args()

            self.files = self.open_files( args.files )
            self.y = args.yAxis
            self.x = args.xAxis

        else:
            self.files = file if isinstance(file, list) else [file]
            self.y = y if isinstance(y,list) else [y]
            self.x = x
        

    def open_files(self, files):
        handlers = []
        # stores all the dataframes in handlers array
        for fs in files:
            handlers.append( pd.read_csv( fs ) )
        
        return handlers


    def _calculate(self, file, y, x):
        args = {
            'y': file[ file.columns[y] ],
            'x': file[ file.columns[x] ]
        }
        return (simps(**args) + trapz(**args) ) / 2


    def integrate_files( self ):
        file_areas = []

        for file in self.files:
            area = []
            for y in self.y:
                area.append( self._calculate( file, y, self.x ) )
            
            file_areas.append( area[:] )
            area.clear()

        return file_areas


    def stats(self):
        for file in self.files:
            return file.describe()


if __name__ == '__main__':
    integ = Integral(cmd=True).integrate_files()
    print( integ[0] if len(integ)==1 else integ )
