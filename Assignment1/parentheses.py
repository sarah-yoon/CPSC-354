def parentheses(input):
    rightCount = 0
    leftCount = 0
    onlyParentheses = True
    for char in input:
        if char == '(':
            rightCount += 1
        elif char == ')':
            leftCount += 1
        else:
            onlyParentheses = False
    if(rightCount==leftCount and onlyParentheses):
        print("yes")
    elif(rightCount!=leftCount or not onlyParentheses):
        print("no")

parentheses(input())