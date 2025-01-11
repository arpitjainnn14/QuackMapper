import requests
import pandas as pd

URL='https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'

response=requests.get(URL)

data=response.json()


complete_data=data['features']
data_list=[]
for cd in complete_data:
    properties=cd['properties']
    magnitude=properties['mag']
    place=properties['place']
    geometry=cd['geometry']
    longitude=geometry['coordinates'][0]
    latitude=geometry['coordinates'][1]
    data_list.append([magnitude,place,longitude,latitude])
    

df=pd.DataFrame(data_list,columns=['Magnitude','Place','Longitude','Latitude'])

df_sorted=df.sort_values(by='Magnitude',ascending=False)

print(df_sorted['Place'][:10])