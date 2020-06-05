import numpy

a =numpy.arange(0,40).reshape(5,2,4)
print(a)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]]
#
#  [[ 8  9 10 11]
#   [12 13 14 15]]
#
#  [[16 17 18 19]
#   [20 21 22 23]]
#
#  [[24 25 26 27]
#   [28 29 30 31]]
#
#  [[32 33 34 35]
#   [36 37 38 39]]]

# [[[ 0  1  2  3  4]
#   [ 5  6  7  8  9]
#   [10 11 12 13 14]]
#
#  [[15 16 17 18 19]
#   [20 21 22 23 24]
#   [25 26 27 28 29]]]

# [[[ 0  1]
#   [ 2  3]]
#
#  [[ 4  5]
#   [ 6  7]]
#
#  [[ 8  9]
#   [10 11]]]
#索引取位置的时候是按照广播的方式去取的，广播的原则是从最后一个参数开始，例如从最后一个与倒数第二个形状开始广播，再与前一个广播依次类推...
print(a[:,[0,1],[[0,0],[1,1]]])
# print(a[:,[(0,1),(1,1)],[(0),(1)]])
# a = numpy.array([0,1])
# b = numpy.array([[0,0],[1,1]])
# print(a*b)
# a = numpy.arange(0,4).reshape(2,2,2)
# b = numpy.arange(0,6).reshape(3,2)
# print(a)
# print('========')
# print(b)
# print('========')
# print(numpy.array([(0,0),(1,1)]).shape)
