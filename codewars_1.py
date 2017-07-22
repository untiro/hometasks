def calc_pol(pol_str, x = None):
    # your code here
    import ast
    if x is None:
        return "There is no value for x"
    node = ast.parse(pol_str, mode='eval')
    code_object = compile(node, filename='<string>', mode='eval')
    result = eval(code_object)
    if result != 0:
        return "Result = " + str(result)
    else:
        return "Result = " + str(result) + ", so  " + str(x) + " is a root of " + pol_str

pol_str = "2*x**2 + 3*x"
#x = 4
print(calc_pol(pol_str))