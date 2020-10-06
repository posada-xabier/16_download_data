import json


# next you get   "a giant no indented python dico"   from the raw data json
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

# next you get the number of terremotos
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# next extracting magnitudes for Earth Q.
mags = []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']
	mags.append(mag)
print(mags[:10])

# next in same folder your code creates a data python file more readable because of indentation
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
	json.dump(all_eq_data, f, indent=4)
