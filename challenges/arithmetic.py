from ast import arg
import inspect

def get_num_in_digit(num_in_words):
    zero_to_nine = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    return zero_to_nine[num_in_words]

def do_opr(operand1, operator, operand2):
    if operator == 'plus':
        return operand1 + operand2
    elif operator == 'minus':
        return operand1 - operand2
    elif operator == 'times':
        return operand1 * operand2
    elif operator == 'divided_by':
        return operand1 // operand2

def common_operation(*args):
    operand1 = args[0]
    operator = None
    operand2 = None
    if len(args) > 1:
        operator = args[1][0]
        operand2 = args[1][1]
        return do_opr(operand1, operator, operand2)
    else:
        return operand1

def zero(*args):
    return common_operation(get_num_in_digit(inspect.stack()[0][3]), *args)

def one(*args):
    return common_operation(get_num_in_digit(inspect.stack()[0][3]), *args)

def two(*args):
    return common_operation(get_num_in_digit(inspect.stack()[0][3]), *args)

def three(*args):
    return common_operation(get_num_in_digit(inspect.stack()[0][3]), *args)

def four(*args):
    return common_operation(get_num_in_digit(inspect.stack()[0][3]), *args)

def five(*args):
    return common_operation(get_num_in_digit(inspect.stack()[0][3]), *args)

def six(*args):
    return common_operation(get_num_in_digit(inspect.stack()[0][3]), *args)

def seven(*args):
    return common_operation(get_num_in_digit(inspect.stack()[0][3]), *args)

def eight(*args):
    return common_operation(get_num_in_digit(inspect.stack()[0][3]), *args)

def nine(*args):
    return common_operation(get_num_in_digit(inspect.stack()[0][3]), *args)

def plus(operand_2):
    return inspect.stack()[0][3], operand_2

def minus(operand_2):
    return inspect.stack()[0][3], operand_2

def times(operand_2):
    return inspect.stack()[0][3], operand_2

def divided_by(operand_2):
    return inspect.stack()[0][3], operand_2

#print(nine(divided_by(nine())))