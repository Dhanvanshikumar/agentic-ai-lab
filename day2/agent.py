from tools import calculator, weather, summarize

def input_handler():
    query = input("Enter command: ")
    return query

def decision_logic(query):
    query = query.lower()

    if "calculate" in query:
        return "calculator"
    elif "weather" in query:
        return "weather"
    elif "summarize" in query:
        return "summarize"
    else:
        return "unknown"

def action_execution(intent, query):

    if intent == "calculator":
        expression = query.replace("calculate", "")
        result = calculator(expression)
        print("Result:", result)

    elif intent == "weather":
        result = weather()
        print(result)

    elif intent == "summarize":
        text = query.replace("summarize", "")
        result = summarize(text)
        print(result)

    else:
        print("Sorry, I don't understand")

def main():
    query = input_handler()
    intent = decision_logic(query)
    action_execution(intent, query)

if __name__ == "__main__":
    main()