from pathlib import Path
import json

# read data as a string and convert to a python object
path = Path('eq_data/eq_data_1_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# create a more readable version of the data file
path = Path('eq_data/eq_data_1_m1.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)