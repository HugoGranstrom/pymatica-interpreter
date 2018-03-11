# pymatica-interpreter

# Usage
At the moment the commands used are SymPy's. See their documentation for which functions are available. Example usage for differentiating a function:
`var y = diff(x**2 + exp(2*x), x)`
´print y´
This will print out ´2*x + 2*exp(2*x)´
See the example.pymath file for examples of how to use Pymatica.

## Running script
To run a .pymath file (just a txt file) run run this command:
`python main.py filename`

## What's Working
- Comments (`# this is a comment`)
- Variables (`var number = 6`)
- Printing and evaluating expressions (`print diff(sin(t) + x*t, t)`) 

## Syntax
Every expression is one line, so no multi-line expressions. 

## TODO
- Saving variables to file (json)
