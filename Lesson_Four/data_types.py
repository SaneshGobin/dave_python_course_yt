# String data type

# Literal assignment
first = 'Sanesh'
last = 'Gobin'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Contructor function
# pizza = str('peperoni')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
full_name = first + " " + last
print(full_name)

full_name += "!"
print(full_name)

# casting a number to a string
decade = str(1980)
print(type(decade))

statement = 'I like music from the ' + decade + "'s"
print(statement)

# multiple lines
multiline = '''
Hey how are you           

I was just checking .
                            All good?

'''

print(multiline)
