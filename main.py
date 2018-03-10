from sympy import *
from sympy.parsing.sympy_parser import parse_expr

var_dict = {}

# read from file test.pymath and save it in source
with open("test.pymath", "r") as f:
    source = f.read()

# split source into lines
source = source.split("\n")

for s in source:
    s = s.split(" ")
    
    # if first word is '#' the line is a comment and is skipped
    if s[0].lower() == "#":
        continue
    # if the first word is 'var' treat the line as a variable assignment 
    elif s[0].lower() == "var":
        var_name = s[1] 
        var_value = ' '.join(str(e) for e in s[3:]) # value is everything after the '='
        var_value = '({})'.format(var_value) # add parentases around the value
        var_value = parse_expr(var_value, evaluate=False) # convert input to sympy expression but do not evaluate it. That is done only when printing answers
        var_dict[var_name] = var_value # add name/value pair to variable dictionary
    
for i in var_dict:
    print(var_dict[i])