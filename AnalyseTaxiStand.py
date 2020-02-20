import csv
from operator import itemgetter

def kNearestNeighbors(stands, standID, k):
    """ change name because it that's a different algorithm to label nodes """
    long = stands[standID - 1][1]
    lat = stands[standID - 1][2]
    neighbors = []
    distances = []
    for i in stands:
        if i[0] == standID:
            continue
        if len(neighbors) < k:
            neighbors.append(i[0])
            distances.append(abs(i[1]-stands[standID-1][1])+abs(i[2]-stands[standID-1][2]))
            """ manhatten distance """
        else:
            dist = abs(i[1]-stands[standID-1][1])+abs(i[2]-stands[standID-1][2])
            if dist < max(distances):
                pos = distances.index(max(distances))
                neighbors[pos] = i[0]
                distances[pos] = dist
    return neighbors

def analyseTaxiStand(standID):
    print('test')
    with open('taxistand.csv') as standcsv:
        csv_reader = csv.reader(standcsv, delimiter=',')
        line_count = 0
        stands = []
        """ id, long, lat """
        for row in csv_reader:
            if line_count != 0:
                stands.append([int(row[0]),float(row[2]),float(row[3])])
            line_count += 1
        print(stands)

        k = 3
        """ StandIDs of the k nearest neighbors """
        neighbors = kNearestNeighbors(stands, standID, k)

        """ change over time """
        with open('data_process_small.csv') as datacsv:
            csv_reader = csv.reader(datacsv, delimiter=',')
            line_count = 0
            data = []
            """ stand, timestamp """
            for row in csv_reader:
                if line_count != 0:
                    data.append([int(float(row[3])),int(row[5])])
                line_count += 1
        data.sort(key=itemgetter(1))
        times = [[0]*(k+2)]
        """" init element for the first if in the following for loop """
        time = 0
        for d in data:
            if times[time][0] != d[1]:
                times.append([0]*(k+2))
                time += 1
                times[time][0] = d[1]
            if d[0] == standID:
                times[time][1] += 1
            for n in range(len(neighbors)):
                if d[0] == neighbors[n]:
                    times[time][2+n] += 1
        if times[0][1] == 0:
            times.pop(0)
            """ remove init element """
        for t in times:
            print(t)


analyseTaxiStand(1)