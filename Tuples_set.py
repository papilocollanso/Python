# A Tuples is a collection which is ordered and unchangeable. Allowes duplicate numbers
#create a turple

fruits =('apples',)
fruits = ('apples', 'oranges', "grapes")
fruits2 = tuple(('apples','oranges','grapes'))
#print(fruits[1])
#print(type(fruits))

# delete tuple

#print(len(fruits2))

# A set is collection which is unordered and unindexed. no duplicate numbers

#create a set

fruits_set = {'Apples','oranges',"Mango"}

#check if in set

#print('Apples' in fruits_set)
#add to set
fruits_set.add('grapes')
#print(fruits_set)
#remove set
fruits_set.remove('grapes')

#clear set
fruits_set.clear()
del fruits_set
print(fruits_set)
