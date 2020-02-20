import csv
from geopy.geocoders import Nominatim

def find_important_locations():
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

    #npdata = np.asarray(data)

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

    #add neighbors of neighbors to neighbors to cluster the neighborshoods
    for n in neighbors:
        for n2 in n:
            if n2 != n[0]:
                for n3 in neighbors[int(n2)-1]:
                    if n3 not in n:
                        n.append(n3)

    for n in neighbors:
        for n2 in n:
            if n2 != n[0]:
                neighbors[int(n2)-1] = []

    neighbors = [x for x in neighbors if x != []]

    with open('taxistand.csv') as standcsv:
        csv_reader = csv.reader(standcsv, delimiter=',')
        line_count = 0
        stands = []
        """ id, long, lat """
        for row in csv_reader:
            if line_count != 0:
                stands.append([int(row[0]),float(row[2]),float(row[3])])
            line_count += 1

    cluster_centers = []
    for n in neighbors:
        long = 0
        lat = 0
        for n2 in n:
            long += stands[int(n2)-1][1]
            lat += stands[int(n2)-1][2]
        long /= len(n)
        lat /= len(n)
        cluster_centers.append([n,long,lat,0])

    for d in data:
        for c in cluster_centers:
            if str(d[0]) in c[0]:
                c[3] += d[1]

    important_places = []
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    for c in cluster_centers:
        if c[3] > 5000:
            place = geolocator.reverse(','.join([str(c[1]),str(c[2])]))
            print(place)
            important_places.append(place)

    print(important_places)
    return important_places

find_important_locations()