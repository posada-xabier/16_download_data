import json

filename = 'data/eq_data_1_day_m1.json'

with open(filename) as f:
	all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))



readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
	json.dump(all_eq_data, f, indent=4)
