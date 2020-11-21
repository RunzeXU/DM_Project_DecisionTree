from DecisionTree import *

DT = DecisionTree()

data = [[1, 3], [1, 2], [1, 0], [1, 4], [1, 4], [1, 4], [2, 3]]

print(DT.recurrent_split(data))
print(" 1 ", DT.recurrent_split(data)[0].label)
print(" 2 ", DT.recurrent_split(data)[1])



