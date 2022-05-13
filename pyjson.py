#JSON is commonly used with data APIS.Here how we can parse into a
#python dictionary

import json

#Sample JSON
userJSON = '{"first_name":"John", "last_name":"Doe", "age":30}'

#Parse to dict

user =json.loads(userJSON)
 #json to regular dictionary 
 #note dictionary looks like an object
print(user['first_name'])
#print(user)

car = {
    'make':'ford',
    'model': 'mustang',
    'year': 1970
}
#dictionary has single quote
#json has
# dictionary to regular json
carJSON = json.dumps(car)
print(carJSON)