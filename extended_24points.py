import sympy as sy
from sympy import sqrt
import copy
# expressions: list
# each expression: {"expression": str, "pre_operator": str, "result": sympy.Rational}
# allowed_operators: list: [["+","-","*","/","^"],["","sqrt","factorial"]]
def twenty_four_points_expansion(expressions: list, allowed_operators: list, valid_expression: list, target_number=24):

    # only one expression left, check if it is target number
    if len(expressions) == 1:
        if expressions[0]["result"] == target_number:
            return valid_expression.append(expressions[0]["expression"])
        else:
            return valid_expression
        
    # more than one expression left
    for first_expression_order in range(len(expressions)):
        first_expression_original=copy.deepcopy(expressions[first_expression_order])
        for second_expression_order in range(len(expressions)):

            # avoid same
            if first_expression_order == second_expression_order:
                continue
            second_expression_original=copy.deepcopy(expressions[second_expression_order])

            other_expressions = [expressions[i] for i in range(len(expressions)) if i != first_expression_order and i != second_expression_order]

            # self operation for first: sqrt, factorial, None
            for first_operator in allowed_operators[1]:
                # print("first_operator ",first_operator)
                first_expression_expression=copy.deepcopy(first_expression_original["expression"])
                first_expression_pre_operator=copy.deepcopy(first_expression_original["pre_operator"])
                first_result=copy.deepcopy(first_expression_original["result"])
                if first_operator == "factorial":

                    # not int or negative
                    if first_result != int(first_result) or first_result < 0:
                        continue

                    # positive int or 0
                    first_expression_expression = "factorial("+first_expression_expression+")"
                    first_expression_pre_operator = "factorial"
                    first_result = sy.factorial(first_result)

                elif first_operator == "sqrt":
                    # negative
                    if first_result < 0:
                        continue

                    # positive or 0
                    first_expression_expression = "sqrt("+first_expression_expression+")"
                    first_expression_pre_operator = "sqrt"
                    first_result = sqrt(first_result)
                    
                first_expression_after_single_process={"expression": first_expression_expression, "pre_operator": first_expression_pre_operator, "result": first_result}
                # print("first_expression_after_single_process ",first_expression_after_single_process)

                # self operation for second: sqrt, factorial, None
                for second_operator in allowed_operators[1]:
                    second_expression_expression=copy.deepcopy(second_expression_original["expression"])
                    second_expression_pre_operator=copy.deepcopy(second_expression_original["pre_operator"])
                    second_result=copy.deepcopy(second_expression_original["result"])
        
                    if second_operator == "factorial":
                        # not int or negative
                        if second_result != int(second_result) or second_result < 0:
                            continue

                        # positive int or 0
                        second_expression_expression = "factorial("+second_expression_expression+")"
                        second_expression_pre_operator = "factorial"
                        second_result = sy.factorial(second_result)
                    elif second_operator == "sqrt":
                        # negative
                        if second_result < 0:
                            continue

                        # positive or 0
                        second_expression_expression = "sqrt("+second_expression_expression+")"
                        second_expression_pre_operator = "sqrt"
                        second_result = sqrt(second_result)

                    second_expression_after_single_process={"expression": second_expression_expression, "pre_operator": second_expression_pre_operator, "result": second_result}


                    # combined operation: +, -, *, /, ^
                    for combined_operator in allowed_operators[0]:
                        first_expression = copy.deepcopy(first_expression_after_single_process)
                        second_expression = copy.deepcopy(second_expression_after_single_process)

                        if combined_operator in ["+","-"]:
                            # + - are lowest priority, for the other pre_operator, add ()
                            if second_expression_pre_operator not in ["+","-","","factorial","sqrt"]:
                                second_expression["expression"] = "("+second_expression["expression"]+")"
                            
                            combined_expression = first_expression["expression"]+combined_operator+second_expression["expression"]
                            combined_pre_operator = combined_operator

                            if combined_operator == "+":
                                combined_result = first_expression["result"]+second_expression["result"]
                            elif combined_operator == "-":
                                combined_result = first_expression["result"]-second_expression["result"]

                        elif combined_operator in ["*"]:
                            # * higher priority than + -
                            if (first_expression_pre_operator in ["+","-"]) and (first_expression_pre_operator not in ["factorial","sqrt"]):
                                first_expression["expression"] = "("+first_expression["expression"]+")"
                            
                            # * higher priority than + -, but lower than ^, add () for second expression
                            if (second_expression_pre_operator in ["+","-"]) and (second_expression_pre_operator not in ["factorial","sqrt"]):
                                second_expression["expression"] = "("+second_expression["expression"]+")"
                        
                            combined_expression = first_expression["expression"]+combined_operator+second_expression["expression"]
                            combined_pre_operator = combined_operator

                            combined_result = first_expression["result"]*second_expression["result"]

                        elif combined_operator in ["/"]:
                            # if second expression is 0, skip
                            if second_expression["result"] == 0:
                                continue

                            # / is higher priority than + -
                            if (first_expression_pre_operator in ["+","-"]) and (first_expression_pre_operator not in ["factorial","sqrt"]):
                                first_expression["expression"] = "("+first_expression["expression"]+")"
                            
                            # / is not symmetric, add () for second expression if it is not ^, because ^ is higher priority than /
                            if second_expression_pre_operator not in ["^","","factorial","sqrt"]:
                                second_expression["expression"] = "("+second_expression["expression"]+")"
                        
                            
                            combined_expression = first_expression["expression"]+combined_operator+second_expression["expression"]
                            combined_pre_operator = combined_operator
                            combined_result = sy.Mul(first_expression["result"], 1/second_expression["result"])

                        
                        elif combined_operator == "^":
                            # ^ is highest priority, add () for first expression if it is not ^ or ""
                            if first_expression_pre_operator not in ["","^","factorial","sqrt"]:
                                first_expression["expression"] = "("+first_expression["expression"]+")"
                            
                            # ^ is highest priority, add () for second expression if it is not ""
                            if second_expression_pre_operator not in ["","factorial","sqrt"]:
                                second_expression["expression"] = "("+second_expression["expression"]+")"
                            combined_expression = first_expression["expression"]+"**"+second_expression["expression"]
                            combined_pre_operator = "^"
                            combined_result = sy.Pow(first_expression["result"], second_expression["result"])

                        next_try_expressions = other_expressions + [{"expression": combined_expression, "pre_operator": combined_pre_operator, "result": combined_result}]
                        # iterate next try
                        twenty_four_points_expansion(next_try_expressions, allowed_operators, valid_expression, target_number)
    return valid_expression

def init_inputs(input_numbers):
    expressions=[]
    for i in input_numbers:
        expressions.append({"expression": str(i), "pre_operator": "", "result": i})
    return expressions
                    
                            