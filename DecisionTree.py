class node:
    def __init__(self, label=None, index=None, condition=None, left_node=None, right_node=None):
        self.label = label
        self.index = index
        self.condition = condition
        self.left_node = left_node
        self.right_node = right_node


class DecisionTree:

    def __init__(self,):
        self.root = None
        self.num_object = 0
        self.num_attribut = 0

    def recurrent_split(sub_set):

        # stop split
        #   all sub' attributes are the same or
        #   all sub' labels are the same
        if 1:
            err = 0
            return node(), err

        # split
        best_gini = 1
        best_split = None
        best_condition = None
        index = None
        for i in range(self.num_attribut):

            current_split, current_condition, current_gini = split_with_index(sub_set, i)

            if current_gini < best_gini:
                best_gini = current_gini
                best_split = current_split
                best_condition = current_condition
                index = i

        a, a_err = self.recurrent_split(best_split[0])
        b, b_err = self.recurrent_split(best_split[1])

        return node(index, a, b, best_condition), a_err + b_err

    # find in what condition is the
    def split_with_index(self, sub_set, attribute_index,):
        # using dictionary
        # for(condition)
        a, b = sub_set
        condition = None
        gini_value = 0
        return [a, b], condition, gini_value

    def build_tree(self, train_set):
        self.num_object = len(self.train_set)
        self.num_attribut = len(train_set[0]) - 1
        self.root, err_object = self.recurrent_split(train_set)
        err_s = err_object / self.num_object
        return err_s

    def classify(self, input):
        current_node = self.root
        while(not current_node.label):

            if(isinstance(current_node.condition,int)):
                if (input[current_node.index] < current_node.condition):
                    current_node = current_node.left_node
                else:
                    current_node = current_node.right_node

            else:
                if (input[current_node.index] == current_node.condition):
                    current_node = current_node.left_node
                else:
                    current_node = current_node.right_node

        return current_node.label

    def gini(self, indexs):
        gini_value = 0
        return gini_value
