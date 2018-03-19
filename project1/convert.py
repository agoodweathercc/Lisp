def flatten(lst):
    return sum(([x] if not isinstance(x, list) else flatten(x) for x in lst), [])

def matched(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] == "(":
            count += 1
        elif lst[i] == ")":
            count -= 1
        if ((i<len(lst)-1) and count < 1):
            print('parentheses do not match')
            return False
    return count == 0

def tokenize(chars):
    "convert a string of characters into a list of tokens"
    # if (len(chars)==2 and chars[0] == '(' and chars[1]==')'):
    #     return ''
    if len(chars) ==1:
        print('SyntaxError missing ( or )')
        return -1
    else:
        result = chars.replace('(', ' ( ').replace(')', ' ) ').replace('.',' . ').split()
        if (isinstance(result,list)==True and result.count('(')!=result.count(')')):
            print("number of ( and ) is not equal!")
            return -1
        elif ('+' in result or '-' in result or '*' in result or '/' in result ):
            print('+-*/ operator are not allowed')
            return -1
        if matched(result)==False:
            return -1
        return result

def read_from_tokens(tokens):
    "Read an expression from a sequence of tokens."
    if (tokens == 'NIL'):
        return ['NIL']
    if tokens==['(',')']:
        return 'NIL'
    if tokens == -1:
        return -1
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)

    if token == '(':
        L = []
        # if tokens[0]==')':
        #     L.append('NIL')
            # L.append(read_from_tokens(tokens))
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0)  # pop off ')'
        return L
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

def parse(program):
    "Read a Scheme expression from a string."
    return read_from_tokens(tokenize(program))

def checkdot(lst):
    if isinstance(lst,list)==True:
        if (lst.count('.') > 1):
            print('more than one dot in exp,wrong!')
            return -1
        # if isinstance(lst,list)==False:
        #     print('  ')

        elif ('.' in lst and lst.count('.') == 1):
            if len(lst) != 3:
                print('error, there should be one element both at the left and right of . symbol')
                return -1
            elif (len(lst) == 5 and lst[2] == '.'):
                checkdot(lst[1])
                checkdot(lst[3])
        else:
            return 0

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
    s = ""
    for i in range(len(l)):
        s = s + str(l[i])
    return s

def str2list(s):
    return list(s)

def pretty_print(l):
    print(list2str(flatten(l)))
    return list2str(flatten(l))

def ifnested(a):
    "check whether a is a nested list"
    return any(isinstance(i, list) for i in a)

def convert(l):
    if l==[]: # case []
        return ['NIL']
    if isinstance(l, list) == False:
        return l
    elif (len(l) == 1 and isinstance(l[0], list) == False):
        return ['(', l[0], '.', 'NIL', ')']
    elif (len(l) == 1 and isinstance(l[0], list) == True):
        return ['(', convert(l[0]), '.', 'NIL', ')']

    elif (l.count('.') > 1):
        print('number of . can not be more than 1')
        return -1
    elif (len(l) == 3 and l[1] == '.'):
        lst = ['(', convert(l[0]), '.', convert(l[2]), ')']
        # print('call it')
        return lst
    else:
        return ['(', convert(l[0]), '.'] + [convert(l[1:])] + [')']

def read_test(path):
    with open(path) as f:
        mylist = f.read()
    mylist = mylist.replace('\n','')
    mylist = mylist.split('$')
    del mylist[-1]; del mylist[-1]
    return mylist

# test = ['(silly (car (quote (5 . 6))) (cdr (quote (5 . 6))) )', '(silly 5 b)', '(defun silly (a b) (plus a b))',
#         '(car (quote (a . b))

if __name__ == '__main__':
    test = read_test('./incorrect.txt')
    for i in test:
        print(i)
        if parse(i)!=-1:
            # convert(parse(i))
            if convert(parse(i)) != -1:
                if checkdot(parse(i)) !=-1:
                    pretty_print(convert(parse(i)))
                    print('\n')
