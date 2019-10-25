import yaml
import objectpath

data = {
    'name': "Padmakar",
    'age': 48,
    'handles': {
        'Facebook': 'padmakarkotule',
        'github': 'pkotule',
        'youtube': 'indianpython'
    },
    'languages': {
        'markup': ['html', 'XML', 'Markdown'],
        'programming': ['C', 'Python', 'Golang', 'Js']
    }
}
print("..[01]....\nPrint source Data :\n", data)

yml_data_output = yaml.dump(data, default_flow_style=True)
print("..[02]....\nPrint yaml Data (Default_flow_style=True):\n", yml_data_output)

yml_data_output = yaml.dump(data, default_flow_style=False)
print("..[03]....\nPrint source Data (Default_flow_style=False):\n", yml_data_output)

yaml_string = '''
paths:
  /users:
    get:
      tags:
        - Users data
      summary: "Get the users data"
      description: "Will be return all users data"
      operationId: "UsersData"
      parameters:
      - name: "id"
        in: "query"
        description: "**City name**. *Example: London*. You can call by city name, or by city name and country code. The API responds with a list of results that match a searching word. For the query value, type the city name and optionally the country code divided by a comma; use ISO 3166 country codes."
        schema:
          type: "string"

      - name: "zip"
        in: query
        description: "State Zip code"
        schema:
          type: integer

      responses:
        200:
          description: "Successful respones"
          content:
            application/json:
              schema:
                title: Sample
                type: object
                properties:
                  placeholder:
                    type: string
                    description: "Get users data"
        404:
          description: Not found response
          content:
            application/json:
              schema:
                title: Weather not found
                type: string
                example: Not found

  /catalog:
    get:
        tags:
          - Catalog
        summary: "Get the users data"
        description: "Will be return all users data"
        operationId: "CatalogData"
        parameters:
          - name: "id"
            in: "query"
            schema:
              type: string

        responses:
          201:
            description: "Successful respones"
            content:
              application/json:
                schema:
                  title: User creation response
                  type: object
                  properties:
                    placeholder:
                      type: string
                      description: "User created"

'''




yaml_string1 = '''
name: Padmakar
age: 48
handles:
  Facebook: padmakarkotule
  github: pkotule
  youtube: indianpython
languages:
  markup:
  - html
  - XML
  - Markdown
  programming:
  - C
  - Python
  - Golang
  - Js
'''


yaml_to_json_output = yaml.load(yaml_string, Loader=yaml.FullLoader)
print("..[04]....\n Example of yaml load - load data:\n", yaml_to_json_output )
print("..[05]....\n Example of yaml load - load data:\n", yaml_to_json_output['paths']['/users']['get']['tags'] )
print("..1-key:\n",yaml_to_json_output.get('paths').get('/users').get('get').get('tags'))
print("..2-key:\n",yaml_to_json_output.get('paths').get('/users').get('get').get('summary'))
print("..3-key:\n",yaml_to_json_output.get('paths').get('/users').get('get').get('operationId'))
print("..4-key:\n",yaml_to_json_output.get('paths').get('/users').get('get').get('parameters'))
list_params = yaml_to_json_output.get('paths').get('/users').get('get').get('parameters') #

print("..Params..:",list_params[1].get('schema').get('type'))

data = yaml.load(yaml_string, Loader=yaml.FullLoader)
jsonnn_tree = objectpath.Tree(data['paths']['/users']['get'])
print("\n....JsonTree..:\n", jsonnn_tree)
#result_tuple = tuple(jsonnn_tree.execute('$..content'))
result_tuple = tuple(jsonnn_tree.execute('$..name'))
print("\n....Search in JsonTree..:\n", result_tuple)