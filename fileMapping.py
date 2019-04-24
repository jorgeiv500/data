import json
import csv
import numpy as np


def createBuidlingIndex():
    with open("BuildingList.json") as f:
        # get all the building names and sort
        data = json.load(f)
        data = list(data.keys())
        for i in range(len(data)):
            data[i] = data[i].lower().strip()
        data = sorted(data)

    with open("MapKeys", 'w') as f:
        # save to file
        for item in data:
            f.write("{}\n".format(item))


def changeMapping():
    with open("MapKeys") as f:
        k = f.read().split("\n")
    array = np.zeros((len(k)-1, len(k)-1), dtype=list)
    with open('Distance_Matrix.json') as f:
        data = json.load(f)
        for i in data:
            # get the first and second building name
            first = i.split("|")[0].strip()
            second = i.split("|")[1].strip()

            # convert the building name to index
            index1 = k.index(first)
            index2 = k.index(second)

            # save the data to the 2d array: bidirectional map
            array[index1][index2] = data[i][0]
            array[index2][index1] = data[i][0]

    json.dump(array.tolist(), open('time_matrix.json', 'w'))


changeMapping()
api_key = 'AIzaSyAB7V8GGSxwkvmMgYFGkFx0s3cCSM0YHC0'
