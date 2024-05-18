import os

from sklearn.ensemble import RandomForestClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
    # Vashiot kod tuka
    dataset = dataset
    col = int(input())
    train_set = dataset[:int(0.85 * len(dataset))]
    train_X = [[row[i] for i in range(len(row) - 1) if i != col] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_set = dataset[int(0.85 * len(dataset)):]
    test_X = [[row[i] for i in range(len(row) - 1) if i != col] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    forest_classifier = RandomForestClassifier(n_estimators=int(input()), criterion=input(), random_state=0)
    forest_classifier.fit(train_X, train_Y)

    acc = 0

    for i in range(len(test_set)):
        pred = forest_classifier.predict([test_X[i]])[0]
        if pred == test_Y[i]:
            acc += 1

    accuracy = acc / len(test_set)

    print(f'Accuracy: {accuracy}')
    input = [float(el) for el in input().split(" ")]
    input.pop(col)
    print(forest_classifier.predict([input])[0])
    print(forest_classifier.predict_proba([input]))
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii
    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(forest_classifier)
