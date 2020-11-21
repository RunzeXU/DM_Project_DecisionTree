from DecisionTree import *

DT = DecisionTree()

data = [[1,'a', -1],[2,'a',1],[3,'a',1],[4,'a',1],[5,'a',-1],
        [1,'b',1],[2,'b',1],[3,'b',1],[4,'b',1],[5,'b',-1],
        [1,'c',1],[2,'c',1],[3,'c',1],[4,'c',1],[5,'c',-1],
        [1,'d',-1],[2,'d',-1],[3,'d',-1],[4,'d',-1],[5,'d',-1],
        # [3,'b',-1]
        ]
print(DT.build_tree(data))
DT.print_tree()
# print(currentnode.get_info())
# print(DT.classify([3, 'c']))



