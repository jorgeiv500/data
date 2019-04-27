# Distance Data Usage of Python File Explained
1. use [Request_From_UREG.py](https://github.com/awesome-schedule/data/blob/master/Distance/Request_From_UREG.py) to scrape data from official building list on [UREG](http://www.virginia.edu/registrar/buildings.html)
* The program scrapes and saves the data to [Building_Names.json](https://github.com/awesome-schedule/data/blob/master/Distance/Building_Names.json)
2. use [GoogleMapRequests.py](https://github.com/awesome-schedule/data/blob/master/Distance/GoogleMapRequests.py) to create the following data files: 
* [Building_Array.json](https://github.com/awesome-schedule/data/blob/master/Distance/Building_Array.json): the 1d array serving as a dictionary which uses index as key and the building names as value
*[Building_MetaData.json](https://github.com/awesome-schedule/data/blob/master/Distance/Building_MetaData.json): Meta Data related to Google Geocoding API
* [Time_Matrix.json](https://github.com/awesome-schedule/data/blob/master/Distance/Time_Matrix.json):the 2d array serving as a dictionary which contains the time it takes to walk from one building to another. Use Building_Array to look up the name of the building in each index
* [Distance_MetaData.json](https://github.com/awesome-schedule/data/blob/master/Distance/Distance_MetaData.json):Meta Data related to Google Distance Matrix API

# Functions in GoogleMapRequests.py Explained
1.  load_data:
from Building_Names to get Building_Meta_Data
2. create_distance_matrix:
from Building_Meta_data 
get building_name, origin, destination
