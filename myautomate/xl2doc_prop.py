import openpyxl, sys
from xl2doc_func import *

template = '''
.. property:: <PROP>
	
	<DESC>
	
	:Permission: <PERM>
	
	:Type: :class:`<TYPE>`
'''

def insert_temp(prop, desc, perm, ptype):
    t = template
    t = t.replace('<PROP>', prop)
    t = t.replace('<DESC>', desc)
    t = t.replace('<PERM>', perm)
    t = t.replace('<TYPE>', ptype)
    return t

def main():
    wb = openpyxl.load_workbook(sys.argv[1])
    ws = wb['parsed']
    dlist = loadws(ws)
    for l in dlist:
        l = [l[1-1], l[4-1], l[3-1], l[2-1]]
        doc = insert_temp(*l)
        print(doc)



if __name__ == '__main__':
    main()