from convert import *
galist = {}; gdlist = {}
class lisperror(Exception):
    pass
def getval(func,dlist):
    global gdlist
    if isinstance(func, int):
        print('interger cannot be function in lisp')
        raise lisperror
    if func in gdlist:
         return gdlist[func]
    else:
        print('error, function not in Dlist')
        raise lisperror;

def Atom(exp):
    if isinstance(exp,int):
        return 'T'
    elif (exp == 'CONS' or exp == 'CDR' or exp == 'NULL' or exp == 'EQ'or exp == 'COND'):
        return 'T'
    elif (isinstance(exp, str)==True):
        return 'T'
    else:
        return 'NIL'
# test case
Atom('NIL')

def car(exp):
    if (isinstance(exp, str) or isinstance(exp, int)):
        print(('car cannot take atomic variable'))
        raise lisperror
    try:
        assert len(exp) == 5
        return exp[1]
    except (AssertionError):
        print('length is not 5')
        raise  lisperror

def cdr(exp):
    if (isinstance(exp, str) or isinstance(exp,int)):
        print(('cdr cannot take atomic variable'))
        raise lisperror
    else:
        try:
            assert (len(exp)==5)
            return exp[3]
        except (RuntimeError, TypeError):
            print(('len is not 5'))
            raise lisperror


def cons(exp1, exp2):
    # if (exp2 == 'NIL' or exp1 == 'NIL'):
    #     print('the first and second arg of cons can not be just NIL')
    #     raise lisperror
        # return ['(', exp1, '.', 'NIL', ')'] # not sure here, try return exp1 only later
        # return exp1
    if (exp2 == None):
        print('the second argument should not be None')
        raise lisperror
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
    # elif (isinstance(lis,str)==True or isinstance(lis, int)==True):
    #     print('arg of evlis must be a list, not atom')
    #     raise lisperror
    else:
        l1 = evaluate(car(lis), {}, {})
        l2 = evlis(cdr(lis), {}, {})
        return cons(l1, l2)
        # for i in lis:
            # evaluate(i,alist,dlist)
def lispapply(f,x, alist, dlist):
    # assert type(x)==list
    if Atom(f)=='T':
        if f=='CAR':
            assert len(x)==5
            if cdr(x)!='NIL':
                print('car expects only 1 arguments')
                raise lisperror
            return car(car(x))
        elif f=='CDR':
            assert len(x) == 5
            if cdr(x) != 'NIL':
                print('cdr expects only 1 arguments')
                raise lisperror
            return cdr(car(x))
        elif f == 'CONS':
            if cdr(cdr(x))!='NIL':
                print('CONS expects exactly two arguments')
                raise lisperror
            return ['(', car(x),'.', car(cdr(x)),')']
        elif f=='NULL':
            if cdr(x)!='NIL':
                print('NULL expects exactly one argument')
                raise lisperror
            return null(car(x))
        elif f == 'EQ':
            if cdr(cdr(x)) != 'NIL':
                print('CONS expects exactly two arguments')
                raise lisperror
            if (Atom(car(x))=='NIL' or Atom(car(cdr(x))) == 'NIL'):
                print('EQ can only be applied to two atomic arguments')
                raise lisperror
            if car(x)==car(cdr(x)):
                return "T"
            else:
                return 'NIL'
        elif f == 'PLUS':
            if cdr(cdr(x)) != 'NIL':
                print('CONS expects exactly two arguments')
                raise lisperror
            if (isinstance(car(x),int)!=True or isinstance(car(cdr(x)), int)!=True):
                print('Less expects two args are interger')
                raise lisperror
            return car(x) + car(cdr(x))
        elif f == 'MINUS':
            if cdr(cdr(x)) != 'NIL':
                print('CONS expects exactly two arguments')
                raise lisperror
            if (isinstance(car(x),int)!=True or isinstance(car(cdr(x)), int)!=True):
                print('Less expects two args are interger')
                raise lisperror
            return car(x) - car(cdr(x))
        elif f == 'TIMES':
            if cdr(cdr(x)) != 'NIL':
                print('CONS expects exactly two arguments')
                raise lisperror
            if (isinstance(car(x),int)!=True or isinstance(car(cdr(x)), int)!=True):
                print('Less expects two args are interger')
                raise lisperror
            return car(x) * car(cdr(x))
        elif f == 'QUOTIENT':
            if cdr(cdr(x)) != 'NIL':
                print('CONS expects exactly two arguments')
                raise lisperror
            if (isinstance(car(x),int)!=True or isinstance(car(cdr(x)), int)!=True):
                print('Less expects two args are interger')
                raise lisperror
            return car(x) / car(cdr(x))
        elif f == 'REMAINDER':
            if cdr(cdr(x)) != 'NIL':
                print('CONS expects exactly two arguments')
                raise lisperror
            if (isinstance(car(x), int) != True or isinstance(car(cdr(x)), int) != True):
                print('Less expects two args are interger')
                raise lisperror
            return car(x) % car(cdr(x))
        elif f == 'LESS':
            if cdr(cdr(x)) != 'NIL':
                print('CONS expects exactly two arguments')
                raise lisperror
            if (isinstance(car(x),int)!=True or isinstance(car(cdr(x)), int)!=True):
                print('Less expects two args are interger')
                raise lisperror
            if car(x) < car(cdr(x)):
                return 'T'
            else:
                return 'NIL'
        elif f == 'GREATER':
            if cdr(cdr(x)) != 'NIL':
                print('CONS expects exactly two arguments')
                raise lisperror
            if (isinstance(car(x),int)!=True or isinstance(car(cdr(x)), int)!=True):
                print('Less expects two args are interger')
                raise lisperror
            if car(x) > car(cdr(x)):
                return 'T'
            else:
                return 'NIL'

        elif f == 'ATOM':
            if cdr(x)!='NIL':
                print('ATOM expects exactly one argument')
                raise lisperror
            if Atom(car(x))=='T':
                return 'T'
            else:
                return 'NIL'
        elif f == 'INT':
            if cdr(x)!='NIL':
                print('INT expects exactly one argument')
                raise lisperror
            if Atom(car(x))=='T':
                try:
                    int(car(x))
                    return 'T'
                except:
                    return 'NIL'
            else:
                return 'NIL'
        else:
            arg1 = cdr(getval(f, gdlist)) # not sure here
            addpairs(car(getval(f, gdlist)), x, {})
            arg3 = {} # gdlist
            return evaluate(arg1, {}, arg3)
    else:
        print(('No such function'))
        raise lisperror
