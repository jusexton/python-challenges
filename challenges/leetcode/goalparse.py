def interpret(text: str) -> str:
    return text.replace("()", "o").replace("(al)", "al")
