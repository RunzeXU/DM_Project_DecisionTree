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


train_path = './data/adult.data'
test_path = './data/adult.test'
train = clean_data(train_path)
test = clean_data(test_path)


print(len(train))
print(train[0])
# print(type(train[0]))
