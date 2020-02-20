from haversine import haversine, Unit
import csv

def find_neighbors(dist):

    with open('taxistand.csv') as standcsv:
        csv_reader = csv.reader(standcsv, delimiter=',')
        line_count = 0
        stands = []
        """ id, long, lat """
        for row in csv_reader:
            if line_count != 0:
                stands.append([int(row[0]),float(row[2]),float(row[3])])
            line_count += 1

        neighbors = []
        for s in stands:
            neighbors_os_s = [s[0]]
            for s2 in stands:
                if haversine((s[1],s[2]),(s2[1],s2[2])) < dist and not s[0] == s2[0]:
                    neighbors_os_s.append(s2[0])
            neighbors.append(neighbors_os_s)

        with open('neighbors.csv', mode='w') as newFile:
            writer = csv.writer(newFile, delimiter=',')
            writer.writerow(['Stand ID, neighbors'])
            for n in neighbors:
                writer.writerow(n)

find_neighbors(0.5)