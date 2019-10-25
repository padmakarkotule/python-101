import yaml
import json

# Code start here

yaml_filename = "yaml_single_doc.yaml"
with open(yaml_filename) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

print("... Type of yaml file name is:", type(yaml_filename))
print("... Type of data object is:", type(data))
print("... Output after yaml.load func, (YAML_to_JSON), converted.:\n", data)
print("\n")

# Convert dict (data loaded from Yaml) object into json
json_output = json.dumps(data, indent=4, separators=(',', ': '))
print("... Output after json.dumps:\n", json_output)
