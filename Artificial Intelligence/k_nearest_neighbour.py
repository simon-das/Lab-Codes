import numpy as np
import matplotlib.pyplot as plt

def most_found_point(nghbr_labels):
    lst = []
    for i in range(len(nghbr_labels)):
        if nghbr_labels[i] not in lst:
            lst.append(nghbr_labels[i])

    most_counted = ''
    n_most_counted = None

    for i in range(len(lst)):
        count = nghbr_labels.count(lst[i])
        if n_most_counted == None:
            most_counted = lst[i]
            n_most_counted = count
        elif n_most_counted < count:
            most_counted = lst[i]
            n_most_counted = count
        elif n_most_counted == count:
            most_counted = None

    return most_counted
    

def find_nghbr(p, data, labels, k):
    number_of_dimensions = len(p)
    nghbrs = []
    nghbr_labels = []

    for i in range(k):
        nearest_id = None
        smallest_dist = None
        
        for j in range(len(data)):
            eucl_dist = 0
            for d in range(number_of_dimensions):
                dist = abs(p[d] - data[j][d])
                eucl_dist += dist

            eucl_dist = np.sqrt(eucl_dist)

            if smallest_dist == None:
                smallest_dist = eucl_dist
                nearest_id = j
            elif smallest_dist > eucl_dist:
                smallest_dist = eucl_dist
                nearest_id = j

        nghbrs.append(data[nearest_id])
        nghbr_labels.append(labels[nearest_id])

        data.remove(data[nearest_id])
        labels.remove(labels[nearest_id])

    return nghbr_labels
            

def knn(p, data, labels, k=3):
    while True:
        nghbr_lbls = find_nghbr(p, data, labels, k)
        label = most_found_point(nghbr_lbls)
        if label != None:
            break
        k += 1
        if k >= len(data):
            break
    return label

# Input data - [SAT Score, GPA]
X = [[1590,2.9], [1540,2.7], [1600,2.6], [1590,2.7], [1520,2.5], [1540,2.4], [1560,2.3], [1490,2.3], [1510,2.4],
     [1350,3.9], [1360,3.7], [1370,3.8], [1380,3.7], [1410,3.6], [1420,3.9], [1430,3.4], [1450,3.7], [1460,3.2],
     [1590,3.9], [1540,3.7], [1600,3.6], [1490,3.7], [1520,3.5], [1540,3.4], [1560,3.3], [1460,3.3], [1510,3.4],
     [1340,2.9], [1360,2.4], [1320,2.5], [1380,2.6], [1400,2.1], [1320,2.5], [1310,2.7], [1410,2.1], [1305,2.5],
     [1460,2.7], [1500,2.9], [1300,3.5], [1320,3.6], [1400,2.7], [1300,3.1], [1350,3.1], [1360,2.9], [1305,3.9], 
     [1430,3.0], [1440,2.3], [1440,2.5], [1380,2.1], [1430,2.1], [1400,2.5], [1420,2.3], [1310,2.1], [1350,2.0]]

# Labels - Accepted or Rejected
Y = ['accepted','accepted','accepted','accepted','accepted','accepted','accepted','accepted','accepted',
     'accepted','accepted','accepted','accepted','accepted','accepted','accepted','accepted','accepted',
     'accepted','accepted','accepted','accepted','accepted','accepted','accepted','accepted','accepted',
     'rejected','rejected','rejected','rejected','rejected','rejected','rejected','rejected','rejected',
     'rejected','rejected','rejected','rejected','rejected','rejected','rejected','rejected','rejected',
     'rejected','rejected','rejected','rejected','rejected','rejected','rejected','rejected','rejected']


p = [1500, 2.3]
print(knn(p, X, Y, 5))
