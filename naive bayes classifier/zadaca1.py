import os

from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

os.environ['OPENBLAS_NUM_THREADS'] = '1'

if __name__ == '__main__':
    dataset = dataset
    encoder = OrdinalEncoder()

    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.75 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(0.75 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = CategoricalNB()

    train_x_enc = encoder.transform(train_x)
    test_x_enc = encoder.transform(test_x)
    classifier.fit(train_x_enc, train_y)

    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x_enc[i]])[0]
        if predicted_class == test_y[i]:
            accuracy += 1

    acc = accuracy / len(test_set)

    print(acc)

    entry = [el for el in input().split(" ")]
    encoded_entry = encoder.transform([entry])
    pred = classifier.predict(encoded_entry)[0]
    input_probabilities = classifier.predict_proba(encoded_entry)

    print(pred)
    print(input_probabilities)

    submit_train_data(train_x_enc, train_y)

    submit_test_data(test_x_enc, test_y)

    submit_classifier(classifier)

    submit_encoder(encoder)
