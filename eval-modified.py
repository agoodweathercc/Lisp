from convert import *
galist = {}; gdlist = {}
def getval(func,dlist):
    global gdlist
    return gdlist[func]
def Atom(exp):
    # if (isinstance(exp,list)==True):
    #     if (len(exp) == 1 and isinstance(exp[0], list) == False):
    #         return 'T'

    if isinstance(exp,int):
        return 'T'
    elif (exp == 'CONS' or exp == 'CDR' or exp == 'NULL' or exp == 'EQ'or exp == 'COND'):
        return 'T'
    # elif exp in galist:
    #     return 'NIL'
    #     Atom(galist[exp])
    elif (isinstance(exp, str)==True):
        # if exp in galist:
        #     return Atom(galist[exp])
            # return 'NIL'
        return 'T'
    else:
        return 'NIL'
# test case
Atom('a')
# Atom(['a'])

def car(exp):
    if (isinstance(exp,str)== True or isinstance(exp,int)==True):
        try:
            1/0
            print('try this')
            return galist[exp]
        except:
            return exp
    else:
        assert len(exp)==5
        return exp[1]
def cdr(exp):
    if (isinstance(exp, str) or isinstance(exp,int)):
        try:
            1/0
            print('try this')
            return galist[exp]
        except:
            return exp
    else:
        assert (len(exp)==5)
        return exp[3]

def cons(exp1, exp2):
    if (exp2 == 'NIL' or exp2 == None):
        # assert isinstance(exp1,list)
        # assert len(exp1)==5
        return ['(', exp1, '.', 'NIL', ')'] # not sure here, try return exp1 only later
        # return exp1
    else:
        return ['(', exp1,'.', exp2,')']
    # return car(cdr())
def null(exp):
    if (exp=='NIL'):
        return 'T'
    else:
        return 'NIL'
def evlis(lis, alist, dlist):
    global galist, gdlist
    if null(lis)=='T':
        return 'NIL'
        # print('there is nothing to evalulate')
        pass
        # return 'NIL' # not sure here
    elif (isinstance(lis,str)==True or isinstance(lis, int)==True):
        try:
            1/0
            print('try this')
            return galist[lis]
        except:
            return lis
    else:
        # print('using evlis')
        l1 = evaluate(car(lis), galist, gdlist)
        l2 = evlis(cdr(lis), galist, gdlist)
        # assert len(cons(l1,l2))==5
        return cons(l1, l2)
        # for i in lis:
            # evaluate(i,alist,dlist)
def lispapply(f,x, alist, dlist):
    # assert type(x)==list
    if Atom(f)=='T':
        if f=='CAR':
            assert len(x)==5
            return car(car(x))
        elif f=='CDR':
            return cdr(car(x))
        elif f == 'CONS':
            return ['(', car(x),'.', car(cdr(x)),')']
        elif f=='NULL':
            return null(car(x))
        elif f == 'EQ':
            if car(x)==car(cdr(x)):
                return "T"
            else:
                return 'NIL'
        elif f == 'PLUS':
            return car(x) + car(cdr(x))
        elif f == 'MINUS':
            return car(x) - car(cdr(x))
        elif f == 'TIMES':
            return car(x) * car(cdr(x))
        elif f == 'QUOTIENT':
            return car(x) / car(cdr(x))
        elif f == 'REMAINDER':
            return car(x) % car(cdr(x))
        elif f == 'LESS':
            if car(x) < car(cdr(x)):
                return 'T'
            else:
                return 'NIL'
        elif f == 'GREATER':
            if car(x) > car(cdr(x)):
                return 'T'
            else:
                return 'NIL'

        elif f == 'ATOM':
            if Atom(car(x))=='T':
                return 'T'
            else:
                return 'NIL'
        elif f == 'INT':
            if Atom(car(x))=='T':
                try:
                    int(car(x))
                    return 'T'
                except:
                    return 'NIL'
            else:
                return 'NIL'
        else:
            arg1 = cdr(getval(f, gdlist))
            arg2 = addpairs(car(getval(f, gdlist)), x, {})
            arg3 = {} # gdlist
            return evaluate(arg1, arg2, arg3)
    else:
        print('there is error!')
# test lispapply
f = 'CONS'
x = convert(parse('(3 4)'))
pretty_print(lispapply(f,x,{},{}))
expr = ['(2 3)']
for i in range(len(expr)):
    alist = {'w': 1, 'y': 2}
    dlist = {}
    x = convert(parse(expr[i]))
    f = 'CONS'
    lispapply(f, x, alist, dlist)
test = convert(parse('(2 3)'))
lispapply('CDR', convert(parse('((x y z))')), alist,{})
def evcon(exp, alist, dlist):
    global galist,gdlist
    if null(exp)=='T':
        print('error when evaluating evcon')
        return 'NIL' # not sure here
    elif evaluate(car(car(exp)), {},{})=='T':
        e = car(cdr(car(exp)))
        # return evaluate(e, galist,gdlist)
        return evaluate(e, {}, {})
    elif evaluate(car(car(exp)), {},{})=='NIL':
        return evcon(cdr(exp), {},{})

