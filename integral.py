from scipy.integrate import simps    
from numpy import trapz

import numpy as np
import pandas as pd

import argparse


class Integral:

    def __init__(self, file=None, xspacement=None, y=None, x=None) -> None:
        self.prs = argparse.ArgumentParser()
        if file == None:
            # set all the arguments
            self.prs.add_argument('-f', '--files', nargs='+', type=str, required=True)
            self.prs.add_argument('-xs', '--xspacement', type=int, default=5)
            self.prs.add_argument('-x', '--xAxis', type=int, default=0)
            self.prs.add_argument('-y', '--yAxis', nargs='+', type=int, default=1)
            # parse
            args = self.prs.parse_args()

            self.files = self.open_files( args.files )
            self.xs = args.xspacement
            self.x = args.xAxis
            self.y = args.yAxis
        else:
            self.file = pd.read_csv( file )
            self.xs = xspacement
            self.x = x
            self.y = y
        

    def open_files(self, files):
        handlers = []
        # stores all the dataframes in handlers array
        for fs in files:
            handlers.append( pd.read_csv( fs ) )
        
        return handlers


    def _calculate(self, file, y):
        args = {
            'y': file[ file.columns[y] ],
            'dx': self.xs 
        }
        return (simps(**args) + trapz(**args) ) / 2


    def integrate_files( self ):
        file_areas = []

        for file in self.files:
            area = []
            for y in self.y:
                area.append( self._calculate( file, y ) )
            
            file_areas.append( area[:] )
            area.clear()

        return file_areas


    def stats(self):
        for file in self.files:
            return file.describe()


if __name__ == '__main__':
    integ = Integral().integrate_files()
    print( integ[0] if len(integ)==1 else integ )
