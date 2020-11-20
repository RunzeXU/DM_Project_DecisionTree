def clean_data(path):
    data = []
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            temp = []
            line = line.strip()
            value = line.split(', ')
            for i in range(len(value)):
                if i == len(value)-2:
                    continue

                if i == len(value)-1:
                    if value[i] == '<=50K':
                        temp.append('0')
                    else:
                        temp.append('1')
                    continue

                temp.append(value[i])
            data.append(temp)
            line = f.readline()

    print(len(data))
    for index, line in enumerate(data):
        for item in line:
            if item == '?' or index == len(data)-1:
                del data[index]
                continue
    print(len(data))

    for index, line in enumerate(data):
        for item in line:
            if item == '?' or index == len(data)-1:
                del data[index]
                continue
    print(len(data))

    f.close()

    return data


train_path = 'data/adult.data'
test_path = 'data/adult.test'
train = clean_data(train_path)
test = clean_data(test_path)

col_labels = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
              'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
              'hours_per_week', 'wage_class']


for line in train:
    conbine_label = zip(col_labels, line)
    # print(dict(conbine_label))

