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

    for index, line in enumerate(data):
        for item in line:
            if item == '?':
                del data[index]
                continue
            # del line[len(line)-2]

    print(len(data))
    f.close()

    return data


train_path = 'adult.data'
test_path = 'adult.test'
train = clean_data(train_path)
test = clean_data(test_path)

col_labels = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
              'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
              'hours_per_week', 'wage_class']




print(len(train[0]))
print(train[0])
x = train[0]
print (x[1])
list_account = x.count('Male')
print(list_account)
conbine = zip(col_labels,x)
print(dict(conbine))

for line in train:
    conbine_label = zip(col_labels, line)
    print(dict(conbine_label))

    


# print(type(train[0]))
