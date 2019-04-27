# Distance Data Organizing Explained
1. use [Request_From_UREG.py](https://github.com/awesome-schedule/data/blob/master/Distance/Request_From_UREG.py) to scrape data from official building list on [UREG](http://www.virginia.edu/registrar/buildings.html)
..* The program scrapes and saves the data to [Building_Names.json](https://github.com/awesome-schedule/data/blob/master/Distance/Building_Names.json)
2. use [GoogleMapRequests.py](https://github.com/awesome-schedule/data/blob/master/Distance/GoogleMapRequests.py) to create the following data files: 
..*[Building_Array.json](https://github.com/awesome-schedule/data/blob/master/Distance/Building_Array.json)
..*[Building_MetaData.json](https://github.com/awesome-schedule/data/blob/master/Distance/Building_MetaData.json)
..*[Time_Matrix.json](https://github.com/awesome-schedule/data/blob/master/Distance/Time_Matrix.json)
..*[Distance_MetaData.json](https://github.com/awesome-schedule/data/blob/master/Distance/Distance_MetaData.json)


a.  load_data:
from Building_Names to get Building_Meta_Data
b. create_distance_matrix:
from Building_Meta_data 
get building_name, origin, destination

-> get distance metadata


now fix load