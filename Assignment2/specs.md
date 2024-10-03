## Overview
This program is a calculator that uses Lark parsing for its expressions. It reads the given expression through the terminal, parses it, transforms it into an AST, and evaluates it. 

## Key Components
### Transformer Class
Name: CalcTransformer <br/>
Purpose: transforms the parsed expression into an AST.<br/>
Methods in CalcTransformer:<br/>
plus(self, items):<br/>
Purpose: transforms the plus operation<br/>

minus(self, items):<br/>
Purpose: transforms the minus operation<br/>

times(self, items):<br/>
Purpose: transforms the multiplication operation<br/>

power(self, items):<br/>
Purpose: transforms the power operation<br/>

neg(self, items):<br/>
Purpose: transforms the negative operation<br/>

log(self, items):<br/>
Purpose: transforms the log operation<br/>

num(self, items):<br/>
Purpose: transforms a number<br/>

### Evaluation Function
Name: evaluate(ast)<br/>
Purpose: evaluates the AST and calculates it<br/>