def evaluate(exp, alist, dlist):
    global galist
    global gdlist
    """
    :param exp: a list of characters
    :param alist: a dictionary
    :param dlist: a dictionary
    :return:
    """
    if Atom(exp)=='T':
        pass
        # try:
        #     isinstance(exp,list)
        #     check = 1 # it is int
        # except (TypeError,ValueError):
        #     check = 23 # not a int
        try:
            isinstance(int(exp), int)
            if isinstance(int(exp), int):
                return int(exp)
        except:
            if (exp == 'T'):
                return 'T'
            elif (exp == 'NIL'):
                return 'NIL'
            elif (exp in galist):
                return galist.get(exp) # very important!
            else:
                return 'unbound variable'
    else:

        if car(exp)=='QUOTE':
            # pretty_print(car(cdr(exp)))
            return car(cdr(exp))
        elif car(exp)=='COND':
            # return evcon(cdr(exp), galist, gdlist)
            return evcon(cdr(exp), galist, gdlist)
        elif car(exp)=='DEFUN':
            func_name = car(cdr(exp))
            # gdlist[func_name]=cdr(cdr(exp)) # very important!
            plist = car(cdr(cdr(exp)))
            fb = car(cdr(cdr(cdr(exp))))
            gdlist[func_name] = ['(', plist, '.', fb, ')']
            return func_name
            # print(func_name)
            # return pretty_print(cdr(cdr(exp)))

        else:
            f = car(exp) # exp[1] # same as car(exp), sketchy here
            x = evlis(cdr(exp), {}, {})
            if x == None:
                return f
            else:
                _galist = galist
                _gdlist = gdlist
                lispapply(f, x, {}, {})
                # print(lispapply(f, x, _galist, _gdlist))
                return lispapply(f, x, {}, {})
            # else:
        #     print('some error occured!')

sexp = convert(parse('((b1 e1) (b2 e2) (b3 e3))'))
galist = {'b1':'NIL','b2':'T','b3':'NIL'}
gdlist = {'e1':8,'e2':4,'e3':2}
# evcon(sexp, {}, {})

def addpairs(plist, x, alist):
    # global galist
    if plist=='NIL' or plist ==['NIL']:
        alist['NIL']='NIL'
        return alist
    else:
        assert len(plist)==5
        assert len(x) == 5
        alist[car(plist)] = car(x)
        addpairs(cdr(plist), cdr(x), alist)
        return alist

plis = convert(parse('(p1 p2 p3)'))
xlis = convert(parse('(x1 x2 x3)'))
alis = {}
addpairs(plis, xlis, alis)




test = convert(parse('(F.(plist. fb))'))
alist={'w':1,'y':2}
gdlist={}
f ='cons'

alist = {'x':1, 'y':2, 'z':3}
test = [convert(parse('(quote (a . b))')), convert(parse('(cons 3 4)')), convert(parse('(cons 4 (quote (a . b)))'))]
functiontest = [convert(parse('(DEFUN SILLY (A B) (PLUS A B))')), convert(parse('(SILLY 5 6)')), convert(parse('(PLUS 5 6)')),
                convert(parse('(CAR (QUOTE (4 . b)))'))]

test_str = ['(5)', '(QUOTE (a . b))', '(CONS 3 4)', '(CONS 4 (QUOTE (a . b)))', '(DEFUN SILLY (A B) (PLUS A B))',
            '(SILLY 5 6)', '(PLUS 5 6)', '(CAR (QUOTE (4 . b)))', '(CDR (QUOTE (4 . b)))',  '(SILLY (CAR (QUOTE (5 . 6))) (CDR (QUOTE (5 . 6))) )']
test_str = ['(DEFUN COUNT (X) (COND((ATOM X) 1)(T (PLUS (COUNT (CAR X)) (COUNT (CDR X))))))',
            '(COUNT (QUOTE (1 2)))']
# test_str = ['(-1)']
length = len(test_str)
for i in range(length):
# for i in [8]:
    dotstr = convert(parse(test_str[i]))
    print ('the string %s is the following'%i)
    pretty_print(dotstr)
    result = evaluate(dotstr, galist, gdlist)
    pretty_print(evaluate(dotstr, galist, gdlist))
    print(result);print('\n')
    # pretty_print(result)

def read_test(path):
    with open(path) as f:
        mylist = f.read()
    mylist = mylist.replace('\n','')
    mylist = mylist.split('$')
    del mylist[-1]; del mylist[-1]
    return mylist
print('here')
if __name__ == '__main__':
    test = read_test('./project2-test-case/null.txt')
    for i in test:
        # print(i)
        dotstr = convert(parse(i))
        pretty_print(dotstr)
        # print('finish pretty print')
        evaluate(dotstr, galist, gdlist)
        result = evaluate(dotstr,galist,gdlist)
        print(result)
        pretty_print(result)
        print('\n')
