def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid expression"

def weather():
    return "Weather is sunny today"

def summarize(text):
    return text[:50] + "..."