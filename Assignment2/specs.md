## Overview
This program is a calculator that uses Lark parsing for its expressions. It reads the given expression through the terminal, parses it, transforms it into an AST, and evaluates it. 

## Key Components
### Transformer Class
Name: CalcTransformer
Purpose: transforms the parsed expression into an AST.
Methods in CalcTransformer:
plus(self, items):
Purpose: transforms the plus operation

minus(self, items):
Purpose: transforms the minus operation

times(self, items):
Purpose: transforms the multiplication operation

power(self, items):
Purpose: transforms the power operation

neg(self, items):
Purpose: transforms the negative operation

log(self, items):
Purpose: transforms the log operation

num(self, items):
Purpose: transforms a number

### Evaluation Function
Name: evaluate(ast)
Purpose: evaluates the AST and calculates it
