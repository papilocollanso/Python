#a function is a block of code which only runs when it is called. In python, we do not use 
#curly brackets, we use indentation with tabs or spaces

# a lamba function is a small function anonymous function

# a lamba function can take any number of arguments but can only
#have one expression very simila to javascript to js arrow function

#create function

def sayHello(name='sam'):
    print(f'{name}');
    
def getSum(num1,num2):
    total =num1 + num2;
    return total;
num = getSum(2,3);
#print(num);


getSum = lambda num1, num2: num1 +num2

print(getSum(10,3))