def arithmetic_arranger(problems, *result):
    operands_operations = []
    str_op1 = ""
    str_op2 = ""
    dashes = ""
    dash_count_list = []
    compute_result = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        if '+' in problem:
            pass
        elif '-' in problem:
            pass
        else:
            return "Error: Operator must be '+' or '-'."

    for problem in problems:
        if '+' in problem:
            operands_operations.append(problem.split(' '))
        else:
            operands_operations.append(problem.split(' '))

    for i in range((len(operands_operations))):
        if not operands_operations[i][0].isdigit() or not operands_operations[i][2].isdigit():
            return "Error: Numbers must only contain digits."
        elif len(operands_operations[i][0]) > 4 or len(operands_operations[i][2]) > 4:
            return "Error: Numbers cannot be more than four digits."

    for operands in operands_operations:
        operands[0] = int(operands[0])
        operands[2] = int(operands[2])
        if len(result) != 0:
            if operands[1] == '+':
                operands.append(operands[0] + operands[2])
            else:
                operands.append(operands[0] - operands[2])

    i = 0
    for operands in operands_operations:
        if len(str(operands[0])) < len(str(operands[2])):
            str_op1 += "  " + " " * (len(str(operands[2])) - len(str(operands[0]))) + str(operands[0])
            str_op2 += operands[1] + " " + str(operands[2])
        else:
            str_op1 += "  " + str(operands[0])
            str_op2 += operands[1] + " " + " " * (len(str(operands[0])) - len(str(operands[2]))) + str(operands[2])

        dashes += '-' * (max(len(str(operands[0])), len(str(operands[2]))) + 2)
        dash_count_list.append(max(len(str(operands[0])), len(str(operands[2]))) + 2)
        if i == len(operands_operations) - 1:
            str_op1 += '\n'
            str_op2 += '\n'
        else:
            str_op1 += "    "
            str_op2 += "    "
            dashes += "    "
            i += 1

    arranged_problems = str_op1 + str_op2 + dashes
    if len(operands_operations[0]) == 4:
        i = 0
        arranged_problems += '\n'
        for operands in operands_operations:
            compute_result += " " * (dash_count_list[i] - len(str(operands[3]))) + str(operands[3])
            if i < len(operands_operations) - 1:
                compute_result += "    "
            i += 1
        return arranged_problems + compute_result
    else:
        return arranged_problems
