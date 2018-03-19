the default path of test file is './correct.txt'.
To run it on the incorrect text file, change the file directory at line 143. And run it with python convert.py.

correct.txt contains all the test s-expression that is correct
incorrect.txt contains all the test s-expression that is incorrect

Borrow ideas from the artile by Peter Norvig. http://norvig.com/lispy.html
I used borrow three functions(read_from_tokens, tokensizer and parse) there to parse the string.