"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...


Jill={
    'age' : 26,
    'job': 'biologist',
    'relastions' : {'Friend':'Zalika', 'Partner' : 'John'}
}

Zalika={
    'age' : 28,
    'job': 'Artist',
    'relastions' : {'Friend':'Jill'}
}

John={
    'age' : 27,
    'job': 'Writter',
    'relastions' : {'Partner':'Jill'}
}

Nash={
    'age' : 34,
    'job': 'chef',
    'relastions' : {'Cousin':'John', 'Landlord':'Zalika'}
}

my_group =[Jill, Zalika, John, Nash];

print(my_group[0]['relastions']['Friend'])