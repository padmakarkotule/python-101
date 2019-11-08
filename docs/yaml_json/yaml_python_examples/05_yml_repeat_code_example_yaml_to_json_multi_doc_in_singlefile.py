import yaml
import json

# Code start here
# Use load_all to get multi document of yaml file.
yaml_filename = "yaml_multi_doc_in_singlefile.yaml"
with open(yaml_filename) as file:
    data = list(yaml.load_all(file, Loader=yaml.FullLoader))
print("... Type of yaml file name is:", type(yaml_filename))
print("... Type of data object is:", type(data))
print("... Output after yaml.load func, (YAML_to_JSON),1st doc.:\n", data[0])
print("... Output after yaml.load func, (YAML_to_JSON),2nd doc.:\n", data[1])
print("\n")

json_output = json.dumps(data[0], indent=4, separators=(',', ': '))
print("... Output after json.dumps), for combined docs:\n", json_output)
