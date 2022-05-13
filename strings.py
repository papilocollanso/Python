name ='Prosper'
age = '37'
#concatenate
print('Hello, my name is ' + name +' and i am ' + str(age))

#string formating


#arguments by position
print('my name is {name} and i am {age}'.format(name=name,age=age))
#F-strings
print(f'heloo i am {name} and {age} years old ')
s= 'helloworld'
#capitalize strings
"""print(s.capitalize())
print(s.upper())
print(s.lower())"""
print(s.swapcase())
print(len(s))
print(s.replace('world','everyone'))

#count
sub='h'
print(s.count(sub))
print(s.startswith('hello'))
print(s.endswith("d"))
#split into a list
print(s.split())
print(s.find('r'))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())

