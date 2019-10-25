import yaml

#my_dict = yaml.load(open('swagger_yaml.example.yml'))
with open('swagger_yaml.example.yml') as file:
    my_dict = yaml.load(file, Loader=yaml.FullLoader)
#my_dict = yaml.load(open('swagger_yaml.example.yml'))
print("..Data..:", my_dict.keys())
print("..Data..:", my_dict.get('components').keys())
print("..Data.Info.:", my_dict['info'].get('title'))
print("..Data.Path-Parameters.:", my_dict['paths'].get('/weather').get('get').get('parameters'))

paramaters_wether = my_dict['paths']['/weather']['get']['parameters']
print("..Data.Path-Parameters.:\n", paramaters_wether[2])

for token in paramaters_wether:
    print("....paramaters in wether .:\n", token)

#print("..Info Keys..:", my_dict.get('info').keys())
Info_Keys = my_dict.get('info').keys()
print("----INFO_KEYS:",Info_Keys)
info = my_dict.get('info')
print("...Info..", info['version'])
print("...Info..", info['title'])
print("...Info..", info['license'])
print("...Info..", info['license']['name'])
print("...Info..", info['license']['url'])
#print("...Info..", info['description'])
#for (k, v) in my_dict.items():
#   print("Key:" + k)
#   print("Value: " + str(v))