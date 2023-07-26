def func_a(numA, numB, exp):
    if exp == '+':
        return numA + numB
    elif exp == '-':
        return numA - numB
    elif exp == '*':
        return numA * numB
    
def func_b(exp):
    for index, value in enumerate(exp):
        if value == '+' or value == '-' or value == '*':
            return index
        
def func_c(exp, idx):
    numA = int(exp[:idx])
    numB = int(exp[idx + 1:])
    return numA, numB

def solution(expression):
    exp_index = func_b(expression)
    first_num, second_num = func_c(expression, exp_index)
    result = func_a(first_num, second_num, expression[exp_index])
    return result

#The following is code to output testcase.
expression = "123+12"
ret = solution(expression)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")