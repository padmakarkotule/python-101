import yaml
import json

# Code start here

'''
Declare Yaml file name, open it and use yaml load function to convert in dict object.
Note: During load you must need to add Loader, else it will give warring message.
With PyYaml 5.1, The current Loader choices are:
    - BaseLoader, SafeLoader, FullLoader
'''

yaml_filename = "01_yml_general_example.yaml"
with open(yaml_filename) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

print("... Type of yaml file name is:", type(yaml_filename))
print("... Type of data object is:", type(data))
print("... Output after yaml.load func, (YAML_to_JSON), converted.:\n", data)
print("\n")

# Convert dict (data loaded from Yaml) object into json
json_output = json.dumps(data, indent=4, separators=(',', ': '))
print("... Output after json.dumps:\n", json_output)

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