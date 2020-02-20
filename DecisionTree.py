import numpy as np
from sklearn import tree
import csv
from operator import itemgetter
import math

def decision_tree(file):
    with open(file) as datacsv:
        csv_reader = csv.reader(datacsv, delimiter=',')
        line_count = 0
        data = []
        """['Stand ID','Stand name','Latitude','Longitude','passengers this week', 'year - month'] to ['Stand ID','passengers this week', 'year - month']"""
        for row in csv_reader:
            if line_count != 0 and row != []:
                date = row[5].split("-")
                data.append([row[0], int(row[4]), date[0], date[1]])
            line_count += 1


    npdata = np.asarray(data)
    print(npdata)

    X = npdata[100:, [0,2,3]]
    y = npdata[100:,1]

    x_test = X[:100,:]

    model = tree.DecisionTreeClassifier(criterion='gini')
    model.fit(X, y)
    model.score(X, y)
    # Predict Output
    predicted = model.predict(x_test)
    print(predicted)

decision_tree('monthdata_process.csv')