# a dictionary is a colelction which is unoredered , changeable and indexed, no duplicate

person ={
    'first_name': 'john',
    'last_name':'Doe',
    'age': 30
    
}
person2 = dict(first_name='Sara', last_name='collins') # squares[:] copy an array
#mathc status

"""
try:
except(TypeError, NameError,ValueError,RuntimeError):
or except ZeroDivisionError as err:
"""
#print(person['first_name'])
#print(person.get('last_name'))

#add key value
person['person'] ='0909999'
#print(person.items());

person2 = person.copy()
person2['city']='boston'
#print(person2);
#del (person['age']);
person.pop('age');

#clear
#pass jus go to the next code dont do anything
#finally

person.clear()
#print(person);
#get length
#print(len(person2));

people =[
    {'name':'martha', 'age':30},
    {'name':'kelvin', 'age':25}
    
]
print(people[0]['name'])