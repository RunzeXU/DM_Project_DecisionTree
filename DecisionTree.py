class decisiontree_node:
    def __init__(self, col=-1, condition=None, left_node=None, right_node=None):
        self.condition = condition
        self.left_node = l_node
        self.right_node = r_node


class DecisionTree:

    def __init__(self, root):
        self.root = None
        self.num_object = 0
        self.num_attribut = 0

    def get_split(sub_set):

        # stop split
        #   all sub' attributes are the same or
        #   all sub' labels are the same
        if len(sub):
            return decisiontree_node(), err

        # split
        best_gini = 1
        best_split = None
        best_condition = None
        for i in range(self.num_attribut):

            current_split, current_condition = split_with_index(sub_set, i)
            current_gini = gini(current_split)

            if current_gini < best_gini:
                best_gini = current_gini
                best_split = current_split
                best_condition = current_condition

        a, a_err = self.get_split(best_split[0])
        b, b_err = self.get_split(best_split[1])

        return decisiontree_node(a, b, best_condition), a_err + b_err

    def split(self, attribute_index, ):
        # for()
        return [a, b], condition

    def build_tree(self, train_set):
        self.num_object = len(self.train_set)
        self.num_attribut = len(train_set[0]) - 1
        self.root, err_object = get_split(train_set)
        err_s = err_object / num_object
        return err_s

    def classify(self, input):
        label = 0
        return label

    def gini(self, indexs):
        gini_value = 0
        return gini_value
