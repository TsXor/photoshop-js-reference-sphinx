import sys

name = sys.argv[1]
name_header = ('%s\n%s\n%s\n\n\n\n'%('='*len(name), name, '='*len(name)))

property_header = '''
----------
Properties
----------



'''[1:]

method_header = '''
-------
Methods
-------



'''[1:]

print(name_header+property_header+method_header)