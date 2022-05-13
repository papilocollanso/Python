
x =100;
y=1000



#camparison operators(==, !=,>, <, >=, <=)-used to compare value
"""if x >y:
    print(f'{x} is greater than {y}')
else:
    print('not true')
   
if x > y:
    print(f'{x} is greater than {y}')
elif x==y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater {y}')


#nested if 
if x>2:
    if x<100:
      print(f'{x} is greater than 2 and less than or equal to 10')

"""

#logical operators (and ,or , not) -Used to combine conditional statements


#membership operators (not, not in) - membership operators are used to test if a sequence is
#presented in an object

"""if x>2 and x<= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')
    
if x>2 or x<= 10:
     print(f'{x} is greater than 2 and less than or equal to 10')
     
if not(x==y):
        print(f'{x} is not equal to {y}')
        """
numbers = [1,2,3,4,5]

#in
"""if x in numbers:
    print(x in numbers)
    
    #not in
if y  not in numbers:
    print(y in numbers)"""
    
# identity operators(is , is not)-compare the objects, not if they are equal
#but if they are acutally the same object, with the same
#memory location

# is
if x is y:
    print(x is y)
    
# is not
if x is not y:
    print(x is y)