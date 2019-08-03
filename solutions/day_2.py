# dataframe
import numpy
import pandas
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
my_df = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(my_df)
