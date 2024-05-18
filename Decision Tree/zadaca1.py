import os

from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
# Vashiot kod tuka
    dataset = dataset
    encoder = OrdinalEncoder()

    encoder.fit([row[:-1] for row in dataset])

    percent = int(input())
    p = (100 - percent) / 100

    train_set = dataset[int(p * len(dataset)):]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    train_X = encoder.transform(train_X)

    test_set = dataset[:int(p * len(dataset))]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]
    test_X = encoder.transform(test_X)

    classifier = DecisionTreeClassifier(criterion=input(), random_state=0)
    classifier.fit(train_X, train_Y)

    acc = 0

    for i in range(len(test_set)):
        pred = classifier.predict([test_X[i]])[0]
        if pred == test_Y[i]:
            acc += 1

    accuracy = acc/len(test_set)
    print(f'Depth: {classifier.get_depth()}')
    print(f'Number of leaves: {classifier.get_n_leaves()}')
    print(f'Accuracy: {accuracy}')
    features_importances = list(classifier.feature_importances_)
    print(f'Most important feature: {features_importances.index(max(features_importances))}')
    print(f'Least important feature: {features_importances.index(min(features_importances))}')
# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
# klasifikatorot i encoderot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

# submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

# submit na klasifikatorot
    submit_classifier(classifier)

# submit na encoderot
    submit_encoder(encoder)
