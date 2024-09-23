#gives an operator a value depending on the operator
def operatorValue(op):
    if op == '+':
        return 1
    if op == '*':
        return 2
    if op == '^':
        return 3
    return 0

#takes an array full of operators
#takes an array full of nums
#does the operation depending on the operator
def operation(operators, nums):
    right = nums.pop()  
    left = nums.pop()   
    operator = operators.pop()  
    
    if operator == '+':
        nums.append(left + right)
    elif operator == '*':
        nums.append(left * right)
    elif operator == '^':
        nums.append(left ** right)

def calculate(input):

    operators = []
    nums = []
    i = 0

    while i < len(input): 
        #if the position of i is a number it inputs it into the nums array   
        if input[i].isdigit():
            val = 0
            while i < len(input) and input[i].isdigit():
                val = str(val) + input[i]
                i += 1
            nums.append(int(val))
            i -= 1  
        #if position of i is (, it puts it into the operators
        elif input[i] == '(':
            operators.append(input[i])
        #if position of i is ), and the front of operators isnt (, then it does the operations inside the parentheses
        elif input[i] == ')':
            while operators and operators[-1] != '(':
                operation(operators, nums)
            operators.pop() 
        #if position of i is an operator, and the front of operators isnt (, it does the operation
        elif input[i] in "+*^":
            while (operators and operators[-1] != '(' and
                   operatorValue(operators[-1]) >= operatorValue(input[i])):
                operation(operators, nums)
            operators.append(input[i])

        i += 1
    #does the rest of the oerpations
    while operators:
        operation(operators, nums)
    #returns the remaining number
    return nums[-1]

input = input()
result = calculate(input)
print(result)