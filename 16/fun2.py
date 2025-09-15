#Join Names
def lastFirst(firstName, lastName):
    separator = ', '
    result = lastName + separator + firstName
    return result

print(lastFirst('John', 'Doe'))
print(lastFirst('Andrew', 'Harrington'))