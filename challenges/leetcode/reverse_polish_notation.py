def reverse_polish_notation(tokens: list[str]) -> int:
    stack = []
    operands = "+-*/"
    for token in tokens:
        if token in operands:
            b, a = stack.pop(), stack.pop()
            match token:
                case "+":
                    result = a + b
                case "-":
                    result = a - b
                case "*":
                    result = a * b
                case _:
                    result = int(a / b)
            stack.append(result)
        else:
            stack.append(int(token))
    return stack[0]
