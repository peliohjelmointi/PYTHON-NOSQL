import json

lause = "D'Oh!"
lause = "D \"Oh"
lause = 'D"Oh!'

# LOADS
json_string = '{"hasChildren":false,"employees":null}'

# parse json to python object
d = json.loads(json_string)

print(d)    #   false>False, null>None
print(type(d)) # dict

# LOAD
with open('chrisu.json','r') as file:
    chrisu_as_python = json.load(file)

print(type(chrisu_as_python)) # dict
print(chrisu_as_python)