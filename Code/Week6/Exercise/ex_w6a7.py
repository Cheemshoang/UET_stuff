def calculator(a: float, b: float, s: str):
    if s == "-":
        return round(a-b, 2)
    elif s == "+":
        return round(a+b, 2)
    elif s == "*":
        return round(a*b, 2)
    elif s == "/":
        return round(a/b, 2)
