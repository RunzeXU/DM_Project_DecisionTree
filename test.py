from DecisionTree import *

DT = DecisionTree()


data = [[1, 1], [2, 1], [3, 1], [4444, 1]]

print(DT.recurrent_split(data))
print(DT.recurrent_split(data)[0].label)


