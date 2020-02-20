import numpy as np
from sklearn.linear_model import LinearRegression
import csv
from operator import itemgetter
import math
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state


def neighbor_prediction():
    with open('monthdata_process_small.csv') as datacsv:
        csv_reader = csv.reader(datacsv, delimiter=',')
        line_count = 0
        data = []
        """['Stand ID','Stand name','Latitude','Longitude','passengers this week', 'year - month'] to ['Stand ID', 'passengers this week', 'year', 'month']"""
        for row in csv_reader:
            if line_count != 0 and row != []:
                date = row[5].split("-")
                data.append([int(row[0]),  int(row[4]), int(date[0]), int(date[1])])
            line_count += 1

    npdata = np.asarray(data)

    with open('neighbors.csv') as standcsv:
        csv_reader = csv.reader(standcsv, delimiter=',')
        line_count = 0
        neighbors = []
        """ id, long, lat """
        for row in csv_reader:
            if line_count != 0:
                if row != []:
                    neighbors.append(row)
            line_count += 1

    y = npdata[-100:,:]
    x = npdata[:-100,:]
    predictions = []


    for d in y:
        for n in neighbors[d[0]-1]:
            #find n at time t-1
            passengers = []
            n = int(n)
            for d2 in x:
                if d2[0] == n:# and d2[2] == d[2] and d2[3]-1 == d[3]:
                    passengers.append(d2[1])
                elif d2[0] == n and d2[2]-1 == d[2] and d2[3] == 1 and d[3] == 12:
                    passengers.append(d2[1])
        if len(passengers) > 0:
            predictions.append(math.floor(sum(passengers)/len(passengers)))
        else:
            predictions.append(0)

    print(np.asarray(predictions))
    print(y[:,1])

neighbor_prediction()