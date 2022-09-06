from xlformat_func import *

perm_matcher = re.compile(r'Read-(only)?(write)?\. ')

def getperm(x):
    target = x[2]
    perms = ['' if (r := perm_matcher.search(s)) is None else r.group() for s in target]
    others = [(s := target[i]).replace((sp := perms[i]), '') for i in range(len(target))]
    return (perms, others)

def main():
    wb = openpyxl.load_workbook(sys.argv[1])
    ws = wb.active
    x = extract(ws, 1)
    perms, others = getperm(x)
    x = [x[0], x[1], perms, others]
    wsr = wb.create_sheet('sheet')
    wsr.title = 'parsed'
    dump2ws(wsr, x)
    wb.save(sys.argv[1])



if __name__ == '__main__':
    main()