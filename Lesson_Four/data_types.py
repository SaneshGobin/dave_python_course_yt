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


# escaping special characters
sentence = 'I\'m not amused.\tHey\n\nWhere\'s this @\\located\n'
print(sentence)


# String methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace('good', 'ok'))
print(multiline)

print(len(multiline))
multiline += "                      "
multiline = "                    " + multiline
print(multiline)
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# blank space from readability
print()
print()
print()
print()
print()
print()
print()


# Build a menu
title = 'menu'.upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "R20".rjust(4))
print("Tea".ljust(16, ".") + "R15".rjust(4))
print("Muffin".ljust(16, ".") + "R16".rjust(4))
print("Cheesecake".ljust(16, ".") + "R25".rjust(4))

print("")

# string index value
print(first[1])
print(first[-1])  # reference the last value
print(first[1:-1])
print(first[1:])

# some methods return boolean data
print(first.startswith("S"))
print(first.endswith("s"))


# boolean data type
myvalue = True
x = bool(False)

print(myvalue)
print(type(x))
print(isinstance(myvalue, bool))
