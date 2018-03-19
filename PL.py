def flatten(lst):
    return sum( ([x] if not isinstance(x,list) else flatten(x) for x in lst),[])
lst= [[1],2,[[3,4],5],[[]],[[6]],7,8,[]]
flatten(lst)

def tokenize(chars):
    "convert a string of characters into a list of tokens"
    return chars.replace('(',' ( ').replace(')', ' ) ').split()

def parse(program):
    "Read a Scheme expression from a string."
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens):
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

def atom(token):
    "Numbers become numbers; every other token is a symbol."
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return str(token)

def list2str(l):
    "convert a non-nested list into a string"
    s=""
    for i in range(len(l)):
        s = s +str(l[i])
    return s

def str2list(s):
    return list(s)

def ifnested(a):
    "check whether a is a nested list"
    return any(isinstance(i, list) for i in a)

def convert(s):
    """convert a non-nested s-expression into dot notation, input is a list, output is also a list"""
    if len(s)==1:
        if '.' in s[0]:
            return s
        else:
            return ['('] + s + ['.', 'NIL'] + [')']

    # if len(s)==3:
    #     return '('+ s[1]+ '.'+ 'NIL'+')'
    else:
        ans = ['('] + [s[0]] + ['.'] + convert(s[1:]) + [')']
        # ans = ''.join(ans)
        return ans
list2str(convert(parse('(x y.t z)')))

def convertlist(l):
    if isinstance(l,list)==False:
        return l

    if (len(l)==1 and isinstance(l[0],list)==False):
        return ['(',l[0],'.','NIL',')']
    elif (len(l)==1 and isinstance(l[0],list)==True):
        # print('call second')
        return ['(',convertlist(l[0]),'.','NIL',')']
    else:
        return ['(',convertlist(l[0]),'.'] + convertlist(l[1:]) + [')']

test = ['(2)', '(1 2 3)', '(1 (2 3))', '((1))','((1 2 (3 4) 5))','(DEFUN MINUS2 (A B) (MINUS A B))']

for i in test:
    print(i)
    print(pretty_print(convertlist(parse(i))))


def convertNest(l):
    """input is a list output is a list"""
    if ifnested(l)==False:
        return convertlist(l)
    else:
        tmp_list =[]
        for i in range(len(l)):
            if type(i)==list:
                tmp_list = tmp_list +  [convertNest(l[i])]
            else:
                tmp_list = tmp_list + [l[i]]
        # import itertools
        # flatten_list = list(itertools.chain.from_iterable(*tmp_list))
        return convertlist(tmp_list)
test = '(1 2 (3 4) 5)'
convertNest(parse(test))

def pretty_print(l):
    print(list2str(flatten(l)))
    return list2str(flatten(l))

def convertDot(lst):
    if len(lst)==3 and lst[1]=='.':
        l = convertNest(lst[0]) + ['.'] + convertNest(lst[2])
        print(pretty_print(l))
    else:
        print('error! Either the number of arg is not 3, or the second arg is not . symbol')

def convertDot(lst):
    if len(lst)==3 and lst[1]=='.':
        l = eval(lst[0]) + ['.'] + convertNest(lst[2])
        print(pretty_print(l))
    else:
        print('error! Either the number of arg is not 3, or the second arg is not . symbol')


test = '((x y) . ( 1  2 ) )'
test = '(x . y. z)'
convertDot(parse(test))


def convertcons(s):
    if 'cons' in s:
        if len(s)!=3:
            print('error! Expect 3 arguments')
        else:
            return [s[1]] + ['.'] + [s[2]]
pretty_print(convertcons(['cons', 's','1']))

def convertquote(s):
    if (len(s)==2 and s[0]=='quote'):
        return s[1]
    else:
        print('quote error!')

def eval(s):
    if (len(s)==3 and s[1]=='.'):
        return  pretty_print(convertDot(s))
    elif s[0] == 'cons':
        return pretty_print(convertcons(s))
    elif s[0] == 'quote':
        return pretty_print(convertquote(s))
    elif ('.' in s)==False:
        return  convertlist(s)
    else:
        print('must be some uncatched error!')


test = ['(cons s y)', '((1 x) . (2 3))', '(1 2  (3 4))', '(quote (x y z))']
for s in test[2:3]:
    # print(s)
    print(pretty_print(eval(parse(s))))


def atomsexp(s):
    """:return whethen s is an atom s-expression or not"""
    if len(s)==1 and len(s[0]):
        return True
    else:
        return 0





if __name__=='__main__':
    file = open('/Users/admin/PycharmProjects/untitled/venv/test.txt','r')
    lines = file.readlines()
    for test_string in lines:
        test_string = test_string.split('$')
        test_string = test_string[:-1]
        print(test_string)
        for i in test_string:
            parse_string = parse(i)
            l = convertNest(parse_string)
            print(pretty_print(l))

    test_string = '(1 3 (m.n) (x.y))'
