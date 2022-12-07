# Do math
# https://medium.com/codex/another-python-question-that-took-me-days-to-solve-as-a-beginner-37b5e144ecc
def CalcMath(expr):
    expr = expr.replace(" ", "")

    #* It can do "2 - 1" but fails to do "-1 + 2", solve it ~> (Solved)
    expr = expr if not expr.startswith("-") else "0" + expr

    def splitby(string, separators):
        lis = []
        current = ""
        for ch in string:
            if ch in separators:
                lis.append(current)
                lis.append(ch)
                current = ""
            else: current += ch

        lis.append(current)
        return lis

    lis = splitby(expr, "+-")
    def evaluate_mul_div(string):
        lis = splitby(string, "x/")
        if len(lis) == 1: return lis[0]

        output = float(lis[0])
        lis = lis[1:]

        while len(lis) > 0:
            operator = lis[0]
            number = float(lis[1])
            lis = lis[2:]

            if operator == "x": output *= number
            elif operator == "/": output /= number

        return output

    try:
        for i in range(len(lis)): lis[i] = evaluate_mul_div(lis[i])
        output = float(lis[0])
        lis = lis[1:]

        while len(lis) > 0:
            operator = lis[0]
            number = float(lis[1])
            lis = lis[2:]

            if operator == "+": output += number
            elif operator == "-": output -= number

    except ZeroDivisionError: output = "undefined"

    output = output if not str(output).endswith(".0") else int(output)
    return f"{expr} = {output}"
