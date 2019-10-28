import yaml
import json

# Code start here (All examples are related to YAML)

# Format
# Note that YAML takes the value in string format and represents the output. E.g.
yaml_data = yaml.load("Quick brown fox jumped over the lazy dog.", Loader=yaml.FullLoader)
print ("...01..OUTPUT - (Format):", yaml_data)

# Block format
yaml_data = '''
--- # Favorite movies
 - Casablanca
 - North by Northwest
 - The Man Who Wasn't There
'''
yaml.load(yaml_data, Loader=yaml.FullLoader)
print ("...02..OUTPUT - (Block Format):", yaml_data)

# Inline format
# Inline format is delimited with comma and space and the items are enclosed in JSON.
yaml_data = '''
--- # Shopping list
   [milk, groceries, eggs, juice, fruits]
'''
yaml.load(yaml_data, Loader=yaml.FullLoader)
print ("...03..OUTPUT - (Inline Format):", yaml_data)

# Folded Text
# Folded text converts newlines to spaces and removes the leading whitespace.
yaml_data = '''
- {name: John Smith, age: 33}
- name: Mary Smith
  age: 27
'''
yaml.load(yaml_data, Loader=yaml.FullLoader)
print ("...04..OUTPUT - (Folded text):", yaml_data)

# Indentation of YAML
print ("...05..OUTPUT - (Indentations of Yaml, Keep 2 space for each level.):")

# Separation of Strings
# Strings are separated using double-quoted string. If you escape the
# newline characters in a given string, it is completely removed and
# translated into space value.
yaml_data = '''
errors:
      messages:
         already_confirmed: "was already confirmed, please try signing in"
         confirmation_period_expired: "needs to be confirmed within %{period}, please request a new one"
         expired: "has expired, please request a new one"
         not_found: "not found"
         not_locked: "was not locked"
         not_saved:
            one: "1 error prohibited this %{resource} from being saved:"
            other: "%{count} errors prohibited this %{resource} from being saved:"
'''
yaml.load(yaml_data, Loader=yaml.FullLoader)
print ("...06..OUTPUT - (Separation string):", yaml_data)

# YAML comments
yaml_data = '''
YAML supports single line comments.
YAML does not support multi line comments.
If you want to provide comments for multiple lines, you can do so as shown in the example below
# this
# is a multiple
# line comment
'''
print ("...07..OUTPUT - (YAML Comments):", yaml_data)






'''
Yaml load file example, (convert yaml to json):
    Declare Yaml file name, open it and use yaml load function to convert in dict object.
    Note: During load you must need to add Loader, else it will give warring message.
    With PyYaml 5.1, The current Loader choices are:
        - BaseLoader, SafeLoader, FullLoader
'''
'''
yaml_filename = "yaml_general_example.yaml"
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