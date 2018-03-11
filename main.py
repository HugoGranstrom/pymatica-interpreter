import sys
import json

from sympy.parsing.sympy_parser import parse_expr
from sympy import *

# don't move re up, it will break the program for some reasong. Maybe it has to do with parse_expr
import re

init_printing(use_unicode=False)

var_dict = {}
reserved_names = ['var', 'cos', 'sin', 'tan', 'pi', 'e']
file_name = sys.argv[1]

# loop through var_dict and see if expr includes any of them. Then replace it with '(' ')' around it.
def insert_vars(expr):
    splitted_expr = re.split( '(\W)', expr )
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

    # print the answer in sympy form, use printf if you want decimal
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
        pprint(eval_expr)

    # save var_dict to json file
    elif s_space[0].lower() == "save":
        file_name = s_space[1]
        if s_space[2].lower() == "append":
            try:
                with open(file_name, "r+") as f:
                    old_save = json.load(f.read())
                    new_save = {**old_save, **var_dict}
                    json.dump(new_save ,f)
            except:
                with open(file_name, "w+") as f:
                    json.dump(var_dict ,f)
        elif s_space[2].lower() == "overwrite":
            answer = input("This will delete all your old variables saved in {}. Are you sure you want to delete those? (y/n)".format(file_name))
            if answer[0].lower() == "y":
                with open(file_name, "w+") as f:
                    json.dump(var_dict ,f)
            else: 
                print("Use the command 'save filename append' instead if you want to save your old variables")

    # load var_dict from json file overringing the old local variables
    elif s_space[0].lower() == "load":
        file_name = s_space[1]
        with open(file_name, "r") as f:
            loaded_save = f.read()
            loaded_save = json.loads(loaded_save)
            new_save = {**var_dict, **loaded_save}
            var_dict = new_save

    # same as print but prints the decimal form
    elif s_space[0].lower() == "printf":
        expr = ' '.join(str(e) for e in s_space[1:])
        inserted_expr = insert_vars(expr)
        # clean expr before printing if first and last char is paranteses
        while True:
            if inserted_expr[0] == "(" and inserted_expr[-1] == ")":
                inserted_expr = inserted_expr[1:-1]
            else:
                break
        eval_expr = parse_expr(inserted_expr)
        print(eval_expr.evalf())

    else:
        # maybe use this as print 
        continue
