discrete_index = [1, 3, 4, 5, 6, 7, 8]

class node:
    def __init__(self, label=None, index=None, condition=None, left_node=None, right_node=None):
        self.label = label
        self.index = index
        self.condition = condition
        self.left_node = left_node
        self.right_node = right_node


class DecisionTree:

    def __init__(self):
        self.root = None
        self.num_object = 0
        self.num_attribute = 0

    def recurrent_split(self, sub_set):

        # stop split, all sub_set labels are the same
        current_label = sub_set[0][-1]  # subset label
        flag = 0
        for record in sub_set:
            if record[-1] != current_label:
                flag = 1
                break
            else:
                continue
        if flag == 0:
            return node(label=current_label), 0

        # stop split, all sub_attributes are the same
        # for i in self.num_attribute:
        #     for record in sub_set[][]
        flag_1 = 0
        # self.num_attribute = len(sub_set[0]) - 1
        for i in range(1, len(sub_set)):
            for j in range(self.num_attribute):
                print(i, j)
                if sub_set[i][j] != sub_set[i - 1][j]:

                    flag_1 = 1
                    break
                else:
                    continue

        if flag_1 == 0:
            dict = {}
            for record in sub_set:
                if record[-1] not in dict.keys():
                    dict[record[-1]] = 1
                else:
                    dict[record[-1]] += 1
            value_list = list(dict.values())

            key = list(dict.keys())[value_list.index(max(value_list))]

            err = len(sub_set) - max(dict.values())

            return node(label=key), err

        # split
        best_gini = 0.5
        best_split = None
        best_condition = None
        index = None
        for i in range(self.num_attribute):

            current_split, current_condition, current_gini = self.split_with_index(sub_set, i)

            if current_gini < best_gini:
                best_gini = current_gini
                best_split = current_split
                best_condition = current_condition
                index = i

        a, a_err = self.recurrent_split(best_split[0])
        b, b_err = self.recurrent_split(best_split[1])

        return node(index, a, b, best_condition), a_err + b_err

    def split_with_index(self, sub_set, attribute_index):
        value = []
        best_gini = 1
        best_condition = None
        subset_left = []
        subset_right = []

        for element in sub_set:
            if element[attribute_index] not in value:
                value.append(element[attribute_index])
        num_attributes = len(value)

        for index in range(num_attributes):

            left_pos, left_neg, right_pos, right_neg = 0
            left = []
            right = []
            condition = value[index]

            if attribute_index in discrete_index:
                for i, data in enumerate(sub_set):
                    if data == condition:
                        left.append(data)
                        if data[-1] == '1':
                            left_pos += 1
                        else:
                            left_neg += 1
                    else:
                        right.append(data)
                        if data[-1] == '1':
                            right_pos += 1
                        else:
                            right_neg += 1
                temp_gini = self.get_gini_index([[[1, left_pos], [1, left_neg]], [[1, right_pos], [1, right_neg]]],
                                                [0, 1])

                if temp_gini < best_gini:
                    best_gini = temp_gini
                    subset_left = left
                    subset_right = right
                    best_condition = condition
            else:
                continue
                # todo: continuous attribute

        return [subset_left, subset_right], best_condition, best_gini

    def build_tree(self, train_set):
        self.num_object = len(self.train_set)
        self.num_attribute = len(train_set[0]) - 1
        self.root, err_object = self.recurrent_split(train_set)
        err_s = err_object / self.num_object
        return err_s

    def classify(self, input):
        current_node = self.root
        while not current_node.label:

            if isinstance(current_node.condition, int):
                if input[current_node.index] < current_node.condition:
                    current_node = current_node.left_node
                else:
                    current_node = current_node.right_node

            else:
                if input[current_node.index] == current_node.condition:
                    current_node = current_node.left_node
                else:
                    current_node = current_node.right_node

        return current_node.label

    # calculate the Gini index for a split dataset
    def get_gini_index(self, groups, classes):
        # count all samples at split point
        num_instances = float(sum([len(group) for group in groups]))

        # sum weighted Gini index for each group
        gini = 0.0
        for group in groups:
            size = float(len(group))
            # avoid divided by zero
            if size == 0:
                continue
            score = 0.0
            # score the group based on the score for each class
            for class_val in classes:
                p = [row[-1] for row in group].count(class_val) / size
                score += p * p
            # weight the group score by its relative size
            gini += (1.0 - score) * (size / num_instances)

        return gini
