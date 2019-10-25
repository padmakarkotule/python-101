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

# Yaml dump file example. (convert JSON to YAML)
# take any json data. E.g.
data = {
    "defaults": {
        "adapter": "postgres",
        "host": "localhost"
    },
    "development": {
        "adapter": "postgres",
        "host": "localhost",
        "datanase": "myapp_development"
    },
    "test": {
        "adapter": "postgres",
        "host": "localhost",
        "database": "myapp_test"
    }
}

json_data = json.dumps(data, indent=4)
yml_data_output1 = yaml.dump(data, default_flow_style=True)
print("... Output after yaml.dumps).:\n", yml_data_output1)

yml_data_output2 = yaml.dump(data, default_flow_style=False)
print("... Output after yaml.dumps (default_flow_stype=Failse).:\n", yml_data_output2)

# Dump data from json to yaml in file - (JSON to YAML dump example).
yaml_output_file1 = "output_03_json_to_yaml_dump_in_file1.yaml"
with open(yaml_output_file1, 'w') as yaml_file1:  # writing YAML object
    yaml.dump(data, yaml_file1, default_flow_style=True)

yaml_output_file2 = "output_03_json_to_yaml_dump_in_file2.yaml"
with open(yaml_output_file2, 'w') as yaml_file2:  # writing YAML object
    yaml.dump(data, yaml_file2, default_flow_style=False)
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