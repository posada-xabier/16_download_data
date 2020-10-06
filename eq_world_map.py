import json

# We import the Scattergeo chart type and the Layout class, 
# and then import the offline module to render the map
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []


for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# MAP THE EARTHQUAKES.
# we define a list called data. We create the Scattergeo object inside this list.
# modo 1     data = [Scattergeo(lon=lons, lat=lats)]  next you see alternative to mode 1
data = [{
	'type':'scattergeo',
	'lon': lons,
	'lat': lats,
	'text': hover_texts,
	'marker':{
		'size': [5*mag for mag in mags],
		'color':mags,
		'colorscale':'Viridis',
		'reversescale':True,
		'colorbar':{'title':'Magnitude'},
	}
}]

# You can plot more than one data set in any visualization, 
# but the Scattergeo chart type allows you to overlay a scatter plot of geographic data on a map
# the simplest just list latit + list longit.
# We give the chart an appropriate title
my_layout = Layout(title='Global Earthquakes')
# and create a dictionary
# called '"fig"' that contains the data and the layout
fig = {'data':data, 'layout':my_layout}

#Finally, we pass fig
# to the plot() function along with a descriptive filename for the output
offline.plot(fig, filename='global_earthquakes.html')
















