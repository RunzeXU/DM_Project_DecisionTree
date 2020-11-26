def clean_data(path, test):
    data = []
    # index = 0
    with open(path, 'r') as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            if test and index == 0:
                continue
            temp = []
            line = line.strip()
            value = line.split(', ')
            for i in range(len(value)):
                if i == len(value)-2:
                    continue

                if i == len(value)-1:
                    if test:
                        if value[i] == '<=50K.':
                            temp.append('0')
                        else:
                            temp.append('1')
                        continue
                    else:
                        if value[i] == '<=50K':
                            temp.append('0')
                        else:
                            temp.append('1')
                        continue

                if i == len(value) - 3 or i == len(value) - 4 or i == len(value) - 5 or i == len(
                        value) - 11 or i == len(value) - 13 or i == len(value) - 15:
                    temp.append(int(value[i]))
                    continue
                temp.append(value[i])
            if '?' not in temp and index != len(lines)-1:
                data.append(temp)
            # index += 1
            # if index >= 3000:
            #     break

    f.close()

    return data


# train_path = 'data/adult.data'
# test_path = 'data/adult.test'
# train = clean_data(train_path)
# test = clean_data(test_path)
#
# col_labels = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
#               'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
#               'hours_per_week', 'wage_class']
#
#
# for line in train:
#     combine_label = zip(col_labels, line)
#     print(dict(combine_label))
# print(len(train))