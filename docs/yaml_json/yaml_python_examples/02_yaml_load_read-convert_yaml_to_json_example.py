import yaml
import json

# Code start here
'''
Serializing and Deserializing with dumps() and loads()
The dumps() function works exactly like dump() 
but instead of sending the output to a file-like object, it returns the
output as a string. Similarly, loads() function is as same as load() 
but instead of deserializing the JSON string from a file, it deserializes from a string.
'''

# Yaml load file
yaml_filename = "yaml_single_doc.yaml"
with open(yaml_filename) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

print("... Type of yaml file name is:", type(yaml_filename))
print("... Type of data object is:", type(data))
print("... Output after yaml.load func, (YAML_to_JSON), converted.:\n", data)
print("\n")

# Convert dict (data loaded from Yaml) object into json object
# ** IMP - data is alreadt dict obj. so no need to again json dumps
#json_output = json.dumps(data, indent=4, separators=(',', ': '))
#print("... Output after json.dumps:\n", json_output)

# Dump data into json file after converting YAML to JSON
with open('output_02_yaml_dump_to_json_in_file.json', 'w') as jsonfile:  # writing JSON object
    json.dump(data, jsonfile, indent=4)

'''
yml_data_output1 = yaml.dump(data, default_flow_style=True)
print("... Output after yaml.dumps).:\n", yml_data_output1)

yml_data_output2 = yaml.dump(data, default_flow_style=False)
print("... Output after yaml.dumps).:\n", yml_data_output2)

YAML :Data serialization language, designed to be human friendly and works 
      perfectly with other programming languages.
      Note that YAML takes the value in string format and represents the output.
      Example,      
'''
host = data['test']['host']
print("----HOST:", host)