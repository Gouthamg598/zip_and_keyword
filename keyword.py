import keyword as key
print(key.kwlist)

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'] 

print(len(key.kwlist))#35

print(key.iskeyword('False'))#True
print(key.iskeyword('print'))#False
print(key.iskeyword('return'))#True
print(key.iskeyword('assert'))#True
print(key.iskeyword('try'))#True
print(key.iskeyword('None'))#True
