# A list is a collection which is ordered and changeable. Allows duplicate members
# Creat list
numbers = [1,23,4,5]
numbers1 = list((1,2,3,4))
fruits = ['mangoes','apple','pawpaw','coconut']
#print(numbers1)
#print(fruits[3])
fruits.append('Mango')
fruits.remove("coconut")
#print(fruits)

#insert into position
fruits.insert(2,'bobo')

#remove with pop
print(fruits.pop(1))
#print(fruits.reverse())
fruits.sort()
fruits.sort(reverse=True)
fruits[0] ='milk'
print(fruits)

