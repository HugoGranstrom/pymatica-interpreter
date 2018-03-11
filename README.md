# pymatica-interpreter

# Usage

## Running script
To run a .pymath file (just a txt file) run run this command:
`python main.py filename`

## What's Working
- Comments (`# this is a comment`)
- Variables (`var number = 6`)
- Printing and evaluating expressions (`print diff(sin(t) + x*t, t)`) 

## Syntax
Every expression is one line, so no multi-line expressions
Separate all tokens (variables, operators, parentases) by spaces

## TODO
- Saving variables to file (json)