import json


# next you get   "a giant no indented python dico"   from the raw data json
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

# next you get the number of terremotos
# result >> 158
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# next extracting magnitudes for Earth Q.
# result >> [0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	lon = eq_dict['geometry']['coordinates'][0]
	lat = eq_dict['geometry']['coordinates'][1]
	mags.append(mag)
	lons.append(lon)
	lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])

# next in same folder your code creates a data python file more readable because of indentation
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
	json.dump(all_eq_data, f, indent=4)
