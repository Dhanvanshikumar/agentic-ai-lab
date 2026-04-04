from tools import calculator, weather, summarize
from logger import log

def llm_decide(query):
    query = query.lower()

    if "calculate" in query:
        return "calculator"
    elif "weather" in query:
        return "weather"
    elif "summarize" in query:
        return "summarize"
    else:
        return "unknown"

def execute_tool(tool, query):

    if tool == "calculator":
        expression = query.replace("calculate", "")
        return calculator(expression)

    elif tool == "weather":
        return weather()

    elif tool == "summarize":
        text = query.replace("summarize", "")
        return summarize(text)

    else:
        return "I don't understand"

def main():
    query = input("Enter command: ")

    tool = llm_decide(query)

    result = execute_tool(tool, query)

    print("Output:", result)

    log(query, tool, result)

if __name__ == "__main__":
    main()