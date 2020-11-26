from DecisionTree import *
from clean_dict import *

DT = DecisionTree(25)

# data = [[1,'a', -1],[2,'a',1],[3,'a',1],[4,'a',1],[5,'a',-1],
#         [1,'b',1],[2,'b',1],[3,'b',1],[4,'b',1],[5,'b',-1],
#         [1,'c',1],[2,'c',1],[3,'c',1],[4,'c',1],[5,'c',-1],
#         [1,'d',-1],[2,'d',-1],[3,'d',-1],[4,'d',-1],[5,'d',-1],
#         # [3,'b',-1]
#         ]
# print(DT.build_tree(data))
# DT.print_tree()
# print(currentnode.get_info())
# print(DT.classify([3, 'c']))


train_path = 'data/adult.data'
test_path = 'data/adult.test'

train = clean_data(train_path, False)
test = clean_data(test_path, True)
print(DT.build_tree(train))

correct = 0
num_data = 0
for data in test:
    num_data += 1
    predict_label = DT.classify(data)
    if predict_label == data[-1]:
        correct += 1
print(float(correct) / num_data)
print(correct)
print(num_data)
DT.print_tree()