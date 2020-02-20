import csv
from operator import itemgetter
import numpy as np
from _datetime import datetime

def DataTransformation(file):
    with open(file) as datacsv:
        csv_reader = csv.reader(datacsv, delimiter=',')
        line_count = 0
        data = []
        """ stand, timestamp """
        for row in csv_reader:
            if line_count != 0:
                data.append([int(float(row[3])), int(row[5]), 1])
            line_count += 1

    for d in data:
        d[1] = datetime.utcfromtimestamp(d[1]).strftime('%Y-%m')


    npdata = data
    for i in range(len(npdata)):
        if not npdata[i][0] == 0:
            for j in range(i+1,len(npdata)):
                if npdata[i][0] == npdata[j][0] and npdata[i][1] == npdata[j][1]:
                    npdata[i][2] = int(npdata[i][2])+1
                    npdata[j] = [0,npdata[j][1],0]
                elif npdata[i][1] != npdata[j][1]:
                    break

    data = []
    for d in npdata:
        if not d[0] == 0:
            data.append(d)


    with open('taxistand.csv') as standcsv:
        csv_reader = csv.reader(standcsv, delimiter=',')
        line_count = 0
        stands = []
        """ id,name,lat,long """
        for row in csv_reader:
            if line_count != 0:
                stands.append([row[0],row[1], float(row[2]), float(row[3])])
            line_count += 1


    with open('month'+file, mode='w') as newFile:
        writer = csv.writer(newFile, delimiter=',')
        writer.writerow(['Stand ID, Stand name','Latitude','Longitude','passengers this month', 'year - month'])
        for d in data:
            writer.writerow([stands[d[0]-1][0],stands[d[0]-1][1],stands[d[0]-1][2],stands[d[0]-1][3],d[2],d[1]])

DataTransformation('data_process.csv')