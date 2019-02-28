from train_test_dataset_label import train_test_dataset_label

data = train_test_dataset_label

training_dataset=data.get_training_dataset(data)

print('training dataset:')

print(training_dataset)
f = open('trainDataset.txt', 'w')
f.write(str(training_dataset) + "\n")
f.close()

test_dataset = data.get_testing_dataset(data)

print('testing dataset:')

print(test_dataset)
f1 = open('testDataset.txt', 'w')
f1.write(str(test_dataset) + "\n")
f1.close()