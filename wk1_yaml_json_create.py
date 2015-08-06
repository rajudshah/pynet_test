#!/usr/bin/env python

import yaml
import json
from pprint import pprint as pp

list_1 = range(5)
list_1.append('Create a list')
list_1.append('with a dictionary with 2 keys')
list_1.append({})
list_1[-1]['json_file'] = 'wk1_list.json'
list_1[-1]['yaml_file'] = 'wk1_list.yml'

# Write list to file in YAML format
with open ("wk1_list.yml", "w") as f:
    f.write(yaml.dump(list_1, default_flow_style=False))
f.close()

# Write list to flle in JSON format
with open ("wk1_list.json", "w") as f:
    json.dump(list_1, f)
f.close()

# Read YAML file and pretty print it
with open("wk1_list.yml") as f:
    list_yaml = yaml.load(f)
print "\nYAML List\n"
pp(list_yaml)
f.close()

# Read JSON file and pretty print it
with open("wk1_list.json") as f:
    list_json = json.load(f)
print "\n\nJSON List\n"
pp(list_json)
f.close()



