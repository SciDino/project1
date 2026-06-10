import requests
import json

APIkey = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjUyNGVlN2U3NjRmNjRmZmU4YjZiNTNjMTE5MGJjZGYyIiwiaCI6Im11cm11cjY0In0=" #CONFIDENTIAL BTW

#setting parameters
parameters = {
    "api_key": APIkey,
    "start": "139.87264766867165, 35.6636123530917",
    "end": "139.70053911753428, 35.689746067501105"
}

#setting the urls
carurl = "https://api.openrouteservice.org/v2/directions/driving-car"
walkurl = "https://api.openrouteservice.org/v2/directions/foot-walking"
cycleurl = "https://api.openrouteservice.org/v2/directions/cycling-regular"
truckurl = "https://api.openrouteservice.org/v2/directions/driving-hgv"

#getting response
carresponse = requests.get(carurl, params = parameters)
walkresponse = requests.get(walkurl, params = parameters)
cycleresponse = requests.get(cycleurl, params = parameters)
truckresponse = requests.get(truckurl, params = parameters)

#converting to python dictionary
cardictionary = carresponse.json()
walkdictionary = walkresponse.json()
cycledictionary = cycleresponse.json()
truckdictionary = truckresponse.json()

#filetring the summary (what we need)
carfiltered = cardictionary['features'][0]['properties']['summary']
walkfiltered = walkdictionary['features'][0]['properties']['summary']
cyclefiltered = cycledictionary['features'][0]['properties']['summary']
truckfiltered = truckdictionary['features'][0]['properties']['summary']

#setting up the array where information will go
dataarray = [
    ["car", 0, 0],
    ["walking", 0, 0],
    ["cycling", 0, 0],
    ["truck", 0, 0]
]
#format for storing data: method, distance, duration

#inputting requried data into the correct position in array
dataarray[0][1] = carfiltered['distance']
dataarray[0][2] = carfiltered['duration']
dataarray[1][1] = walkfiltered['distance']
dataarray[1][2] = walkfiltered['duration']
dataarray[2][1] = cyclefiltered['distance']
dataarray[2][2] = cyclefiltered['duration']
dataarray[3][1] = truckfiltered['distance']
dataarray[3][2] = truckfiltered['duration']

print(dataarray)

#creating functions for bubble sort
def bubblesortasc(position):
    for i in range(4):
        for j in range(3):
            if dataarray[j][position] > dataarray[j + 1][position]:
                temp = dataarray[j]
                dataarray[j] = dataarray[j + 1]
                dataarray[j + 1] = temp
    print(dataarray)

def bubblesortdesc(position):
    for i in range(4):
        for j in range(3):
            if dataarray[j][position] < dataarray[j + 1][position]:
                temp = dataarray[j]
                dataarray[j] = dataarray[j + 1]
                dataarray[j + 1] = temp
    print(dataarray)

while True:
    userinput = input("Enter 'A' for shortest path \n Enter 'B' for longest path \n Enter 'C' for shortest duration \n Enter 'D' for longest duration \n Enter 'E' to exit: ")

    if userinput.upper() == 'A':
        bubblesortasc(1)
    elif userinput.upper() == 'B':
        bubblesortdesc(1)
    elif userinput.upper() == 'C':
        bubblesortasc(1)
    elif userinput.upper() == 'D':
        bubblesortdesc(2)
    elif userinput.upper() == 'E':
        print("This is the end.")
        break
    else:
        print("Invaild input.")