from datetime import datetime

def input_handler():
    query = input("Enter command: ")
    return query

def decision_logic(query):
    query = query.lower()

    if "hello" in query:
        return "greet"

    elif "date" in query:
        return "date"

    elif "calculate" in query:
        return "calculate"

    else:
        return "unknown"

def action_execution(intent, query):
    if intent == "greet":
        print("Hello! How can I help you?")

    elif intent == "date":
        print("Current date:", datetime.now())

    elif intent == "calculate":
        try:
            expression = query.replace("calculate", "")
            result = eval(expression)
            print("Result:", result)
        except:
            print("Invalid calculation")

    else:
        print("Sorry, I don't understand")

def main():
    query = input_handler()
    intent = decision_logic(query)
    action_execution(intent, query)

if __name__ == "__main__":
    main()