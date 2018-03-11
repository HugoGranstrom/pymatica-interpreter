import sys
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import re

var_dict = {}
reserved_names = ['var', 'cos', 'sin', 'tan']
file_name = sys.argv[1]

# loop through var_dict and see if expr includes any of them. Then replace it with '(' ')' around it.
def insert_vars(expr):
    splitted_expr = re.split('(\W)', expr)
    for i, token in enumerate(splitted_expr):
        if token in var_dict:
            splitted_expr[i] = "(" + var_dict[token] + ")"
    string_expr = ''.join(str(e) for e in splitted_expr)
    return string_expr




# read from file test.pymath and save it in source
with open(file_name, "r") as f:
    source = f.read()

# split source into lines
source = source.split("\n")

for s in source:
    s_space = s.split(" ")
    
    # if first word is '#' the line is a comment and is skipped
    if s_space[0].lower() == "#":
        continue
    # if the first word is 'var' treat the line as a variable assignment 
    elif s_space[0].lower() == "var":
        # if var_name in reserved_names -> not allowed
        var_name = s_space[1] 
        var_value = ' '.join(str(e) for e in s_space[3:]) # value is everything after the '='
        var_value = '({})'.format(var_value) # add parentases around the value
        var_value = insert_vars(var_value) # replace variables with their values
        var_dict[var_name] = var_value # add name/value pair to variable dictionary
    elif s_space[0].lower() == "print":
        expr = ' '.join(str(e) for e in s_space[1:])
        inserted_expr = insert_vars(expr)
        # clean expr before printing if first and last char is paranteses
        while True:
            if inserted_expr[0] == "(" and inserted_expr[-1] == ")":
                inserted_expr = inserted_expr[1:-1]
            else:
                break
        eval_expr = parse_expr(inserted_expr)
        print(eval_expr)
    # save var_dict to json file
    elif s_space[0].lower() == "save":
        file_name = s_space[1]
        if s_space[2].lower() == "append":
            #with open(file_name, "a") as f
            pass
    else:
        # maybe use this as print 
        continue

    
# for i in var_dict:
#     print(var_dict[i])
