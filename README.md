# integrate

Module for calculating the area under the curve of a csv file / pandas.DataFrame.

## Usage

In order to run by the terminal, you need to use the following command
```
python3 integral.py -f [path/to/file] -y [index_of_y_columns] -x [index_of_x_column]
```

In a more concrete example
```
python3 integral.py -f teste.csv -y 1 2 3 -x 0
```
To use it as a module, follow the scheme
```
from integral import Integral
[...]
df = pd.read_csv(path_to_file)
[...]
# to get the integration result
res = Integral(df,y=[1,2,3],x=0).integrate_files()
```

### Arguments
* f - stands for files. Gets the path to the files, or an array of dataframes.
* y - the indexes of y axis.
* x - the index of x axis.
* m - stands for the methods that you can use to perform the calculation. The choices are simpson rule, trapezoidal rule or the mean of both.

### Methods
* integrate_files - return the area under the curve.
* stats - return the stats - the same from the describe method of pandas.

## Dependencies
* pandas
* scipy
* numpy
