# Ideas

## Syntax
- Every expression is a line, no multiline (+)
- Variable assignment when first word on line is `var` (+)
- A symbol `#` for comments, those lines starting with that symbol gets ignored by the interpreter (+)
- Mathematical functions have the syntax `func()`
- Replace custom function names with sympy ones. (eg. ) 
- save statement: `save filename append/overwrite` (+)
- non character values is not allowed in variable names -> _,./-+()&%¤#"@£${[]}\? (+)

## Functionality
- Iteratable (`do 4 action`)
- save section in the program file at the bottom as json. save_section = Source.split("Save section") first and then source.split("\n) and then source.split(" ")
- config section of file where settings can be set.
- add try/except claus to all elif's and print("printing error") etc in REPL.
- add a last answer to REPL.
- reserved variable names