# test lispapply
# f = 'CONS'
# x = convert(parse('(3 4)'))
# pretty_print(lispapply(f,x,,{}))
# expr = ['(2 3)']
# for i in range(len(expr)):
#     alist = {'w': 1, 'y': 2}
#     dlist = {}
#     x = convert(parse(expr[i]))
#     f = 'CONS'
#     lispapply(f, x, alist, dlist)
#
# test = convert(parse('(2 3)'))
# lispapply('CDR', convert(parse('((x y z))')), alist,{})
def evcon(exp, alist, dlist):
    global galist,gdlist
    if null(exp)=='T':
        print('All conditions of COND evaluated to false')
        raise lisperror
    else:
        if cdr(cdr(car(exp))) != 'NIL':
            print('All clauses of COND must be of size 2')
            raise lisperror
        else:
            if evaluate(car(car(exp)), {}, {}) == 'T' or isinstance(evaluate(car(car(exp)), {}, {}), int)==True:
                e = car(cdr(car(exp)))
                return evaluate(e, {}, {})
            # elif evaluate(car(car(exp)), alist, {}) == 'NIL':
            else:
                return evcon(cdr(exp), {}, {})

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
        try:
            isinstance(int(exp), int)
            if isinstance(int(exp), int):
                return int(exp)
        except ValueError:
            if (exp == 'T'):
                return 'T'
            elif (exp == 'NIL'):
                return 'NIL'
            elif (exp in galist):
                return galist[exp]
                # return alist.get(exp) # very important!
            else:
                print('unbound variable')
                raise lisperror
    elif Atom(car(exp))=='T':
        if car(exp)=='QUOTE':
            if cdr(cdr(exp))!='NIL':
                print ('QUOTE expects only one arg/must have wrong arguments')
                raise lisperror
            return car(cdr(exp))
        elif car(exp)=='COND':
            return evcon(cdr(exp), {}, {})
        elif car(exp)=='DEFUN':
            func_name = car(cdr(exp))
            plist = car(cdr(cdr(exp)))
            fb = car(cdr(cdr(cdr(exp))))
            gdlist[func_name] = ['(', plist, '.', fb, ')']
            return func_name
        else:
            f = car(exp) # exp[1] # same as car(exp), sketchy here
            x = evlis(cdr(exp), {}, {})
            # return lispapply(f, x, alist, {})
            if x == None:
                return f
            else:
                _galist = galist
                _gdlist = gdlist
                return lispapply(f, x, {}, {})
    else:
        print('Must be some error in evaluation')
        raise lisperror

sexp = convert(parse('((b1 e1) (b2 e2) (b3 e3))'))
galist = {'b1':'NIL','b2':'T','b3':'NIL'}
gdlist = {'e1':8,'e2':4,'e3':2}

def addpairs(plist, x, alist):
    global galist
    if plist=='NIL':
        return galist
    else:
        try:
            len(plist)==5
            len(x) == 5
        except (AssertionError, TypeError):
            pass
        if car(plist) in galist:
            if galist[car(plist)] != car(x):
                pass
                print('before: %s' % galist[car(plist)])
                print('overwritten happen, key is %s, value is %s'%(car(plist), car(x)))
        galist[car(plist)] = car(x) # need to evalulate it!
        # galist[car(plist)] = evaluate(car(x), {},{})
        addpairs(cdr(plist), cdr(x), {})
        return galist

plis = convert(parse('(p1 p2 p3)'))
xlis = convert(parse('(x1 x2 x3)'))
alis = {}
# addpairs(plis, xlis, alis)




test = convert(parse('(F.(plist. fb))'))
alist={'w':1,'y':2}
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
# for i in range(length):
# # for i in [8]:
#     dotstr = convert(parse(test_str[i]))
#     print ('the string %s is the following'%i)
#     pretty_print(dotstr)
#     result = evaluate(dotstr, alist, gdlist)
#     print(result)
#     pretty_print(evaluate(dotstr, alist, gdlist))
#     print(result);print('\n')
#     # pretty_print(result)

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
        try:
            pretty_print(dotstr)
            # print('finish pretty print')
            evaluate(dotstr, {}, {})
            result = evaluate(dotstr, {}, {})
            # print(result)
            pretty_print(result)
            print('\n')
        except lisperror:
            print('lisp error are caught\n')